# Task 6: Evaluation

## Objective
Evaluate LangChain chains and RAG pipelines using LangSmith tracing and programmatic evaluation.

## What to Learn
- LangSmith tracing setup (`LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY`) — set these env vars and every chain call is traced automatically
  ```bash
  export LANGCHAIN_TRACING_V2=true
  export LANGCHAIN_API_KEY=ls__...
  export LANGCHAIN_PROJECT=my-project
  ```
- Creating evaluation datasets — a dataset is a collection of (input, expected output) examples
  ```python
  from langsmith import Client
  client = Client()
  dataset = client.create_dataset("infra-qa")
  client.create_examples(inputs=[{"question": "What port does HTTPS use?"}],
                         outputs=[{"answer": "443"}], dataset_id=dataset.id)
  ```
- Built-in evaluators: correctness, relevance, faithfulness — LangSmith provides LLM-as-judge evaluators for these; use them via `evaluate()`
- Custom evaluators with scoring functions — a function that takes `(run, example)` and returns a dict with `key` and `score`
  ```python
  def exact_match(run, example):
      predicted = run.outputs["output"].lower()
      expected = example.outputs["answer"].lower()
      return {"key": "exact_match", "score": int(expected in predicted)}
  ```
- Comparing chain variants (A/B testing prompts) — run `evaluate()` twice with different chains against the same dataset, then compare scores
- `langsmith.evaluate()` API
  ```python
  from langsmith.evaluation import evaluate
  results = evaluate(chain.invoke, data="infra-qa", evaluators=[exact_match])
  ```

## Exercises

### 1. Tracing Setup
Enable LangSmith tracing via environment variables. Run a chain and verify the trace appears in the LangSmith UI. Write a function that wraps a chain call with a custom run name.

```python
result = traced_invoke(chain, {"topic": "Kubernetes"}, run_name="k8s-summary")
```

### 2. Evaluation Dataset
Create a dataset of 5+ question-answer pairs programmatically using the LangSmith SDK. Topics should be from your domain (infra/DevOps).

```python
dataset = create_eval_dataset("infra-qa")
# -> dataset with examples like ("What port does HTTPS use?", "443")
```

### 3. Run Evaluation
Evaluate a QA chain against the dataset using a custom evaluator that checks if the expected answer appears in the response.

```python
results = evaluate_chain(chain, dataset_name="infra-qa")
# -> prints pass/fail per example and overall score
```

### 4. Compare Prompts
Create two prompt variants for the same task. Run both against the dataset and compare scores. Print a summary table.

```python
compare_prompts(prompt_a, prompt_b, dataset_name="infra-qa")
# -> "Prompt A: 4/5, Prompt B: 3/5"
```
