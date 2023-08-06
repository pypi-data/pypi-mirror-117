import concurrent.futures
import requests


def map_threads(func, _iterable):
    """Map function with iterable object in using thread pools."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(func, _iterable)
    return result


# Must put headers, else request hangs -- also, headers used in pycraigslist.query.sessions DOES NOT work for apartments.com
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
apartments = ["https://apartments.com" for _ in range(1000)]


def get_request(url):
    return requests.get(url, headers=headers)


if __name__ == "__main__":
    list(map_threads(get_request, apartments))
