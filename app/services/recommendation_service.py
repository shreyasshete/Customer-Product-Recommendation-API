from app.model.customer_model import PurchaseHistory
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def generate_recommendations(customer_id):
    try:
        target_customer_id = int(customer_id)

        # Get the input dataframe
        data = PurchaseHistory.get_purchase_history()

        # Preprocess the data
        # Converting CustomerID to integer type
        data['CustomerID'] = data['CustomerID'].astype(str).str.split('.').str[0]
        data['CustomerID'] = data['CustomerID'].astype(int)

        # User-Item Matrix
        user_item_matrix = pd.crosstab(data['CustomerID'], data['StockCode'])

        # Checking if the target customer id not present in the user item matrix
        if target_customer_id not in user_item_matrix.index:
            raise ValueError(f"Customer ID {target_customer_id} not found")

        # Similarity Calculation using cosine similarity
        similarity_matrix = cosine_similarity(user_item_matrix)

        # Nearest Neighbours
        target_customer_index = user_item_matrix.index.get_loc(target_customer_id)
        target_customer_similarities = similarity_matrix[target_customer_index]
        nearest_neighbors_indices = target_customer_similarities.argsort()[::-1][1:]  # Exclude the target customer itself

        # Recommendation Generated based on neighbour's purchases
        recommendations = []
        for neighbor_index in nearest_neighbors_indices:
            neighbor_id = user_item_matrix.index[neighbor_index]
            neighbor_items = user_item_matrix.iloc[neighbor_index]
            target_customer_items = user_item_matrix.iloc[target_customer_index]
            items_to_recommend = neighbor_items[neighbor_items == 1].index.difference(
                target_customer_items[target_customer_items == 1].index)
            recommendations.extend(items_to_recommend)

        recommended_items = pd.Series(recommendations).value_counts().head(10)

        # Converting recommendations to dictionary format
        recommendations_dict = {}
        count = 1
        for stock_code in recommended_items.index:
            description = data.loc[data['StockCode'] == stock_code, 'Description'].iloc[0]
            recommendations_dict[count] = {
                'StockCode': stock_code,
                'Description': description
            }
            count += 1
        return recommendations_dict

    except Exception as e:
        # Handling the exception and return an error message
        error_message = str(e)
        error_dict = {'error': error_message}
        return error_dict
