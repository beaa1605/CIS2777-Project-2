import ast
import operator

from src.config import get_llm


# Tool 1: Calculator
def calculator(expression: str) -> str:
    """Safely calculate basic math expressions."""

    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent is too large.")

            return operations[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp):
            value = evaluate(node.operand)

            if isinstance(node.op, ast.USub):
                return -value
            if isinstance(node.op, ast.UAdd):
                return value

        raise ValueError("Unsupported math expression.")

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)
        return str(result)
    except Exception as error:
        return f"Calculation error: {error}"


# Tool 2: Word Counter
def word_counter(text: str) -> str:
    """Count the words in a sentence."""

    words = text.split()
    return f"The text contains {len(words)} words."


# AI Tool Selection
def run_tool_chat():
    """Let the AI select and execute one of two tools."""

    llm = get_llm()

    print("\nAI Tool Assistant")
    print("Ask me to calculate something or count words.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not user_input:
            continue

        prompt = f"""
You are an assistant that chooses between two tools.

Available tools:
1. calculator: for mathematical expressions.
2. word_counter: for counting words in text.

User request: {user_input}

Respond in EXACTLY this format:
TOOL: calculator
INPUT: 25 * 4

OR

TOOL: word_counter
INPUT: hello world

Choose the appropriate tool. Do not calculate or count yourself.
"""

        try:
            response = llm.invoke(prompt).content.strip()

            lines = response.splitlines()
            tool_name = ""
            tool_input = ""

            for line in lines:
                if line.startswith("TOOL:"):
                    tool_name = line.replace("TOOL:", "", 1).strip().lower()
                elif line.startswith("INPUT:"):
                    tool_input = line.replace("INPUT:", "", 1).strip()

            if tool_name == "calculator":
                result = calculator(tool_input)

            elif tool_name == "word_counter":
                result = word_counter(tool_input)

            else:
                print("AI Assistant: I couldn't identify a valid tool.")
                continue

            print(f"\nAI Assistant: {result}\n")

        except Exception as error:
            print(f"Error: {error}")