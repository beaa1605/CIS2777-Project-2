from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.config import get_llm


def run_template_chain(topic: str) -> str:
    """Generate a short AI response about a given topic."""

    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["topic"],
        template=(
            "You are a helpful educational assistant. "
            "Explain the following topic clearly and simply: {topic}"
        )
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain.invoke({"topic": topic})