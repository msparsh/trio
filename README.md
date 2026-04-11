# Trio: Multi-Agent Collaborative Coding System

This project demonstrates Multi-Agent Collaborative Coding, using `langgraph` to build a system where distinct agents (Product Manager, Developer, QA Tester) work together to turn a text prompt into a functional, tested Python script.

## System Overview
![banner](./assets/banner.png)

The system orchestrates three specialized AI agents—the Product Manager, Developer, and QA Tester—to collaboratively refine a solution from a single text prompt:

1.  **Product Manager (PM):** Plans the steps required to solve the task.
2.  **Coder:** Writes the actual code based on the PM's plan and incorporates feedback.
3.  **QA Agent:** Critically reviews the generated code, either approving it or providing detailed feedback for iteration.

## Technology Stack

*   **Framework:** LangGraph
*   **LLM:** Ollama (using the Local Gemma model)
*   **Language:** Python

## Usage

To run the system, execute `main.py`. The initial state is predefined with a sample problem.
