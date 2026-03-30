import ipaddress
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# Exercise 1: Custom Tool
@tool
def subnet_calculator(cidr: str) -> str:
    """Calculate network details from a CIDR notation string."""
    pass


# Exercise 2: Simple Agent
def build_network_agent():
    pass


# Exercise 3: Multi-Tool Agent
@tool
def read_file(file_path: str) -> str:
    """Read a file and return its contents."""
    pass


@tool
def count_words(text: str) -> str:
    """Count the number of words in a text."""
    pass


@tool
def summarize_text(text: str) -> str:
    """Summarize a text to its key points."""
    pass


def build_file_agent():
    pass


# Exercise 4: Structured Tool Input
class DNSLookupInput(BaseModel):
    hostname: str = Field(description="The hostname to look up")
    record_type: str = Field(description="DNS record type (A, AAAA, MX, CNAME, TXT)")


@tool(args_schema=DNSLookupInput)
def dns_lookup(hostname: str, record_type: str) -> str:
    """Perform a DNS lookup for a given hostname and record type."""
    pass


def build_dns_agent():
    pass


if __name__ == "__main__":
    # Exercise 1
    print(subnet_calculator.invoke("192.168.1.0/24"))

    # Exercise 2
    agent = build_network_agent()
    print(agent.invoke({"messages": [("user", "How many hosts fit in a /20 subnet?")]}))

    # Exercise 3
    file_agent = build_file_agent()
    print(file_agent.invoke({"messages": [("user", "Read ./docs/sample.txt, count the words, and summarize it")]}))

    # Exercise 4
    dns_agent = build_dns_agent()
    print(dns_agent.invoke({"messages": [("user", "Look up the MX records for google.com")]}))
