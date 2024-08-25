import openai

# Initialize the OpenAI API client
openai.api_key = ''

def analyze_symptoms(symptoms):
    prompt = f"Analyze the following symptoms and suggest possible health conditions: {symptoms}"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
