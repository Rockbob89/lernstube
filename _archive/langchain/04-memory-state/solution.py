from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Session store for exercise 2+
session_store = {}


def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


# Exercise 1: Manual Message History
def chat_with_history(history) -> str:
    pass


# Exercise 2: Runnable with History
def build_conversational_chain():
    pass


# Exercise 3: Window Memory
def build_windowed_chain(window_size: int = 2):
    pass


# Exercise 4: Compare Memory Types
def compare_memory_types():
    pass


if __name__ == "__main__":
    # Exercise 1
    history = InMemoryChatMessageHistory()
    history.add_user_message("My name is Sergio")
    history.add_ai_message("Hello Sergio!")
    history.add_user_message("What is my name?")
    print("Ex1:", chat_with_history(history))

    # Exercise 2
    chain = build_conversational_chain()
    config = {"configurable": {"session_id": "user-1"}}
    print("Ex2a:", chain.invoke({"input": "I work with Kubernetes"}, config=config))
    print("Ex2b:", chain.invoke({"input": "What do I work with?"}, config=config))

    # Exercise 3
    wchain = build_windowed_chain(window_size=2)

    # Exercise 4
    compare_memory_types()
