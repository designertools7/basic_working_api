from openai import OpenAI
client = OpenAI()

response  = client.responses.create(
    model="gpt-5",
    input="list top 10 universities in the wester United States",
)

print(response.output_text)