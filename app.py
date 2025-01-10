import streamlit as st
import requests
import json

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "ef164dfb-0249-410c-914b-25b31e6fa1da"
FLOW_ID = "ca015b8d-763c-4a95-bd7e-08632088af40"
ENDPOINT = "run"
APPLICATION_TOKEN = "AstraCS:aafYAbwZHSrMuRARgcxvLBtJ:7ff3dbd9285a018bead828aa5697b6a620d6197261790446aa05f262926d4726"

# Function to call Langflow API
def query_langflow(message):
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat"
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        try:
            # Extract message from nested response structure
            outputs = response.json().get("outputs", [])
            if outputs:
                results = outputs[0].get("outputs", [{}])[0].get("results", {})
                message = results.get("message", {}).get("data", {}).get("text", "No response generated.")
                return message
            else:
                return "No valid output found. Please try again."
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            st.error(f"Response Parsing Error: {e}")
            return "Error processing the response."
    else:
        return f"Failed to call API. Status code: {response.status_code}"

# Streamlit UI
st.title("Langflow Query Interface")

# Input form
with st.form("query_form"):
    user_query = st.text_input("Enter your query:")
    submit_button = st.form_submit_button("Submit")

# Displaying the result
if submit_button and user_query:
    with st.spinner("Processing..."):
        response_message = query_langflow(user_query)
    st.write("**Response:**")
    st.code(response_message, language='json')
