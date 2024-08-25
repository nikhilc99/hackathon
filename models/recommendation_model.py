import json

# Load herbal and food data
with open('data/herbs.json') as f:
    herbs_data = json.load(f)
with open('data/foods.json') as f:
    foods_data = json.load(f)

def recommend_treatment(condition):
    herbs = herbs_data.get(condition, [])
    foods = foods_data.get(condition, [])
    
    return {"herbs": herbs, "foods": foods}

