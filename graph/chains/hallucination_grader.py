from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", temperature=0)

class GradeHallucination(BaseModel):
    binary_score: bool = Field(
        description="Anser is grounded in Facts. 'yes' or 'no'"
    )

structured_llm_grader = llm.with_structured_output(GradeHallucination)

system = """You are a grader assessing wheather an LLM generation is grounded in/supported by a set of received facts. \n
            Give a binary score 'yes' or 'no'. 'yes' means that the answer is grounded in/ suppoerted by facts"""

hallunication_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "Set of facts: \n\n {documents} \n\n LLM Generation {generation}")
])

hallunication_grader: RunnableSequence = hallunication_prompt | structured_llm_grader 