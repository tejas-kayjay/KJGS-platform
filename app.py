import streamlit as st

st.set_page_config(layout="wide")

# Sidebar
st.sidebar.title("Chatbot Builder")

# Build section
st.sidebar.header("Build")

# Instructions subsection
st.sidebar.subheader("Instructions")
chatbot_instructions = st.sidebar.text_area("Enter chatbot instructions")

# Knowledge base subsection
st.sidebar.subheader("Knowledge Base")
knowledge_option = st.sidebar.radio("Select knowledge source", ["Crawl webpages", "Upload files"])

if knowledge_option == "Crawl webpages":
    website_url = st.sidebar.text_input("Enter website URL")
else:
    uploaded_files = st.sidebar.file_uploader("Upload files", accept_multiple_files=True)

# Main content area
st.title("Chatbot Playground")

# Placeholder for chatbot interface
st.write("Chatbot interface will appear here based on sidebar settings.")
