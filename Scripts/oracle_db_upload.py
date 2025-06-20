import cx_Oracle
import pandas as pd

# Function to connect to Oracle DB
def connect_to_oracle(user, password, dsn):
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
        print("Successfully connected to Oracle DB")
        return connection
    except cx_Oracle.Error as error:
        print("Error connecting to Oracle DB:", error)
        return None

# Function to upload DataFrame to Oracle DB
def upload_reviews(df, connection):
    cursor = connection.cursor()
    insert_sql = """
    INSERT INTO reviews (review_text, processed_text, sentiment, dominant_theme, review_date)
    VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
    """
    
    for index, row in df.iterrows():
        try:
            cursor.execute(insert_sql, (
                row['review_text'], 
                row.get('processed_text', None), 
                row.get('sentiment', None), 
                row.get('dominant_theme', None), 
                row.get('review_date', None)
            ))
        except cx_Oracle.Error as e:
            print(f"Failed to insert row {index}: {e}")
    
    connection.commit()
    print(f"{len(df)} rows uploaded successfully.")
    cursor.close()

# Main execution
if __name__ == "__main__":
    # Set your credentials and DSN (Data Source Name)
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    DSN = 'host:port/service_name'  # Example: 'localhost:1521/orclpdb1'

    # Connect to Oracle DB
    conn = connect_to_oracle(USERNAME, PASSWORD, DSN)
    if conn:
        # Load your processed reviews data (example CSV)
        df_reviews = pd.read_csv('data/processed_reviews.csv')

        # Upload data to Oracle DB
        upload_reviews(df_reviews, conn)

        # Close connection
        conn.close()
