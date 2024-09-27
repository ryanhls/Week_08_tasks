import streamlit as st

st.title("About this App")

st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")

"1. Enter your prompt in the text area."
"2. Click the 'submit' button."
"3. The app will generate the text completion based on your prompt."

st.divider()

with st.expander("Tips"):
    st.write("1. I want to learn programming.")
    st.write("2. Is there any Python courses?")
    st.write("3. AI related courses.")
