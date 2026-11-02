from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from src.config import get_llm


def run_memory_chat():
    """Run a chat that remembers previous messages."""

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Remember the conversation."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | llm

    histories = {}

    def get_session_history(session_id: str):
        if session_id not in histories:
            histories[session_id] = InMemoryChatMessageHistory()
        return histories[session_id]

    chat = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    session_id = "student-session"

    print("\nAI Assistant: Memory chat started!")
    print("I'll remember our conversation.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("AI Assistant: Goodbye!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        try:
            response = chat.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )

            print(f"\nAI Assistant: {response.content}\n")

        except Exception as error:
            print(f"Error: {error}")