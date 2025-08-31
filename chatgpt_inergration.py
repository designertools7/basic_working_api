import openai
import os

#Set your API key here
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

#ChatGPT prompt
def chat_with_gpt():
    prompt = "Hello, ChatGPT! Can you tell me a joke?"

    response = openai.Completion.create(
        model= "gpt-5",
        prompt=prompt,
        max_tokens=100,
    )

    print("Response from ChatGPT:", response.choices[0].text.strip())
          
if __name__ == "__main__":
    chat_with_gpt() 