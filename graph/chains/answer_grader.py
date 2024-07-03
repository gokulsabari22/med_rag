from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", temperature=0)

class AnswerGrader(BaseModel):
    binary_score: bool = Field(
        description = "Answer addresses the question"
    )

structured_llm_grader = llm.with_structured_output(AnswerGrader)

system = """You are a grader assessing whether an answer address / resolves a question \n
             Give a binary score 'yes' or 'no'. 'yes' means the answer resolves a question"""

answer_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "User question \n\n {question} \n\n LLM Generation \n\n {generation}")
])

answer_grader: RunnableSequence = answer_prompt | structured_llm_grader