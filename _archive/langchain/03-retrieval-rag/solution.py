from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings()


# Exercise 1: Load and Split
def load_and_split(file_path: str, chunk_size: int = 500, overlap: int = 50):
    pass


# Exercise 2: Embed and Store
def embed_and_store(chunks):
    pass


# Exercise 3: Retrieval
def retrieve(vectorstore, query: str, k: int = 3):
    pass


# Exercise 4: RAG Chain
def build_rag_chain(vectorstore):
    pass


if __name__ == "__main__":
    chunks = load_and_split("./docs/sample.txt")
    print(f"Loaded {len(chunks)} chunks")

    vectorstore = embed_and_store(chunks)
    print("Vector store created")

    results = retrieve(vectorstore, "What is a sidecar container?", k=3)
    for doc in results:
        print(doc.page_content[:100])

    rag = build_rag_chain(vectorstore)
    print(rag.invoke("How do init containers work?"))
