Conversational Analytics API Codelab

This directory contains the boilerplate code for the Conversational Analytics API codelab. The files are designed to be used as a starting point for building conversational AI applications with BigQuery.

## File Descriptions

### Core Files

*   `main.py`: A simple "Hello World" entry point. Not used in the main application logic.
*   `chat_utils.py`: Utility functions for the chat application, such as `show_message` to display the chat response.

### Agent Creation

*   `create_agent.py`: A script to create a data agent for the Google Trends dataset. This is the original boilerplate script.
*   `create_agent_so.py` and `create_agent_so_v2.py`: Versions of the agent creation script, likely for different iterations or use cases (e.g., Stack Overflow data).
*   `create_agent_equi.py`: A script to create a data agent for the Equi.com synthetic dataset. This was created as part of the Equi.com demo.

### Conversation Management

*   `create_conversation.py`: A script to create a conversation for the Google Trends agent. This is the original boilerplate script.
*   `create_conversation_so.py` and `create_conversation_so_v2.py`: Versions of the conversation creation script, likely for different iterations or use cases.
*   `create_conversation_equi.py`: A script to create a conversation for the Equi.com agent. This was created as part of the Equi.com demo.

### Chat Interaction

*   `chat.py`: A script to interact with the Google Trends agent. This is the original boilerplate script.
*   `chat_so.py` and `chat_so_v2.py`: Versions of the chat script, likely for different iterations or use cases.
*   `chat_equi.py`: A script to interact with the Equi.com agent. This was created as part of the Equi.com demo.

### Other Scripts

*   `get_agent.py`: A script to retrieve information about a data agent.
*   `test_agent.py`: A script to test the functionality of a data agent.
*   `query.sql`: A sample SQL query.

### Web Interface

*   `index.html`: A simple HTML file, likely for a web-based chat interface.

## How to Use and Edit the Code (for LLMs)

This section outlines the workflow for creating a new demo based on the boilerplate code in this directory.

### 1. Understand the Goal

Start by understanding the user's request. This includes:

*   The target domain (e.g., a specific company or industry).
*   The type of data to be used (e.g., synthetic or existing BigQuery dataset).

### 2. Research and Storytelling

*   If a website is provided, use web research to understand the business domain.
*   Create a user persona and a compelling demo story to showcase the capabilities of the Conversational Analytics API.

### 3. Data Preparation

*   **Synthetic Data:**
    *   If the user requests synthetic data, create a new Python script (e.g., `generate_data.py`) outside of this directory.
    *   Define a relevant BigQuery schema for the tables.
    *   Use libraries like `Faker` to generate realistic data.
    *   Use the `google-cloud-bigquery` library to create a dataset and upload the data.
*   **Existing Data:**
    *   If the user provides an existing dataset, analyze the schema and data to understand its structure and content.

### 4. Adapt the Boilerplate Code

**IMPORTANT:** Do not modify the original boilerplate files (`create_agent.py`, `create_conversation.py`, `chat.py`). Always create copies with descriptive names (e.g., `create_agent_your_domain.py`).

*   **Agent Creation:**
    1.  Copy `create_agent.py` to a new file (e.g., `create_agent_your_domain.py`).
    2.  Change the `data_agent_id` to a unique name for your agent.
    3.  Update the `system_instruction` string with:
        *   The persona of the agent.
        *   Detailed descriptions of the tables and their fields.
        *   `join_instructions` to guide the agent on how to join tables.
        *   `golden_queries` with examples of natural language questions and their corresponding SQL queries.
    4.  Modify the `datasource_references` to point to your BigQuery tables.

*   **Conversation Creation:**
    1.  Copy `create_conversation.py` to a new file (e.g., `create_conversation_your_domain.py`).
    2.  Update the `data_agent_id` to match the one you created.
    3.  Change the `conversation_id` to a unique name for your conversation.

*   **Chat Interaction:**
    1.  Copy `chat.py` to a new file (e.g., `chat_your_domain.py`).
    2.  Update the `data_agent_id` and `conversation_id` to match the ones you created.
    3.  Modify the `question` variable to ask the questions from your demo story.

### 5. Execution and Testing

*   Run the scripts in the following order:
    1.  Data generation script (if you created one).
    2.  Agent creation script.
    3.  Conversation creation script.
    4.  Chat script (run this for each question in your demo story).
*   If a query fails, analyze the error, and try to simplify or rephrase the question. The agent's understanding is guided by the system instructions, so you may need to refine them.

### 6. Create an All-in-One Script (Optional)

For convenience, you can create a single script (e.g., `run_demo.py`) that combines the logic from the agent creation, conversation creation, and chat interaction scripts. This allows the user to run the entire demo with a single command
