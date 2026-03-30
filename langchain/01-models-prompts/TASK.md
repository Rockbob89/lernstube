# Task 1: Models & Prompts

## Objective
Work with LangChain's LLM and ChatModel wrappers, build prompt templates, and parse structured output.

## What to Learn
- `ChatOpenAI` / `ChatAnthropic` — model wrappers and their parameters (temperature, model, max_tokens)
  ```python
  from langchain_openai import ChatOpenAI
  llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
  ```
- `PromptTemplate` and `ChatPromptTemplate` — variable substitution, system/human message templates
  ```python
  from langchain_core.prompts import ChatPromptTemplate
  prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a {role}."),
      ("human", "{question}"),
  ])
  ```
- `OutputParser` — `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser`
  ```python
  from langchain_core.output_parsers import StrOutputParser
  chain = prompt | llm | StrOutputParser()
  ```
- `.invoke()` vs `.batch()` vs `.stream()`
  ```python
  chain.invoke({"role": "expert", "question": "..."})
  chain.batch([{"role": "expert", "question": "a"}, ...])
  for chunk in chain.stream(...): print(chunk, end="")
  ```
- Format instructions for structured output — parsers expose `get_format_instructions()` to inject into the prompt so the model knows the expected schema

## Exercises

### 1. Basic Invocation
Write a function that takes a topic string and returns a one-sentence explanation from the model.

```python
result = explain_topic("Kubernetes CRDs")
# -> "Custom Resource Definitions extend the Kubernetes API..."
```

### 2. Prompt Templates
Write a function that uses `ChatPromptTemplate` with a system message ("You are a {role}") and a human message ("{question}"). Return the model's response.

```python
result = ask_as_role("security auditor", "Is eval() safe in Python?")
```

### 3. Structured Output
Write a function that asks the model to analyze a technology and returns a Pydantic model with fields: `name`, `category`, `pros` (list[str]), `cons` (list[str]).

```python
analysis = analyze_tech("Redis")
# -> TechAnalysis(name="Redis", category="Database", pros=[...], cons=[...])
```

### 4. Batch and Stream
Write a function that takes a list of topics and batch-invokes the model for summaries. Write a second function that streams a response token by token, printing each chunk.

```python
results = batch_explain(["gRPC", "GraphQL", "REST"])
stream_explain("service mesh")  # prints token by token
```
