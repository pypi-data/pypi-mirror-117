"""
Base API for apartments.com
"""

import datefinder

from .keywords import accepted_keywords, path


class URL:
    domain_base = "https://apartments.com/"

    def __init__(self, *args, **kwargs):
        self.path = Path(*args, **kwargs)
        self.params = Param(*args, **kwargs)

    def url(self, new=False):
        """URL constructor. Takes one keyword argument to specify whether to query for
        new posts."""
        if new is not False:
            new = True
        return "".join(
            (
                self.domain_base,
                self.path.get_path(is_new=new),
                self.params.get_params(),
            )
        )


class BaseParser:
    def __init__(self, city="Mountain View", state="CA", filters=None, **kwargs):
        self.city = city
        self.state = state
        self.filters = {} if not filters else filters
        self.filters.update(kwargs)
        self.validate_kwargs()

    def validate_kwargs(self):
        """Validates keyword arguments provided by caller. If not valid, raise
        KeyError."""
        for key in self.filters:
            if key not in accepted_keywords:
                raise KeyError(f"'{key}' is not a valid filter key.")

    def get_tuple_of_filter_values(self, key, typecast=str):
        """Returns a tuple of filter values as typecast datatype (empty or non-empty) from `key`."""
        value = self.filters.get(key, [])
        # User provides attribute datatype other than list.
        if not isinstance(value, (list, tuple)):
            value = list(value)
        return tuple(typecast(v) for v in value)

    @staticmethod
    def validate_attr(attr, attrs, typecast=str):
        """Validate attribute against attributes. Return attribute if validation passes,
        else raise ValueError."""

        def validate_filter_attr(attr_):
            try:
                if typecast(attr_) not in attrs:
                    # TODO: Make custom exception.
                    raise Exception(f"{attr_} is not a valid value for '{attr}'.")
                return attr_
            # Typecast failed.
            except ValueError as e:
                raise ValueError(f"{attr_} is not a valid datatype for '{attr}'.") from e

        if isinstance(attr, (list, tuple)):
            for a in attr:
                validate_filter_attr(a)
        else:
            validate_filter_attr(attr)

    @staticmethod
    def get_nonempty_iter(values):
        """Returns iterable of non-empty values from `values`."""
        return (v for v in values if v)


class Path(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_path(self, is_new):
        """General constructor of a URL path as specified by the caller's query."""
        new_keyword = "new" if is_new is True else ""
        return "/".join(
            self.get_nonempty_iter(
                (
                    self._type,
                    self._location,
                    self._amenities_bathrooms_price,
                    new_keyword,
                    self._amenities_affordability,
                )
            )
        )

    @property
    def _location(self):
        """Location specified in caller query. US city and state are the selectors."""
        return f'{self.city.lower().replace(" ", "-")}-{self.state.lower()}'

    @property
    def _type(self):
        """Type of housing to rent. E.g. 'townhomes'"""
        type_ = self.filters.get("type")
        if not type_:
            return ""
        self.validate_attr(type_, path.type_keys)
        return type_

    @property
    def _amenities_bathrooms_price(self):
        """Combines number of bathrooms and housing price range in one path."""
        attributes = self.get_nonempty_iter(
            (self._bathrooms, self._price, self._amenities(path.amenities_keys_bathrooms_price))
        )
        return "-".join(attributes)

    @property
    def _amenities_affordability(self):
        """"""
        attributes = self.get_nonempty_iter(
            (
                self._affordability,
                self._amenities(path.amenities_keys_affordability),
                self._lifestyle,
            )
        )
        return "-".join(attributes)

    def _amenities(self, keys):
        """Gets amenities from keyword 'amenities' from `self.filters` and returns
        amenity attribute(s) if amenity found in caller provided amenity `keys`."""
        amenities = self.get_tuple_of_filter_values("amenities")
        self.validate_attr(amenities, path.amenities_keys_combined)
        return "-".join(tuple(a for a in amenities if a in keys))

    @property
    def _affordability(self):
        """Affordability of housing. E.g. 'low-income'"""
        affordability = self.filters.get("affordability")
        if not affordability:
            return ""
        self.validate_attr(affordability, path.affordability_keys)
        return affordability

    @property
    def _lifestyle(self):
        """Desired lifestyle and duration of stay. E.g. 'short-term'"""
        lifestyle = self.filters.get("lifestyle")
        if not lifestyle:
            return ""
        self.validate_attr(lifestyle, path.lifestyle_keys)
        return lifestyle

    @property
    def _bathrooms(self):
        """Formats number of bathrooms."""
        # Valid bathrooms keys are 0 - 99
        bathrooms_keys = set(range(100))
        bathrooms = self.filters.get("bathrooms")
        if not bathrooms:
            return ""
        self.validate_attr(bathrooms, bathrooms_keys, typecast=int)
        return f"{bathrooms}-bathrooms"

    @property
    def _price(self):
        """Formats min and max price."""
        min_price = self.filters.get("min_price")
        max_price = self.filters.get("max_price")
        if not min_price and not max_price:
            return ""
        if not min_price:
            return f"under-{max_price}"
        if not max_price:
            return f"over-{min_price}"
        return f"{min_price}-to-{max_price}"


class Param(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_params(self):
        """General constructor of URL parameters as specified by the caller's query."""
        attributes = self.get_nonempty_iter(
            (self._mid, self._min_ft2, self._max_ft2, self._ratings, self._query)
        )
        base = "&".join(attributes)
        return f"?{base}" if base else ""

    @property
    def _mid(self):
        """Desired move-in date."""
        try:
            move_in_dttm_obj = next(datefinder.find_dates(self.filters.get("move_in_date", "")))
            return f"mid={move_in_dttm_obj.strftime('%Y%m%d')}"
        except StopIteration:
            return ""

    @property
    def _min_ft2(self):
        """Desired minimum area (ft2)."""
        return self.filters.get("min_ft2", "")

    @property
    def _max_ft2(self):
        """Desired maximum area (ft2)."""
        return self.filters.get("max_ft2", "")

    @property
    def _ratings(self):
        """Ratings in stars (1-5)."""
        ratings = ",".join(self.get_tuple_of_filter_values("ratings"))
        return f"rt={ratings}" if ratings else ""

    @property
    def _query(self):
        """Any query as provide by caller."""
        query = self.filters.get("query")
        return f"kw={query}" if query else ""
