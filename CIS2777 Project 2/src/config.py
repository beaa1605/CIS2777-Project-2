from langchain_ollama import ChatOllama


def get_llm():
    """Create and return the local language model."""

    return ChatOllama(
        model="llama3.2:3b",
        temperature=0.7
    )