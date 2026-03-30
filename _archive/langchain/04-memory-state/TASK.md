# Task 4: Memory & State

## Objective
Add conversation memory to LangChain chains so the model can reference prior messages.

## What to Learn
- `InMemoryChatMessageHistory` and message types (HumanMessage, AIMessage, SystemMessage)
  ```python
  from langchain_core.chat_history import InMemoryChatMessageHistory
  history = InMemoryChatMessageHistory()
  history.add_user_message("Hello")
  history.add_ai_message("Hi there!")
  ```
- `RunnableWithMessageHistory` for LCEL-based memory — wraps a chain and automatically injects/appends history per session
  ```python
  from langchain_core.runnables.history import RunnableWithMessageHistory
  chain_with_history = RunnableWithMessageHistory(chain, get_session_history,
                                                  input_messages_key="input",
                                                  history_messages_key="history")
  ```
- Session ID management for multi-user scenarios — pass `{"configurable": {"session_id": "user-1"}}` as `config` to `invoke`
- Implementing windowed memory by trimming message history — slice `history.messages[-N*2:]` before passing to the model
- Implementing summary memory by condensing older messages — use the model to summarize older turns, then replace them with a single `SystemMessage`
- When each pattern is appropriate (full buffer for short, summary for long, window for recent)

## Exercises

### 1. Manual Message History
Create a `ChatMessageHistory`, add messages manually, and pass them to a model. Show that the model can reference earlier messages.

```python
history = build_history()
history.add_user_message("My name is Sergio")
history.add_ai_message("Hello Sergio!")
history.add_user_message("What is my name?")
response = chat_with_history(history)
# -> should know the name is Sergio
```

### 2. Runnable with History
Build a chain using `RunnableWithMessageHistory` that automatically manages history per session ID.

```python
chain = build_conversational_chain()
config = {"configurable": {"session_id": "user-1"}}
chain.invoke({"input": "I work with Kubernetes"}, config=config)
chain.invoke({"input": "What do I work with?"}, config=config)
# -> "Kubernetes"
```

### 3. Window Memory
Build a chain that only remembers the last N exchanges. Demonstrate that older messages are forgotten.

```python
chain = build_windowed_chain(window_size=2)
# After 3+ exchanges, the first exchange should be forgotten
```

### 4. Compare Memory Types
Write a script that runs the same 5-message conversation through buffer, window (k=2), and summary memory. Print the internal memory state after each message for all three. Observe the differences.
