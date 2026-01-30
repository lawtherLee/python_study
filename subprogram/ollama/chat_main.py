import streamlit as st
from textwrap import dedent
from langchain_classic.memory import ConversationBufferMemory
from chat_utils import get_response

welcome_msg = dedent(
    """
 **我是小易👋，有什么问题想问吗？我可以做到：**
> 
> 1.  **教育辅助**
>     - 核心价值：解题步骤可视化、个性化习题生成
>     - 示例任务：数学题详解、编程入门答疑、错题本智能分析
>     
> 2.  **开发提效**
>     - 核心价值：代码生成/调试、测试用例编写
>     - 示例任务：接口实现、Bug修复、代码重构建议
>     
> 3.  **企业办公**
>     - 核心价值：文档自动化、智能检索
>     - 示例任务：合同条款审查、会议纪要生成、知识库问答
>     
> 4.  **边缘智能**
>     - 核心价值：本地数据隐私计算
>     - 示例任务：工业质检逻辑判断、车载语音助手、离线客服
"""
)

st.title("ecominfo - LLM")

# 判断是否有历史消息
if "memory" not in st.session_state:  # 存储会话状态的字典 用于存储会话数据
    st.session_state["memory"] = ConversationBufferMemory()
    st.session_state["messages"] = [{"role": "assistant", "content": welcome_msg}]

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接受录入的关键词
prompt = st.chat_input("请输入问题：")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.spinner("正在玩命思考中...", show_time=True):
        response = get_response(st.session_state["messages"])

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
