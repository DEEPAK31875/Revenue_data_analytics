from sqlalchemy import create_engine
import pandas as pd

# Step 1: Define the database connection parameters
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
HOST = 'localhost'  # Use your MySQL server's host
USER = 'root'   # Replace with your MySQL username
PASSWORD = '$29#Dr%40p'  # Replace with your MySQL password
DATABASE = 'revenue_db'  # Replace with your MySQL database name
PORT = 3306  # MySQL's default port is 3306

# Step 2: Create the database connection string
connection_string = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Step 3: Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Step 4: Load the cleaned dataset
cleaned_file_path = "C:/Users/Dell/Desktop/cleaned_revenue_data.csv"  # Path to your cleaned data file
df = pd.read_csv(cleaned_file_path)

# Step 5: Write the DataFrame to the MySQL table
table_name = 'revenue_data'

# Check for existing table handling
try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data successfully uploaded to the '{table_name}' table in the '{DATABASE}' database.")
except Exception as e:
    print(f"An error occurred: {e}")