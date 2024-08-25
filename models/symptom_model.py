import openai

# Initialize the OpenAI API client
openai.api_key = 'sk-02tLwXmZEViiFxWwzSP_ip1W8glSY3tUfHKnmSiOuMT3BlbkFJDZ-Pku2R1FmoX3vAgWIQtC7x3DjLzWWrExDQOss5oA'

def analyze_symptoms(symptoms):
    prompt = f"Analyze the following symptoms and suggest possible health conditions: {symptoms}"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
