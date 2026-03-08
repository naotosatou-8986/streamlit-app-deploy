import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

def get_llm_response(user_input, expert):

    system_messages = {
        "税務アドバイザー": "あなたは税務の専門家です。初心者にもわかりやすく説明してください。",
        "マーケティング専門家": "あなたはマーケティングの専門家です。具体的なアドバイスをしてください。"
    }

    llm = ChatOpenAI(model="gpt-4.1-mini")

    messages = [
        SystemMessage(content=system_messages[expert]),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)

    return response.content


st.title("LLM相談アプリ")

st.write("専門家を選んで質問するとAIが回答します")

expert = st.radio(
    "専門家を選んでください",
    ["税務アドバイザー", "マーケティング専門家"]
)

user_input = st.text_area("質問を書いてください")

if st.button("送信"):

    if user_input:

        answer = get_llm_response(user_input, expert)

        st.write(answer)