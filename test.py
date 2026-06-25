from agents import llm

response = llm.invoke("Hello, tell me what you can do")

print(response.content)