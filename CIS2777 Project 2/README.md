# CIS 2777 Project 2: AI Assistant

Created by: Selina Balawi

## About the Project

For this project I created an AI assistant using Python and LangChain. It runs in the terminal and has five features. It can answer questions and organize information. It can also remember conversations and use simple tools.

## Features

1. Template Chain: Generates answers about different topics.
2. Structured Output: Creates a summary and three key points in JSON format.
3. Basic Chat: Allows users to have conversations with the AI.
4. Memory Chat: Remembers information from earlier messages.
5. Tool Chat: Uses a calculator and a word counter.

## Installation

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install the required packages:

    pip install -r requirements.txt

Install Ollama from https://ollama.com.

Download the model:

    ollama pull llama3.2:3b

Make sure Ollama is running before starting the program.

## How to Run

Template Chain:
    python -m src.main template --topic "Python programming"

Structured Output:
    python -m src.main structured --input "Cybersecurity"

Basic Chat:
    python -m src.main chat

Memory Chat:
    python -m src.main memory-chat

Tool Chat:
    python -m src.main tool-chat

Type exit to end a chat session.

## Running Tests

Run the tests with:

    python -m unittest discover -s tests -v

The project includes four automated tests for the calculator and word counter. All four tests passed during testing.

## Technologies Used

Python
LangChain
Ollama
Llama 3.2
Pydantic
Unittest

## Screenshots

The screenshots folder contains examples of the program features and automated test results.