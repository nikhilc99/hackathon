from flask import jsonify
from models.recommendation_model import recommend_treatment

def get_recommendations(data):
    condition = data.get('condition')
    if not condition:
        return jsonify({"error": "No condition provided"}), 400
    
    recommendations = recommend_treatment(condition)
    return jsonify({"recommendations": recommendations})
