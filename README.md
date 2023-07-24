# Project Title: Customer Product Recommendation API

## Overview
This project is an API that provides personalized product recommendations to customers based on their purchase history. It utilizes collaborative filtering and cosine similarity to find similar customers and recommend products that other similar customers have purchased. The API is built using Flask.

## Features
- **Personalized Recommendations**: The API takes a customer ID as input and returns a list of top 10 product recommendations tailored to that specific customer based on their purchase history.

- **Error Handling**: The API handles various error cases, such as missing customer ID, invalid input type for customer ID, and when no recommendations are found for the given customer.

## Software Requirements
- Python (developed on 3.11.4)
- Flask
- Werkzeug
- pandas
- scikit-learn
- MySQL

## How to Run the API
1. Clone the repository and navigate to the project directory.
2. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
3. Update the database configuration in the `config.py` file to connect to your MySQL database.
4. Start the Flask development server:
   ```
   python api_controller.py
   ```
   The API will be available at `http://localhost:5000`.

## Endpoints

### 1. /recommendations [GET]
This endpoint returns top 10 personalized product recommendations for a specific customer.

**Request Parameters:**
- customer_id: The ID of the customer for whom recommendations are needed.

**Response:**
- If the customer ID is missing or not provided in the request, the API will respond with a 400 Bad Request error and an error message in JSON format.

- If the customer ID is of invalid type or if invalid customer ID is given as input, the API will respond with a 400 Bad Request error and an error message in JSON format.

- If the customer ID is valid and recommendations are successfully generated, the API will respond with a 200 OK status code and a JSON object containing the top 10 product recommendations for the customer.

- If no recommendations are found for the given customer, the API will respond with a 404 Not Found error and an error message in JSON format.

## Unit Tests
The project includes a comprehensive set of unit tests to verify the functionality of the API. To run the tests, use the following command:
```
python test_api_controller.py
```

## Database Schema
The API relies on a MySQL database that contains the customer purchase history. The `PurchaseHistory` class in `customer_model.py` is responsible for fetching the relevant data from the database and creating a DataFrame.
SQL Dump file provided can be used. Most of the columns are purposfully named varchar type so that it can be handled in the main code itself as a part of Data Cleaning
