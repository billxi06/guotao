import streamlit as st
import os

# 设置页面标题
st.set_page_config(page_title="CSS 实验网页")

# 模拟导航栏
nav_style = """
<style>
nav {
    background-color: #ac0fac3e;
    overflow: hidden;
}
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
nav ul li {
    float: left;
}
nav ul li a {
    display: block;
    color: rgb(220, 239, 11);
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}
nav ul li a:hover {
    background-color: #12e80f;
}
</style>
"""
st.markdown(nav_style, unsafe_allow_html=True)
nav_html = """
<nav>
    <ul>
        <li><a href="#">首页</a></li>
        <li><a href="#">关于我们</a></li>
        <li><a href="#">服务</a></li>
        <li><a href="#">联系我们</a></li>
    </ul>
</nav>
"""
st.markdown(nav_html, unsafe_allow_html=True)

# 模拟浮动框
box_style = """
<style>
.float-box {
    float: left;
    width: 30%;
    margin: 1.5%;
    padding: 20px;
    background-color: #970af6;
    box-sizing: border-box;
}
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
a {
    color: #f30808;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
"""
st.markdown(box_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='float-box'>", unsafe_allow_html=True)
    st.header("浮动框 1")
    try:
        st.image("image1.jpg", width=205, caption="图片 1")
    except FileNotFoundError:
        st.write("未找到图片 1")
    st.write("VIP内容请付费查看")
    st.markdown("<a href='#'>了解更多</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='float-box'>", unsafe_allow_html=True)
    st.header("浮动框 2")
    try:
        st.image("image2.jpg", width=250, caption="图片 2")
    except FileNotFoundError:
        st.write("未找到图片 2")
    st.write("SVIP内容请在充值VIP的基础上进行充值，然后点击浏览")
    st.markdown("<a href='#'>了解更多</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='float-box'>", unsafe_allow_html=True)
    st.header("浮动框 3")
    try:
        st.image("666.gif", width=250, caption="图片 3")
    except FileNotFoundError:
        st.write("未找到图片 3")
    st.write("这是一个需要比特币才能打开的内容")
    st.markdown("<a href='#'>了解更多</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)