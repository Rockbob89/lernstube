from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field


model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# Exercise 1: Basic Invocation
def explain_topic(topic: str) -> str:
    pass


# Exercise 2: Prompt Templates
def ask_as_role(role: str, question: str) -> str:
    pass


# Exercise 3: Structured Output
class TechAnalysis(BaseModel):
    name: str = Field(description="Technology name")
    category: str = Field(description="Category (e.g. Database, Framework)")
    pros: list[str] = Field(description="List of advantages")
    cons: list[str] = Field(description="List of disadvantages")


def analyze_tech(tech_name: str) -> TechAnalysis:
    pass


# Exercise 4: Batch and Stream
def batch_explain(topics: list[str]) -> list[str]:
    pass


def stream_explain(topic: str) -> None:
    pass


if __name__ == "__main__":
    # Test exercise 1
    print(explain_topic("Kubernetes CRDs"))

    # Test exercise 2
    print(ask_as_role("security auditor", "Is eval() safe in Python?"))

    # Test exercise 3
    print(analyze_tech("Redis"))

    # Test exercise 4
    print(batch_explain(["gRPC", "GraphQL", "REST"]))
    stream_explain("service mesh")
