from google import genai
from google.genai import errors, types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MAX_TOKENS = 1000

while True:
    prompt = input("You: ").strip()
    if prompt.lower() == "exit":
        print("Have a nice day!!!")
        break
    if not prompt:
        continue

    try:
        response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt,
                                                  config=types.GenerateContentConfig(max_output_tokens=MAX_TOKENS,
                                                automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)))

        print(f"\nGemini: {response.text}\n")
    except errors.APIError as e:
        # Handle 429 Resource Exhausted / Rate Limit errors
        if e.code == 429 or "RESOURCE_EXHAUSTED" in str(e):
            print("\n[Quota Reached] API rate limit or quota exceeded. Exiting program gracefully...")
            break
        else:
            print(f"\n[API Error {e.code}]: {e.message}")
            break
    except Exception as e:
        print(f"\n[Error]: An unexpected error occurred: {e}")
        break

