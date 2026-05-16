import pandas as pd

# EXTRACT
def extract_data(file_path):
    df = pd.read_csv(file_path)
    print("Data Extracted")
    return df

# TRANSFORM
def transform_data(df):
    df['total_sales'] = df['sales'] * df['price']
    df['date'] = pd.to_datetime(df['date'])

    df = df.dropna()

    print("Data Transformed")
    return df

# LOAD
def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print("Data Loaded Successfully!")

if __name__ == "__main__":
    input_path = "data/sales_data.csv"
    output_path = "data/processed_sales.csv"

    df = extract_data(input_path)
    df = transform_data(df)
    load_data(df, output_path)

    print("\nFINAL DATA:")
    print(df.head())