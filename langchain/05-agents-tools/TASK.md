# Task 5: Agents & Tools

## Objective
Build LangChain agents that can use tools to interact with external systems and make decisions.

## What to Learn
- `@tool` decorator for defining custom tools — the docstring becomes the tool description the model sees
  ```python
  from langchain_core.tools import tool

  @tool
  def add(a: int, b: int) -> int:
      """Add two integers."""
      return a + b
  ```
- `langgraph.prebuilt.create_react_agent` and the ReAct reasoning pattern — the agent alternates: think → pick tool → observe result → repeat until done
  ```python
  from langgraph.prebuilt import create_react_agent
  agent = create_react_agent(llm, tools=[add])
  ```
- Agent configuration: `recursion_limit` for controlling iterations — prevents infinite tool-call loops
  ```python
  agent.invoke({...}, config={"recursion_limit": 10})
  ```
- Built-in tools and community tool integrations — e.g. `DuckDuckGoSearchRun`, `WikipediaQueryRun` from `langchain_community.tools`
- Tool input schemas with Pydantic — define a `BaseModel` as the `args_schema` for multi-field tools with validation
  ```python
  class DnsInput(BaseModel):
      hostname: str
      record_type: str = "A"

  @tool(args_schema=DnsInput)
  def dns_lookup(hostname: str, record_type: str) -> str: ...
  ```
- Agent observation/thought/action loop — visible in the message list returned; each `ToolMessage` is an observation
- langgraph message-based input/output format
  ```python
  result = agent.invoke({"messages": [("user", "What is 2+3?")]})
  print(result["messages"][-1].content)
  ```

## Exercises

### 1. Custom Tool
Create a tool using `@tool` that takes a CIDR notation string and returns the network address, broadcast address, and number of hosts.

```python
result = subnet_calculator.invoke("192.168.1.0/24")
# -> "Network: 192.168.1.0, Broadcast: 192.168.1.255, Hosts: 254"
```

### 2. Simple Agent
Create a ReAct agent with the subnet calculator tool and a general knowledge tool. Ask it questions that require tool use.

```python
agent = build_network_agent()
result = agent.invoke({"messages": [("user", "How many hosts fit in a /20 subnet?")]})
```

### 3. Multi-Tool Agent
Create an agent with 3+ tools: a file reader (reads a file and returns contents), a word counter, and a summarizer. Ask it to read a file, count its words, and summarize it.

```python
agent = build_file_agent()
result = agent.invoke({"messages": [("user", "Read ./docs/sample.txt, count the words, and summarize it")]})
```

### 4. Structured Tool Input
Create a tool with a Pydantic input schema (e.g., a DNS lookup tool that takes hostname and record_type). Show that the agent correctly populates both fields.

```python
agent = build_dns_agent()
result = agent.invoke({"messages": [("user", "Look up the MX records for google.com")]})
```
