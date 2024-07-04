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

# Question Asked
What causes rheumatoid arthritis?

# Generated Response
Rheumatoid arthritis (RA) is caused by a combination of genetic and environmental factors. Genetic factors include the Major Histocompatibility Complex (MHC) Class II shared epitope, while environmental factors include obesity, smoking, nulliparity, low socioeconomic status, viral and bacterial infections, and possibly the microbiome.

![image](https://github.com/gokulsabari22/med_rag/assets/57941940/2d899274-5b56-4265-b745-f189d0c00e7a)


# Graph (Generated from code)
![graph](https://github.com/gokulsabari22/med_rag/assets/57941940/9fe2ea40-7a7d-464e-8590-a7436647037f)

# Graph (From documentation)
![image](https://github.com/gokulsabari22/self_rag/assets/57941940/75bf0ef3-1b60-4cdb-8ccc-10031cef5cdf)




