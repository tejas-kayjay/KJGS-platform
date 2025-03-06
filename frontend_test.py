import streamlit as st
import requests

# Create two columns: one for the sidebar and one for the chatbot
side_bar_col, chatbot_col = st.columns([1, 3])

# Sidebar
with side_bar_col:
    st.sidebar.title("Chatbot Configuration")



    # Create expandable sections
    with st.sidebar.expander("Section 1"):
        # Input field for website URL

       
        url = st.text_input("Enter Website URL", placeholder="https://example.com")

        
        # Submit button for backend functionality
        if st.button("Submit"):
            with st.spinner("Checking URL..."):
                try:
                    # Send the URL to the backend for checking
                    response = requests.post("http://localhost:8000/check_url", json={"url": url})
                    if response.status_code == 200:
                        result = response.json()["message"]
                        st.toast('Success, Webiste URL is crawled', icon="✅")
                        #st.write(result)
                    else:
                        st.toast('Error Occured ! Couldnt reach the website', icon="🚨")
                        #st.error("Error communicating with the backend server.")
                except requests.RequestException:
                    st.error("Could not connect to the backend server. Make sure it's running.")




    with st.sidebar.expander("Section 2"):
        st.checkbox("Subsection 2.1")
        st.checkbox("Subsection 2.2")

    with st.sidebar.expander("Section 3"):
        st.selectbox("Subsection 3.1", ["Item 1", "Item 2", "Item 3"])



# Custom CSS for button styling
st.markdown("""
<style>
.stButton > button {
    width: 100%;
    height: 50px;
}
</style>
""", unsafe_allow_html=True)





# Chatbot playground
with chatbot_col:
    st.title("Chatbot Playground")

    # Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# Suggested questions
suggested_questions = [
    "What is the weather like today?",
    "How do I reset my password?",
    "What are your business hours?"
]

    # Create columns for suggested question buttons
col1, col2, col3 = st.columns(3)
    
# Function to handle button click
def handle_button_click(question):
    st.session_state.messages.append({"role": "user", "content": question})
    response = f"This is a sample response to: {question}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.experimental_rerun()

# Add buttons for suggested questions
if col1.button(suggested_questions[0]):
    handle_button_click(suggested_questions[0])
if col2.button(suggested_questions[1]):
    handle_button_click(suggested_questions[1])
if col3.button(suggested_questions[2]):
    handle_button_click(suggested_questions[2])



# Chat input at the bottom of the page
if prompt := st.chat_input("What is your question?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response (replace this with your actual chatbot logic)
    response = f"This is a sample response to: {prompt}"
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})