from openai import OpenAI
client = OpenAI()

response  = client.responses.create(
    model="gpt-5",
    input="create a lesson plan for seventh grader learning about density mass and volume",
)

print(response.output_text)