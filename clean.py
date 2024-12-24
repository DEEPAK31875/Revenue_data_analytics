import pandas as pd

# Load the dataset
data_path = r'C:\Users\Bhawesh\Desktop\Revenue Data Analytics\RAW calendar_year_revenue.csv'
data = pd.read_csv(data_path)

# Step 1: Handle missing values
# Separate handling for numerical and non-numerical columns
for col in data.columns:
    if data[col].dtype in ['float64', 'int64']:
        data[col] = data[col].fillna(0)  # Replace NaN in numerical columns with 0
    else:
        data[col] = data[col].fillna('Unknown')  # Replace NaN in non-numerical columns with 'Unknown'

# Step 2: Standardize numerical formats for Revenue
if 'Revenue' in data.columns:
    data['Revenue'] = data['Revenue'].apply(lambda x: round(float(x), 2) if isinstance(x, (int, float, str)) else x)

# Step 3: Create additional columns
# Add a Revenue Category column based on thresholds
def categorize_revenue(value):
    if isinstance(value, (int, float)):
        if value < 0:
            return 'Loss'
        elif 0 <= value < 1000:
            return 'Low'
        elif 1000 <= value < 10000:
            return 'Medium'
        else:
            return 'High'
    return 'Unknown'

if 'Revenue' in data.columns:
    data['Revenue Category'] = data['Revenue'].apply(categorize_revenue)

# Add a Year column (from Calendar Year) for clarity if not already clear
if 'Calendar Year' in data.columns:
    data['Year'] = data['Calendar Year']

# Step 4: Save the cleaned dataset for SQL loading
cleaned_file_path = r'C:\Users\Bhawesh\Desktop\Revenue Data Analytics\cleaned_revenue_data.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Dataset cleaned and saved to {cleaned_file_path}")
