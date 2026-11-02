import argparse

from src.chains.template_chain import run_template_chain
from src.chains.structured_chain import run_structured_chain
from src.chat.basic_chat import run_basic_chat
from src.chat.memory_chat import run_memory_chat
from src.tools.tool_chat import run_tool_chat


def main():
    parser = argparse.ArgumentParser(
        description="CIS 2777 Modular AI Assistant"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    template_parser = subparsers.add_parser("template")
    template_parser.add_argument("--topic", required=True)

    structured_parser = subparsers.add_parser("structured")
    structured_parser.add_argument("--input", required=True)

    subparsers.add_parser("chat")
    subparsers.add_parser("memory-chat")
    subparsers.add_parser("tool-chat")

    args = parser.parse_args()

    try:
        if args.command == "template":
            print(run_template_chain(args.topic))

        elif args.command == "structured":
            result = run_structured_chain(args.input)
            print(result)

        elif args.command == "chat":
            run_basic_chat()

        elif args.command == "memory-chat":
            run_memory_chat()

        elif args.command == "tool-chat":
            run_tool_chat()

    except Exception as error:
        print(f"Application error: {error}")


if __name__ == "__main__":
    main()