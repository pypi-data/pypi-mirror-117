"""
Module for storing valid keywords
"""

accepted_keywords = {
    # PATHS
    "affordability",  # str
    "amenities",  # list of amenities (str)
    "bathrooms",  # int
    "lifestyle",  # str
    "min_bedrooms",  # int
    "max_bedrooms",  # int
    "min_price",  # int
    "max_price",  # int
    "type",  # str
    # PARAMETERS
    "min_ft2",  # int
    "max_ft2",  # int
    "move_in_date",  # datetime obj --> use datetime inferrer and parse to YYYYMMDD string
    "query",  # str (any query as provided by caller)
    "ratings",  # list of ratings (int, str)
}  # etc...


class path:
    affordability_keys = {
        "low-income",  # Low income housing
        "luxury",  # Luxury housing
        "cheap",  # Cheap housing
    }

    amenities_keys_combined = {
        # Paired with affordability
        "air-conditioning",  # Air conditioning
        "washer-dryer",  # In unit washer & dryer
        "washer_dryer-hookup",  # Washer & dryer hookups
        "dishwasher",  # Dishwasher
        "wheelchair-accessible",  # Wheelchair access
        "parking",  # Parking
        "laundry-facilities",  # Laundry facilities
        "fitness-center",  # Fitness center
        "pool",  # Pool
        "elevator",  # Elevator
        "doorman",  # Doorman
        "furnished",  # Furnished
        "lofts",  # Lofts
        "utilities-included",  # Utilities included
        "gated",  # Gated
        "fireplace",  # Fireplace
        "patio",  # Patio
        "garage",  # Garage
        "hardwood-floors",  # Hardwood floors
        "balcony",  # Balcony
        "office",  # Office
        "living-room",  # Den
        "yard",  # Yard
        "clubhouse",  # Clubhouse
        "business-center",  # Business center
        "controlled-access",  # Controlled access
        "playground",  # Playground
        "basement",  # Basement
        "walk-in-closets",  # Walk-in closets
        "concierge",  # Concierge
        # Paired with bathrooms and price
        "pet-friendly-dog",  # Dog friendly
        "pet-friendly-cat",  # Cat friendly
    }

    amenities_keys_affordability = {
        "air-conditioning",  # Air conditioning
        "washer-dryer",  # In unit washer & dryer
        "washer_dryer-hookup",  # Washer & dryer hookups
        "dishwasher",  # Dishwasher
        "wheelchair-accessible",  # Wheelchair access
        "parking",  # Parking
        "laundry-facilities",  # Laundry facilities
        "fitness-center",  # Fitness center
        "pool",  # Pool
        "elevator",  # Elevator
        "doorman",  # Doorman
        "furnished",  # Furnished
        "lofts",  # Lofts
        "utilities-included",  # Utilities included
        "gated",  # Gated
        "fireplace",  # Fireplace
        "patio",  # Patio
        "garage",  # Garage
        "hardwood-floors",  # Hardwood floors
        "balcony",  # Balcony
        "office",  # Office
        "living-room",  # Den
        "yard",  # Yard
        "clubhouse",  # Clubhouse
        "business-center",  # Business center
        "controlled-access",  # Controlled access
        "playground",  # Playground
        "basement",  # Basement
        "walk-in-closets",  # Walk-in closets
        "concierge",  # Concierge
    }

    amenities_keys_bathrooms_price = {
        "pet-friendly-dog",  # Dog friendly
        "pet-friendly-cat",  # Cat friendly
    }

    lifestyle_keys = {
        "student-housing",  # Student housing
        "senior-housing",  # Senior housing
        "short-term",  # Short-term housing
        # Corporate housing is a parameter. Don't add for now.
    }

    type_keys = {
        "apartments",  # Apartments
        "houses",  # Houses
        "condos",  # Condominiums
        "townhomes",  # Townhomes
    }


# Parameters really don't need a keyword filter. Just about anything gets registered, albeit invalid attributes are ignored.
