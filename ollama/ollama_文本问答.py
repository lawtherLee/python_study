import ollama
import time

while True:
    prompt = input("请输入问题：")

    if prompt.lower() in ["exit", "quit", "退出", "886"]:
        print("退出对话...")
        break

    # 记录开始时间
    start_time = time.time()

    response = ollama.chat(
        model="deepseek-r1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    # 记录结束时间
    end_time = time.time()
    elapsed_time = end_time - start_time

    result = response.message.content

    # 输出主要结果
    print(f"JARVIS:{result}")

    # 输出额外信息
    print(f"响应时间: {elapsed_time:.4f} 秒")
    print(f"模型名称: {response.model}")
    print(f"完成原因: {response.done_reason}")
    print("-" * 50)  # 分隔线
