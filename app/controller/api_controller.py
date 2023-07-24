# Importing necessary packages
from flask import Flask, request, jsonify
from app.services.recommendation_service import generate_recommendations

# Creating a Flask app instance
app = Flask(__name__)

# Defining the API route to handle GET requests for product recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Extractinng the 'customer_id' parameter from the request URL
    customer_id = request.args.get('customer_id')

    # Checking if customer ID is provided in the request
    if not customer_id:
        response = {
            'error': 'Customer ID is missing',
            'status': 400
        }
        return jsonify(response), 400

    # Invoking 'generate_recommendations' function to get similarity product recommendations
    recommendations = generate_recommendations(customer_id)

    # Handling different cases based on the 'recommendations' returned
    if 'error' in recommendations:
        # If an error occurred during recommendation generation, return the error message
        response = {
            'error': recommendations['error'],
            'status': 400
        }
        return jsonify(response), 400
    elif recommendations:
        # If recommendations are generated successfully, return top 10 recommendations
        response = {
            'recommendations': recommendations,
            'status': 200
        }
        return jsonify(response), 200
    else:
        # If no recommendations are found for the given customer, return an error message
        response = {
            'error': 'No recommendations found',
            'status': 404
        }
        return jsonify(response), 404

# Run the Flask app on default port 5000 (you can change it accordingly)
if __name__ == '__main__':
    app.run(port=5000)
