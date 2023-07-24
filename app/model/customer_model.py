# Importing packages
import pandas as pd
from app.utils.database import connect_to_database, execute_query

class PurchaseHistory:
    @classmethod
    def get_purchase_history(cls):
        # Connect to Database
        connection = connect_to_database()
        # Query to select only the relevant records
        query = """
            SELECT *
            FROM transactions
            WHERE StockCode NOT IN ('S', 'POST', 'CRUK', 'PADS', 'M', 'D', 'DOT', 'C2', 'BANK CHARGES', 'AMAZONFEE')
            AND StockCode NOT LIKE '%gift%'
            AND StockCode NOT LIKE '%DCGS%'
            AND Quantity > 0
            AND CustomerID IS NOT NULL
            AND Description IS NOT NULL
            AND UnitPrice > 0
            AND Country != 'Unspecified'
        """
        # Fetch the data from Database
        data = execute_query(connection, query)
        # Close Connection
        connection.close()
        # Convert the obtained items into DataFrame format
        df = pd.DataFrame(data, columns=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])
        return df
