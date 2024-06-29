from graph.chains.retrieve_grader import retrieval_grader
from graph.state import GraphState
from langchain.schema import Document

def grade_document(state: GraphState):
    question = state["question"]
    documents = state["documents"]

    web_search = False
    filtered_docs = []
    for docs in documents:
        score = retrieval_grader.invoke({"question": question, "documents": docs.page_content})
        grade = score.binary_score

        if grade.lower() == "yes":
            filtered_docs.append(docs)
        else:
            web_search = True
            continue
    
    return {"documents": filtered_docs, "question": question, "web_search": web_search}

if __name__ == "__main__":
    inputs = {'documents': [Document(page_content='1 Introduction  \nCondition  \nRheumatoid arthritis (RA)  is an autoimmune systemic inflammatory arthritis.  RA affects 1 \npercent of the world’s population, including more than 1 million American adults.48 RA is \ncharacterized by  synovial inflammation  of joints, which can lead to progressive erosion of  bone , \nirreversible damage to the joint, loss of function, and resultant disability. The average incidence \nof RA in the United States is approximately 70 per 100,000 adults annually.49 RA can develop at \nany age , but incidence increases with age, peaking in the fifth decade .50 The i ncidence of RA is 2 \nto 3 times higher in women.  \nEtiology  \nThe etiology of RA is incompletely understood, but m ultiple environmental and genetic', metadata={'page': 26.0, 'source': 'data\\Bookshelf_NBK524950.pdf'}), Document(page_content='Loss of red blood cells: acute or chronic haemorrhage (gastrointestinal ulcer, ancylostomiasis, schistosomiasis,\netc.);\nIncreased destruction of red blood cells (haemolysis): parasitic (malaria), bacterial and viral (HIV) infections;\nhaemoglobinopathies (sickle cell disease, thalassaemia); intolerance to certain drugs (primaquine, dapsone, co-\ntrimoxazole, nitrofurantoin, etc.) in patients with G6PD deﬁciency.\nCommon signs: pallor of the conjunctivae, mucous membranes, palms of hands and soles of feet; fatigue,\ndizziness, dyspnoea, tachycardia, heart murmur.', metadata={'page': 37.0, 'source': 'data\\guideline-170-en.pdf'}), Document(page_content='Ref-5 47. Mukherjee K, Kamal KM. Socio -demographic factors and out -of-pocket expenditure for \nprescription drugs in rheumatoi d arthritis. Value Health. 2016;19(3):A232. \n48. Wasserman AM. Diagnosis and management of rheumatoid arthritis. Am Fam Physician. \n2011 Dec 01;84(11):1245- 52. PMID: 22150658.  \n49. Ruffing V, Bingham, III, C. O. Rheumatoid Arthritis Signs and Symptoms. Johns Hopkins Arthritis Center; 2017. \nhttps://www.hopkinsarthritis.org/arthritis -\ninfo/rheumatoid- arthritis/ra -symptoms/#epi . Accessed on April 27 2017.', metadata={'page': 578.0, 'source': 'data\\Bookshelf_NBK524950.pdf'})], 'question': 'What causes the symptoms of Rhuematoid Arthesis', 'generation': 'I am sorry, but the provided context does not contain the answer to what causes the symptoms of Rheumatoid Arthritis.'}

    result = grade_document({'question': inputs['question'], 'documents': inputs['documents']})
    print(result)