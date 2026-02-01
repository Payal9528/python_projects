
import numpy as np
import pandas as pd

# number of users (BIG DATA like facebook)
n = 1_000_000
data = {
    "user_id": np.arange(1, n+1),
    "age": np.random.randint(13, 65, size=n),
    "country": np.random.choice(
        ["india", "USA", "UK", "Canada", "Germany"], size=n
    ),
    "device": np.random.choice(
        ["Android", "IOS", "Web"], size=n
    ),
    "time_spend_min": np.random.exponential(scale=60, size=n),
    "likes": np.random.poisson(lam=20, size=n),
    "ads_clicked": np.random.binomial(n=10, p=0.05, size=n),
    "revenue": np.random.exponential(scale=2, size=n)
}

df = pd.DataFrame(data)

print(df.head())
print(df.shape)

# type optimisation
df["age"] = df["age"].astype("int8")
df["likes"] = df["likes"].astype("int16")
df["ads_clicked"] = df["ads_clicked"].astype("int8")
df["country"] = df["country"].astype("category")
df["device"] = df["device"].astype("category")

print(df.info())

# average time spent per device
device_time = df.groupby("device")["time_spend_min"].mean()
print(device_time)

# revenue by country
country_revenue = df.groupby("country")["revenue"].sum()
print(country_revenue)

# High value users (fix column name)
high_value_users = df[
    (df["time_spend_min"] > 120) &
    (df["ads_clicked"] >= 3)
]
print(high_value_users)

# Fast filtering data
india_android_users = df.query(
    "country == 'india' and device == 'Android'"
)
print(india_android_users)

# Save file first before reading in chunks
df.to_csv("social_media_data.csv", index=False)

for chunk in pd.read_csv("social_media_data.csv", chunksize=20000):
    print(chunk.groupby("country")["revenue"].sum())


    file_path = "BigData.csv"
    data.to_csv(file_path , index = False)