import streamlit as st
from vertexai.language_models import CodeChatModel

code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")
st.title("Code Generator Using codechat-bison@001")
prompt = st.text_input("Enter the code generation prompt")
code_chat = code_chat_model.start_chat()
#  check if prompt is not empty
if prompt:
    #  send the prompt to the model and get the response
    response = code_chat.send_message(prompt)
    #  display the response
    st.write('Generated code is ', response.text)
