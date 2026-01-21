import ollama
import time


def get_response(prompt):
    start_time = time.time()
    response = ollama.chat(
        model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}]
    )
    end_time = time.time()
    print(f"大模型响应时间：{(end_time-start_time):.2f}秒")
    return response.message.content


if __name__ == "__main__":
    prompt = "hi"
    print(get_response(prompt))
