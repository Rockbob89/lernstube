import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import Client as LangSmithClient

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# Exercise 1: Traced Invocation
def traced_invoke(chain, inputs: dict, run_name: str = "default") -> str:
    pass


# Exercise 2: Create Evaluation Dataset
def create_eval_dataset(dataset_name: str):
    pass


# Exercise 3: Run Evaluation
def evaluate_chain(chain, dataset_name: str):
    pass


# Exercise 4: Compare Prompts
def compare_prompts(prompt_a, prompt_b, dataset_name: str):
    pass


if __name__ == "__main__":
    # Build a simple chain for testing
    prompt = ChatPromptTemplate.from_template("Answer concisely: {question}")
    chain = prompt | model | StrOutputParser()

    # Exercise 1
    print(traced_invoke(chain, {"question": "What port does SSH use?"}, run_name="ssh-test"))

    # Exercise 2
    dataset = create_eval_dataset("infra-qa")
    print(f"Dataset created: {dataset}")

    # Exercise 3
    evaluate_chain(chain, dataset_name="infra-qa")

    # Exercise 4
    prompt_a = ChatPromptTemplate.from_template("Answer concisely: {question}")
    prompt_b = ChatPromptTemplate.from_template(
        "You are a senior infrastructure engineer. Answer precisely: {question}"
    )
    compare_prompts(prompt_a, prompt_b, dataset_name="infra-qa")
