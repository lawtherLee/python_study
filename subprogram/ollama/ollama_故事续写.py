import ollama

response = ollama.chat(model="deepseek-r1:8b", messages=[{
    "role": "user",
    "content": "请将下面这段内容续写，请勿重复内容。蝙蝠侠回到了哥谭"
}])

# result = response.get("message").get("content")
result = response.message.content
print(result)
