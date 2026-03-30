import urllib.request


airbnb_dataset = "https://data.insideairbnb.com/germany/be/berlin/2025-09-23/data/listings.csv.gz"

urllib.request.urlretrieve(airbnb_dataset, "dataset.csv.gz")
