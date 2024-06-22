from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from const import INDEX_NAME
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

loader = PyPDFDirectoryLoader("data/")

document = loader.load()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=200,
    chunk_overlap=0
)

docs = text_splitter.split_documents(document)

# doc_search = PineconeVectorStore.from_documents(documents=docs, embedding=embedding, index_name=INDEX_NAME)

vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embedding)

question = "What causes Rhuematoid Arthesis"
result = vectorstore.similarity_search(query=question, k=2)
for res in result:
    print(res.page_content)
    print("\n")
    print("\n")