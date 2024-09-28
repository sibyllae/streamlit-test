import streamlit as st

# 側邊欄顯示
with st.sidebar:
    st.write("故事故事  \n故事故事  \n故事故事  \n故事故事  \n故事故事")
    # 在側邊欄中嵌入 iframe
    st.components.v1.html(
        """
        <iframe src="http://127.0.0.1:5500/index.html" 
                width="300" height="400" 
                style="border:none;">
        </iframe>
        """, 
        height=400
    )

# 主頁面內容
st.write("主頁面的內容")
