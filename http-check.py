import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

def check_url(url):
    try:
        with urlopen(url, timeout=10) as response:
            print(f"{url} -> HTTP {response.status}")
        return 0
    except HTTPError as error:
        print(f"{url} -> HTTP error: {error.code}")
    except TimeoutError as error:
        print(f"{url} -> Timeout: {error}")
    except URLError as error:
        print(f"{url} -> Network error: {error.reason}")

    return 1

urls = sys.argv[1:]

if not urls:
    print(f"Usage: {sys.argv[0]} URL [URL ...]")
    raise SystemExit(2)

exit_code = 0

for url in urls:
    if check_url(url) != 0:
        exit_code = 1

raise SystemExit(exit_code)
