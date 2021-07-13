import pandas as pd
url="https://raw.githubusercontent.com/muhash006/data1/main/data.csv"
df = pd.read_csv(url)

print(df.to_string())