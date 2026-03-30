# Task 3: Retrieval & RAG

## Objective
Build a retrieval-augmented generation pipeline: load documents, split, embed, store in a vector DB, and query.

## What to Learn
- Document loaders: `TextLoader`, `WebBaseLoader`, `PyPDFLoader`
  ```python
  from langchain_community.document_loaders import TextLoader
  docs = TextLoader("./docs/sample.txt").load()
  ```
- Text splitters: `RecursiveCharacterTextSplitter` and chunk size/overlap tradeoffs — larger chunks preserve context; smaller chunks improve retrieval precision; overlap prevents losing information at boundaries
  ```python
  from langchain_text_splitters import RecursiveCharacterTextSplitter
  splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
  chunks = splitter.split_documents(docs)
  ```
- Embeddings: `OpenAIEmbeddings` (or alternatives)
  ```python
  from langchain_openai import OpenAIEmbeddings
  embeddings = OpenAIEmbeddings()
  ```
- Vector stores: `Chroma` or `FAISS` for local dev
  ```python
  from langchain_chroma import Chroma
  vectorstore = Chroma.from_documents(chunks, embeddings)
  ```
- Retriever interface and `as_retriever()`
  ```python
  retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
  ```
- RAG chain: retrieve context, stuff into prompt, generate answer — retriever feeds `context` into the prompt alongside the `question`

## Exercises

### 1. Load and Split
Write a function that loads a text file and splits it into chunks. Return the chunks and print count + average length.

```python
chunks = load_and_split("./docs/sample.txt", chunk_size=500, overlap=50)
# -> [Document(...), Document(...), ...]
```

### 2. Embed and Store
Write a function that takes chunks, embeds them, and stores them in a Chroma (or FAISS) vector store. Return the store.

```python
vectorstore = embed_and_store(chunks)
```

### 3. Retrieval
Write a function that queries the vector store and returns the top-k most relevant chunks.

```python
results = retrieve(vectorstore, "What is a sidecar container?", k=3)
```

### 4. RAG Chain
Build a full RAG chain: retriever | prompt (with context + question) | model | parser. The prompt should instruct the model to answer based only on the provided context.

```python
rag = build_rag_chain(vectorstore)
answer = rag.invoke("How do init containers work?")
```

### 5. Create Test Corpus
Create a `docs/` folder with 2-3 text files on a topic you know (e.g., Kubernetes concepts). Use these as your test corpus for exercises 1-4.
