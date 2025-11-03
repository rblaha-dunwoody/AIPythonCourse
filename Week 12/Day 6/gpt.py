from openai import OpenAI

# -- Set OpenAI API key --

client = OpenAI()

try:
    # Generate text using GPT-3.5 Turbo
    response = client.responses.create(
        model="gpt-5",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    
    print("Generated Text:\n", response.output_text)

except Exception as e:
    print(f"An error occurred: {e}")