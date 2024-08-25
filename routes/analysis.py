from flask import jsonify
from models.symptom_model import analyze_symptoms

def analyze_symptoms_route(data):
    symptoms = data.get('symptoms')
    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400
    
    analysis_result = analyze_symptoms(symptoms)
    return jsonify({"analysis": analysis_result})
