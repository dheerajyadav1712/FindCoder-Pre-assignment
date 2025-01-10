# LangFlow Query Interface

This project is a Streamlit-based web application that allows users to interact with a LangFlow API. The app takes user queries as input, sends them to the LangFlow backend via an API, and displays AI-generated responses.

## Features

- **User-Friendly Interface**: Simple form-based UI to input queries and receive responses.
- **LangFlow Integration**: Connects to a LangFlow API instance to process queries and generate intelligent answers.
- **Real-Time Processing**: The app displays the response in real-time after submitting a query.
- **Error Handling**: Handles API errors and response parsing errors gracefully.

## How It Works

1. The user enters a query in the input box.
2. Upon submission, the query is sent to the LangFlow API endpoint.
3. The LangFlow backend processes the query using a predefined flow and returns the result.
4. The app extracts and displays the relevant response to the user.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.8+
- Streamlit
- Requests

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/FindCoder-Pre-assignment.git
   cd FindCoder-Pre-assignment
