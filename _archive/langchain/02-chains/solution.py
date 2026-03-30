from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# Exercise 1: Simple Chain
def build_summary_chain():
    pass


# Exercise 2: Multi-Step Chain
def build_deep_dive_chain():
    pass


# Exercise 3: Parallel Chains
def build_parallel_analysis():
    pass


# Exercise 4: Conditional Routing
def build_routed_chain():
    pass


if __name__ == "__main__":
    summary_chain = build_summary_chain()
    print(summary_chain.invoke({"topic": "container networking"}))

    deep_dive_chain = build_deep_dive_chain()
    print(deep_dive_chain.invoke({"technology": "Helm"}))

    parallel_analysis = build_parallel_analysis()
    print(parallel_analysis.invoke({"topic": "microservices"}))

    routed_chain = build_routed_chain()
    print(routed_chain.invoke({"question": "How does eBPF work?"}))
    print(routed_chain.invoke({"question": "What's a good lunch spot?"}))
