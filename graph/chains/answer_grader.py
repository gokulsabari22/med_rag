from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", temperature=0)

class AnswerGrader(BaseModel):
    binary_score: str = Field(
        description = "Answer addresses the question"
    )

structured_llm_grader = llm.with_structured_output(AnswerGrader)

system = """You are a grader assessing whether an answer addresses / resolves a question.
            Give a binary score 'yes' or 'no'. 'yes' means the answer resolves the question, 'no' means it doesn't.
            Respond with ONLY 'yes' or 'no'."""


answer_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "User question \n\n {question} \n\n LLM Generation \n\n {generation}")
])

answer_grader: RunnableSequence = answer_prompt | structured_llm_grader

if __name__ == "__main__":
    documents = """1 Introduction  \nCondition  \nRheumatoid arthritis (RA)  is an autoimmune systemic inflammatory arthritis.  RA affects 1 \npercent of the world’s population, including more than 1 million American adults.48 RA is \ncharacterized by  synovial inflammation  of joints, which can lead to progressive erosion of  bone , \nirreversible damage to the joint, loss of function, and resultant disability. The average incidence \nof RA in the United States is approximately 70 per 100,000 adults annually.49 RA can develop at \nany age , but incidence increases with age, peaking in the fifth decade .50 The i ncidence of RA is 2 \nto 3 times higher in women.  \nEtiology  \nThe etiology of RA is incompletely understood, but m ultiple environmental and genetic"""
    res = answer_grader.invoke({"question": "What causes Arthesis", "generation": documents})
    print(res.binary_score)