from graph.graph import app
from dotenv import load_dotenv

load_dotenv()

def run_llm(question: str):
    result = app.invoke({"question": question})
    return result

if __name__ == "__main__":
    res = run_llm(question="What causes Migrane?")
    print(res)