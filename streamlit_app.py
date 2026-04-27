import streamlit as st
import requests

st.title("🚨 AI 災情可信度分析系統")

text = st.text_area("輸入災情描述")
location = st.text_input("地點")
time = st.text_input("時間")

if st.button("分析"):
    data = {
        "text": text,
        "location": location,
        "time": time
    }

    try:
        res = requests.post("http://127.0.0.1:8000/analyze", json=data)
        result = res.json()

        st.subheader("分析結果")
        st.write(result)

    except:
        st.error("請先啟動 FastAPI")