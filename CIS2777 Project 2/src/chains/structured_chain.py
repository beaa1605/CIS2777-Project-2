import json

from pydantic import BaseModel, Field

from src.config import get_llm


class TopicSummary(BaseModel):
    summary: str = Field(description="A short explanation of the topic")
    key_points: list[str] = Field(description="Exactly three important points")


def run_structured_chain(topic: str) -> dict:
    """Generate and validate structured information about a topic."""

    llm = get_llm().bind(format="json")

    prompt = f"""
    Explain the topic: {topic}

    Return ONLY a valid JSON object with exactly these fields:
    {{
        "summary": "A short explanation of the topic",
        "key_points": [
            "First important point",
            "Second important point",
            "Third important point"
        ]
    }}

    The key_points list must contain exactly three points.
    Do not return a JSON schema. Return actual information.
    """

    response = llm.invoke(prompt)

    data = json.loads(response.content)

    validated = TopicSummary.model_validate(data)

    if len(validated.key_points) != 3:
        raise ValueError("The response must contain exactly three key points.")

    return validated.model_dump()