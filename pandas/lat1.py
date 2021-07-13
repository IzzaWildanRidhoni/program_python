import pandas as pd
url = "https://raw.githubusercontent.com/muhash006/data1/main/data.csv"
df = pd.read_csv(url)

print(df.to_string())
print(df.info())

print('-----------------------')
# hapus semua baris dengan nilai null
    # df.dropna(inplace =  True)
    # print(df.to_string())
    # print(df.info())

# menangani seluruh sel kosong dengan memasukkan nilai baru
df.fillna(130,inplace=True)
print(df.to_string())
print(df.info())

