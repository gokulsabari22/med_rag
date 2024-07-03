from langgraph.graph import END, StateGraph
from graph.const import RETRIEVE, GRADE_DOCUMENT, GENERATE, WEBSEARCH
from graph.nodes import generate, grade_document, retrieve, websearch
from graph.chains.hallucination_grader import hallunication_grader
from graph.chains.answer_grader import answer_grader 
from graph.state import GraphState
from dotenv import load_dotenv

load_dotenv()


def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")

    if state["web_search"]:
        print(
            "---DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE WEB SEARCH---"
        )
        return WEBSEARCH
    else:
        print("---DECISION: GENERATE---")
        return GENERATE
    
def grade_generation_grounded_in_documents_and_question(state: GraphState) -> str:
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]

    score = hallunication_grader.invoke({"documents": documents, "generation": generation})
    print(f"SCORE: {score.binary_score}")
    if hallunication_grade := score.binary_score:
        print("-----------GENERATION IS GROUNDED IN DOCUMENT--------------------")
        score = answer_grader.invoke({"question": question, "generation": generation})
        
        if answer_grade := score.binary_score:
            print("-----------------GENERATED ANSWER ADDRESS QUESTION---------------")
            return "useful"
        else:
            print("--------------------GENERATED ANSWER DOES NOT ADDRESSES QUESTION----------------")
            return "not useful"
    else:
        print("------------------GENERATED ANSWER IS NOT PRESENT IN THE DOCUMENT-----------------")
        return "not supported"



workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENT, grade_document)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, websearch)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENT)

workflow.add_conditional_edges(
    GRADE_DOCUMENT,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

workflow.add_conditional_edges(
    GENERATE,
    grade_generation_grounded_in_documents_and_question,
    {
        "not supported": GENERATE,
        "useful": END,
        "not useful": WEBSEARCH
    }
)

workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")