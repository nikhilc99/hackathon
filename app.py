from flask import Flask, request, jsonify, render_template
#from models.symptom_model import analyze_symptoms
from routes.analysis import analyze_symptoms
from routes.recommend import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle symptom analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    return analyze_symptoms(data)

# Route to handle herbal and dietary recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    return get_recommendations(data)

if __name__ == '__main__':
    app.run(debug=True, host="10.73.73.112")

@app.route('/analyze-report', methods=['POST'])
def analyze_report():
    if 'report' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['report']
    # Process the file here. For now, we're just simulating a response.
    condition = "simulated_condition_based_on_file"

    # Use Gen-AI to analyze the condition
    prompt = f"Analyze the following condition based on test report: {condition}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100
    )
    analysis_result = response.choices[0].text.strip()

    # Simulated recommendations based on analysis result
    recommendations = recommend_treatment(analysis_result)
    return jsonify({"recommendations": recommendations})

