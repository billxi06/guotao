import streamlit as st
import base64

# 直接渲染HTML文件
def render_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    render_html("a.html") 