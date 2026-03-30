# goals 

#1. Downloads or loads `listings.csv` (the detailed version from Inside Airbnb Berlin).
#2. Prints: row count, column count, dtypes.
#3. Prints: null counts for each column (only columns that have nulls).
#4. Selects a working subset of ~10-15 columns relevant to pricing analysis and prints their names.
#5. Prints `value_counts()` for `room_type` and `neighbourhood_cleansed`.

import pandas as pd

df = pd.read_csv("./data-wrangling/listings.csv.gz")

print("shape: " , df.shape)
print("head: " , df.head())

print("rowcount: ", df.shape[0])
print("columncount: ", df.shape[1])
print("dtypes: " , df.dtypes)

nullcount = df.isnull().sum()

columns_with_null = nullcount[nullcount>0]

print("columns_with_null: ", columns_with_null)

cols = [
    "neighborhood_overview", "host_location", "host_neighbourhood",
    "host_verifications", "neighbourhood_cleansed", "latitude",
    "longitude", "property_type", "room_type", "price",
    "minimum_nights", "maximum_nights", "number_of_reviews",
    "estimated_revenue_l365d", "review_scores_rating",
]


"name", "neighbourhood_grpuped_cleansed", "bathrooms", "bedrooms", "has_availablity", "review_scores_accuracy", "review_scores_cleanliness", "review_scores_value", 
print(cols)

print("room_type.value_counts: ", df["room_type"].value_counts())
print("room_type.neighbourhood_cleansed: ", df["neighbourhood_cleansed"].value_counts())
print("columns.tolist: " , df.columns.tolist())