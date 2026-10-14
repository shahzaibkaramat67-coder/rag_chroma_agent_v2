from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
from pathlib import Path

Path(__file__).resolve()


base_dir = Path(__file__).resolve().parent

documents_file = base_dir / "document" / "FYP_Blog_Site_Final.pdf"

Agent_file = base_dir / "Agent"

loader = PyPDFLoader(str(documents_file))

documents = loader.load()

print("PAGES:", len(documents))
print("FIRST PAGE:")
print(documents[0].page_content[:1000])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)

chunks = text_splitter.split_documents(documents)

print("CHUNKS:", len(chunks))

embedding = HuggingFaceEmbeddings(model="zamanemon/text-embadding-0.1")

vectorStore = Chroma.from_documents(
    documents=chunks, embedding=embedding, persist_directory=str(Agent_file)
)

print("CURRENT DIRECTORY:", os.getcwd())
# print("CHROMA PATH:", os.path.abspath("Agent/RAG_02/Chromadb"))
print("CHROMA COUNT:", vectorStore._collection.count())


# # from langchain_pdf import PyPDFLoader
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
# from pathlib import Path

# import os

# path = r"D:\document\FYP_BlogWebsite_Final_Document.pdf"

# print("path of the document:", Path(path))
# document = PyPDFLoader(path)
# loadDocument = document.load()

# documentSpliter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)

# chunks = documentSpliter.split_documents(loadDocument)


# print("Chunk count : ", chunks)


# embedding = HuggingFaceEmbeddings(model_name="zamanemon/text-embadding-0.1")

# createDb = Chroma.from_documents(
#     embedding=embedding,
#     documents=chunks,
#     persist_directory="Agent/RAG_02/Chromadb",
# )


# print("createDb._collection.count : ", createDb._collection.count())
