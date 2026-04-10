from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Student specific configuration
STUDENT_ROLL_NUMBER = 22  # Your roll number used as seed [cite: 48]
REG_NUMBER = "FA22-BAI-022" # Your registration number [cite: 61]

# Fixed procedure to generate coefficients based on the seed [cite: 46]
random.seed(STUDENT_ROLL_NUMBER)
a1 = random.uniform(-5, 5) [cite: 50]
a2 = random.uniform(-5, 5) [cite: 51]
a3 = random.uniform(-5, 5) [cite: 52]
b = random.uniform(-10, 10) [cite: 53]

@app.route('/predict', methods=['GET'])
def predict():
    """
    Accepts x1, x2, x3 as URL parameters and returns a prediction 
    based on the linear regression equation: y = a1*x1 + a2*x2 + a3*x3 + b
    """
    try:
        # Accept input parameters through API call [cite: 40, 58]
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
        x3 = float(request.args.get('x3', 0))
        
        # Linear regression calculation [cite: 44]
        prediction = (a1 * x1) + (a2 * x2) + (a3 * x3) + b
        
        # Return the prediction as a JSON response [cite: 42, 59]
        return jsonify({
            "registration number": REG_NUMBER,
            "prediction": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # The API must be exposed on port 5000 
    # host='0.0.0.0' allows the container to accept external requests 
    app.run(host='0.0.0.0', port=5000)
