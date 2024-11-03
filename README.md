# Chat with SQL Database using Langchain

This project allows you to chat with an SQL database with using Langchain Agents and LLama. You can connect to either a local SQLite database or a MySQL database and interact with it using natural language queries.

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/OnurAsimIlhan/chat-sqldb-using-langchain.git
    cd https://github.com/OnurAsimIlhan/chat-sqldb-using-langchain.git
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your environment variables. For example:

    ```env
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Run the SQLite script to create and populate the database:**

    ```sh
    python sqlite.py
    ```

2. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

3. **Interact with the app:**

    - Open your browser and go to `http://localhost:8501`.
    - Select the database type (SQLite or MySQL) from the sidebar.
    - If using MySQL, provide the necessary connection details.
    - Enter your Groq API key in the sidebar.
    - Ask questions in the chat interface to interact with the database.
