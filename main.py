# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("hi")
# print(result)

chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")
# result = chat_model.predict("코딩에 대한 시를 써줘")
# print(result)

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요')

if st.button('시 작성하기'):
    with st.spinner('시 작성중...'):
        result = chat_model.predict(content+"에 대한 시를 써줘")
        st.write(result)
