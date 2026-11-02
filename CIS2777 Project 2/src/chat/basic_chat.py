from src.config import get_llm


def run_basic_chat():
    """Run a multi-turn chat without memory."""

    llm = get_llm()

    print("\nAI Assistant: Chat started!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("AI Assistant: Goodbye!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        try:
            response = llm.invoke(user_input)
            print(f"\nAI Assistant: {response.content}\n")

        except Exception as error:
            print(f"Error: {error}")