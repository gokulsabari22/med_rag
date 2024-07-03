# Self RAG 

# Medical Question Answering System for Rheumatoid Arthritis
This repository contains a Medical Question Answering System designed to retrieve, grade, and generate responses to medical queries. The system leverages various models and tools to ensure the responses are relevant and accurate.

# Overview
The workflow of the system is depicted in the graph below:


# Workflow Description
1) Retrieve: The system starts by retrieving relevant documents related to the medical query.
2) Grade Document: Retrieved documents are then graded to assess their relevance.
3) Web Search (Conditional): If the retrieved documents are not sufficient or relevant, a web search is initiated to find more information.
4) Generate: Based on the retrieved and/or web-searched documents, a response is generated.
5) Grade Generation: The generated response is evaluated to determine if it is grounded in the provided documents and addresses the question.
   
    a) If the response is useful, the process ends.
   
    b) If the response is not useful, another web search is initiated.
   
    c) If the response is not supported by the documents, another response is generated.

# Models and Tools Used
1) LLM Model: llama3-8b-8192 (from Groq)
2) Embedding Model: text-embedding-004 (Google)
3) Search Tool: Tavily AI
4) Vector Database: Pinecone

