from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from functools import reduce

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import add

app = Flask(__name__)
CORS(app)

@app.route("/api/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        numbers = data.get("numbers", [])
        if not isinstance(numbers, list):
            return jsonify({"error": "Numbers must be provided as an array"}), 400
            
        if not numbers or len(numbers) < 2:
            return jsonify({"error": "Please provide at least two numbers"}), 400
        
        # Convert string numbers to float and validate
        try:
            numbers = [float(n) if n else 0 for n in numbers]
        except (ValueError, TypeError):
            return jsonify({"error": "All inputs must be valid numbers"}), 400
        
        # Calculate the sum
        result = reduce(add, numbers)
        
        # Check for valid result
        if not isinstance(result, (int, float)) or result == float('inf') or result == float('-inf'):
            return jsonify({"error": "Calculation resulted in an invalid number"}), 400
            
        return jsonify({
            "result": result,
            "operation": "add",
            "numbers": numbers
        })
    except Exception as e:
        app.logger.error(f"Error in calculation: {str(e)}")
        return jsonify({"error": "An error occurred while calculating"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5002)
