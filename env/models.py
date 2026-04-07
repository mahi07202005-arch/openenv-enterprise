from openai import OpenAI

client = OpenAI()

def simple_model(input_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a smart AI agent."},
                {"role": "user", "content": input_text}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("⚠️ Using fallback model due to API issue:", e)
        return f"(Fallback) Improved response for: {input_text}"