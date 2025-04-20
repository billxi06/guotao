import streamlit as st

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
boxes_html = """
<div class="clearfix">
    <div class="float-box">
        <h2>浮动框 1</h2>
        <img src ="image1.jpg" alt="图片 1" width="205px">
        <p>VIP内容请付费查看</p>
        <a href="#">了解更多</a>
    </div>
    <div class="float-box">
        <h2>浮动框 2</h2>
        <img src ="image2.jpg" alt="图片 2" width="250px">
        <p>SVIP内容请在充值VIP的基础上进行充值，然后点击浏览</p>
        <a href="#">了解更多</a>
    </div>
    <div class="float-box">
        <h2>浮动框 3</h2>
        <img src ="666.gif" alt="图片 3" width="250px">
        <p>这是一个需要比特币才能打开的内容</p>
        <a href="#">了解更多</a>
    </div>
</div>
"""
st.markdown(boxes_html, unsafe_allow_html=True)