import pandas as pd
import sqlite3
from io import StringIO
import requests

# List of CSV URLs
csv_urls = [
    "https://example.com/path/to/your/file1.csv",
    "https://example.com/path/to/your/file2.csv",
    # Add more CSV URLs as needed
]

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('your_database.db')

for csv_url in csv_urls:
    # Make a request to get the content of the CSV file
    response = requests.get(csv_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Read the CSV content into a Pandas DataFrame
        csv_content = response.text
        df = pd.read_csv(StringIO(csv_content))

        # Use Pandas to write the DataFrame to the SQLite database
        df.to_sql('your_table_name', conn, index=False, if_exists='append')

        print(f"Data from {csv_url} successfully loaded into SQLite database.")

    else:
        print(f"Failed to retrieve CSV file {csv_url}. Status code: {response.status_code}")

# Commit changes and close the database connection
conn.commit()
conn.close()
