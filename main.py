import streamlit as st
from ai_utils import generate_response
from file_utility import save_to_file, read_from_file

# Constants
DATA_FILE = "data_log.txt"

# In-memory storage for unique prompts
unique_prompts = set()
prompt_response_list = []

# Functions
def validate_input(user_input: str) -> bool:
    """
    Validates the user input.

    :param user_input: The input query from the user.
    :return: True if valid, False otherwise.
    """
    return bool(user_input.strip())

# Streamlit UI
st.title("GenAI Python Developer Helper")

menu = st.sidebar.selectbox(
    "Menu",
    options=["Generate Response", "View Log", "About"]
)

if menu == "Generate Response":
    st.header("Generate a Response")
    user_input = st.text_area("Enter your query:", "")
    
    if st.button("Generate"):
        if not validate_input(user_input):
            st.warning("Please enter some valid text!")
        else:
            if user_input in unique_prompts:
                st.warning("This query has already been processed. Try a new one!")
            else:
                try:
                    # Generate response
                    response = generate_response(user_input)
                    st.text_area("Generated Response:", response, height=300)
                    
                    # Add to in-memory storage
                    unique_prompts.add(user_input)
                    prompt_response_list.append((user_input, response))
                    
                    # Save to log file
                    save_to_file(f"Query: {user_input}\nResponse: {response}\n{'-' * 50}", DATA_FILE)
                    
                    st.success("Response saved to log.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

elif menu == "View Log":
    st.header("View Saved Logs")
    logs = read_from_file(DATA_FILE)
    st.text_area("Log Contents:", logs, height=400)

elif menu == "About":
    st.header("About")
    st.write("""
        ## GenAI Python Developer Helper  
        This app uses Google's GenAI to assist with Python-related queries.  
        
        **Features:**  
        - Generate meaningful responses to Python queries.  
        - Save unique queries and responses to a log file.  
        - View previously saved logs.  
        - Validates user inputs and handles errors gracefully.  
        
        **Developer:** DENIZA SULEYMANOVA ®  
    """)
