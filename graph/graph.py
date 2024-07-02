from langgraph.graph import END, StateGraph
from graph.const import RETRIEVE, GRADE_DOCUMENT, GENERATE, WEBSEARCH
from graph.nodes import generate, grade_document, retrieve, websearch
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
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

# app.get_graph().draw_mermaid_png(output_file_path="graph.png")