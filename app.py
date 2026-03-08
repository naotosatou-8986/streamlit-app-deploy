import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


def get_llm_response(user_input: str, expert_type: str) -> str:
    system_prompts = {
        "税務アドバイザー": (
            "あなたは日本の税務に詳しい専門家です。"
            "初心者にもわかりやすく、やさしく整理して説明してください。"
        ),
        "マーケティングアドバイザー": (
            "あなたは実務に強いマーケティング専門家です。"
            "具体的で実行しやすいアドバイスをしてください。"
        ),
    }

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.7,
    )

    messages = [
        SystemMessage(content=system_prompts[expert_type]),
        HumanMessage(content=user_input),
    ]

    response = llm.invoke(messages)
    return response.content


st.set_page_config(page_title="専門家LLM相談アプリ", page_icon="🤖")

st.title("🤖 専門家LLM相談アプリ")
st.write("入力した内容に対して、選んだ専門家の立場でAIが回答するWebアプリです。")

st.subheader("使い方")
st.write("1. 専門家を選びます")
st.write("2. 質問や相談内容を入力します")
st.write("3. 送信を押すと回答が表示されます")

expert_type = st.radio(
    "専門家を選んでください",
    ["税務アドバイザー", "マーケティングアドバイザー"]
)

user_input = st.text_area("質問を書いてください")

if st.button("送信"):
    if not user_input.strip():
        st.warning("質問を入力してください。")
    else:
        with st.spinner("回答を作成中です..."):
            answer = get_llm_response(user_input, expert_type)
        st.subheader("回答")
        st.write(answer)