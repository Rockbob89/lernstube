# Task 2: Chains

## Objective
Compose LangChain components into chains using LCEL (LangChain Expression Language).

## What to Learn
- LCEL pipe operator (`|`) for composing runnables — each component's output becomes the next component's input
  ```python
  chain = prompt | llm | StrOutputParser()
  chain.invoke({"topic": "gRPC"})
  ```
- `RunnablePassthrough`, `RunnableParallel`, `RunnableLambda`
  ```python
  from langchain_core.runnables import RunnablePassthrough, RunnableParallel
  # pass input through unchanged (useful for merging with other keys)
  chain = RunnablePassthrough() | llm
  # run two chains simultaneously
  parallel = RunnableParallel(pros=pros_chain, cons=cons_chain)
  ```
- Chain input/output schemas — use `.input_schema` and `.output_schema` to inspect what a chain expects/returns
- Sequential composition: prompt | model | parser — the standard LCEL pattern
- Branching and parallel execution — `RunnableParallel` fans out; a lambda or `RunnableBranch` can route based on content

## Exercises

### 1. Simple Chain
Build a chain: `prompt | model | StrOutputParser()` that takes a `{"topic": "..."}` dict and returns a summary string.

```python
result = summary_chain.invoke({"topic": "container networking"})
```

### 2. Multi-Step Chain
Build a chain that first generates a list of key concepts for a technology, then explains each concept. Use two prompts chained together.

```python
result = deep_dive_chain.invoke({"technology": "Helm"})
# -> detailed explanation built from extracted concepts
```

### 3. Parallel Chains
Use `RunnableParallel` to run two analyses simultaneously: one generating pros, one generating cons. Merge the results.

```python
result = parallel_analysis.invoke({"topic": "microservices"})
# -> {"pros": "...", "cons": "..."}
```

### 4. Conditional Routing
Build a chain that classifies input as "technical" or "general", then routes to different prompt templates based on the classification.

```python
result = routed_chain.invoke({"question": "How does eBPF work?"})       # -> technical answer
result = routed_chain.invoke({"question": "What's a good lunch spot?"})  # -> general answer
```
