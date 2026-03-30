## Goal

#Write `clean.py` that:

#1. Loads `listings.csv.gz` with only your selected columns.
#2. Prints the dtypes and a sample before cleaning (so you can see the mess).
#3. Converts `price` to a numeric float.
#4. Handles nulls in every column — drop, fill, or justify ignoring. Print your null counts after.
#5. Fixes any other dtype issues you spot (strings that should be numbers, etc.).
#6. Prints a final `df.info()` and `df.describe()` showing a clean, typed DataFrame.

#Document your decisions as comments — "dropped nulls because X", "filled with median because Y".

import pandas as pd

#cols choosen in last milestone
cols = [
    "neighbourhood_group_cleansed", "host_location", "host_verifications", "neighbourhood_cleansed", "latitude",
    "longitude", "property_type", "room_type", "price",
    "minimum_nights", "maximum_nights", "number_of_reviews",
    "estimated_revenue_l365d", "review_scores_rating",
    "name",  "bathrooms", "beds", "review_scores_accuracy", "review_scores_cleanliness", "review_scores_value"
]

df = pd.read_csv("./data-wrangling/listings.csv.gz", usecols=cols)

print("dytpes: ", df.dtypes)


print("before: ", df.shape[0])
#decisions

#col search deletions
#deleting neighborhood_overview. too many nulls, not that important
#same with host_neigbourhood
#need a better one to see where i stay
# neighbourhood_group_cleansed! adda

# row deletions
#
# price - i need to know how much it costs. sadly count find another col that i could take in its palce
# host verifications - i dont want to sleep somewhere unverified
# has_availability - dont know? dont care, cya
# reviews_x. if one is null, all are null almost all the time.
df = df.dropna(subset=["price", "host_verifications", "review_scores_rating", "review_scores_accuracy", "review_scores_cleanliness", "review_scores_value"])


# nulls stay
# host_location is nice to have, but idc. nulls are fine
# estimated_revenue - not that important, just curious
# beds & bathrooms... its sadly like 3k more rows and id liketo know if im sleeping in a bed or a couch .. but on the other hand, ill be filtering for room_type "entire home/apt".. im just trusting they all got a bed and a toilet
print(df.isnull().sum())
print("after: ", df.shape[0])

df["price"] = df["price"].str.replace("$", "").str.replace(",", "").astype(float)

print("info")
df.info()
print("info")
print("describe", df.describe())
