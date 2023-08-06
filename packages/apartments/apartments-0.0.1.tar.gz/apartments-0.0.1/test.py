from apartments import URL

kwargs = {
    "bathrooms": 2,
    "min_price": 1100,
    "max_price": 2200,
    "type": "townhomes",
    "lifestyle": "short-term",
    "move_in_date": "09/01/2021",
    "amenities": ["pool", "yard", "pet-friendly-dog"],
}

x = URL("san jose", "ca", filters=kwargs)
print(x.url(new=True))
x = URL("san jose", "ca", filters={"bathrooms": 2}, min_price=1100, ratings=["2", 3], query="house")
print(x.url(new=True))
x = URL("san jose", "ca", affordability="low-income")
print(x.url(new=False))
