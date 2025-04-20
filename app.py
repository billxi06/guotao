import streamlit as st
import base64


def generate_html():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS 实验网页</title>
    <style>
        /* 全局样式 */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        /* 菜单样式 */
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

        /* 浮动框样式 */
        .float-box {
            float: left;
            width: 30%;
            margin: 1.5%;
            padding: 20px;
            background-color: #970af6;
            box-sizing: border-box;
        }

        /* 清除浮动 */
        .clearfix::after {
            content: "";
            display: table;
            clear: both;
        }

        /* 超链接样式 */
        a {
            color: #f30808;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <!-- 菜单 -->
    <nav>
        <ul>
            <li><a href="#">首页</a></li>
            <li><a href="#">关于我们</a></li>
            <li><a href="#">服务</a></li>
            <li><a href="#">联系我们</a></li>
        </ul>
    </nav>

    <!-- 浮动框 -->
    <div class="clearfix">
        <div class="float-box">
            <h2>浮动框 1</h2>
            <!-- 替换图片1路径 -->
            <img src="image1.jpg" alt="图片 1" width="205px">
            <p>VIP内容请付费查看</p>
            <a href="#">了解更多</a>
        </div>
        <div class="float-box">
            <h2>浮动框 2</h2>
            <!-- 替换图片2路径 -->
            <img src="image2.jpg" alt="图片 2" width="250px">
            <p>SVIP内容请在充值VIP的基础上进行充值，然后点击浏览</p>
            <a href="#">了解更多</a>
        </div>
        <div class="float-box">
            <h2>浮动框 3</h2>
            <!-- 替换图片3路径（GIF动图） -->
            <img src="666.gif" alt="图片 3" width="250px">
            <p>这是一个需要比特币才能打开的内容</p>
            <a href="#">了解更多</a>
        </div>
    </div>
</body>
</html>
"""
    return html_content


# 使用说明
if __name__ == "__main__":
    # 生成HTML文件
    with open("generated_page.html", "w", encoding="utf-8") as f:
        f.write(generate_html())

    print("HTML文件已生成！请按以下步骤操作：")
    print("1. 图片位置说明：")
    print("   - 浮动框1图片：替换 image1.jpg")
    print("   - 浮动框2图片：替换 image2.jpg")
    print("   - 浮动框3动图：替换 666.gif")
    print("2. 请确保图片文件与生成的HTML文件在同一目录")
    print("3. 或使用绝对路径（例如：/static/images/image1.jpg）")
    