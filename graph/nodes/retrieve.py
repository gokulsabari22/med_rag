from graph.state import GraphState
from document_loader import vectorstore
from typing import Dict, Any


def retrieve(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = vectorstore.similarity_search(question, k=1)
    return {"Question": question, "Documents": documents}

if __name__ == "__main__":
    res = retrieve(state={"question": "What causes the symptoms of Rhuematoid Arthesis"})
    # result = [answer.page_content for answer in res["Documents"]]
    print(res)