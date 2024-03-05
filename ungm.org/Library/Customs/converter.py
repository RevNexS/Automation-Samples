import sqlite3
import pandas as pd


class DB_Converter:

    @staticmethod
    def to_csv():
        # Connect to the SQLite database
        conn = sqlite3.connect('./Database/Masterdb_AMSFinal.db')

        # Query the data from the table
        query = "SELECT * FROM tblTenders"
        # Convert the data to a pandas DataFrame
        df = pd.read_sql_query(query, conn)

        # Write the DataFrame to a CSV file
        df.to_csv('./Output/output.csv',mode='a', header=False, index=False)
        df.to_csv('./output.csv', mode='a', header=False, index=False)

        # Close the connection
        conn.close()

