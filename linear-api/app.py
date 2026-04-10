from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Student Details
ROLL_NUMBER = "FA22-BAI-022" 
seed = 22  
random.seed(seed)

# Fixed procedure for coefficient generation [cite: 47-53]
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b  = random.uniform(-10, 10)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Accept parameters x1, x2, x3 [cite: 58]
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
        x3 = float(request.args.get('x3', 0))

        # Equation: y = a1*x1 + a2*x2 + a3*x3 + b [cite: 44]
        y = a1*x1 + a2*x2 + a3*x3 + b

        return jsonify({
            "registration number": ROLL_NUMBER,
            "prediction": round(y, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Must be exposed on port 5000 [cite: 56]
    app.run(host='0.0.0.0', port=5000)
