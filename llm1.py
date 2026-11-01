# This program demonstrates the use of OpenAI's GPT model to generate responses based on user prompts.
# Uses Open AI SDK to interact with the GPT model.

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def ask_gpt(prompt):
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.output_text


def main():
    prompt = input("Enter your prompt: ")

    answer = ask_gpt(prompt)

    print("\nGPT Response:")
    print(answer)


if __name__ == "__main__":
    main()