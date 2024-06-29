from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.schema import Document
from graph.state import GraphState
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", temperature=0)

search = TavilySearchResults(max_results=3)

def websearch(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = state["documents"]

    tavily_result = search.invoke({"query": question})
    results = "\n".join([result["content"] for result in tavily_result])
    web_result = Document(page_content=results)
    
    if documents is not None:
        documents.append(web_result)
    else:
        documents = [web_result]

    return {"documents": documents, "question": question}

if __name__ == "__main__":
    res = websearch(state={"question": "What causes Migrane?", "documents": None})
    print(res)