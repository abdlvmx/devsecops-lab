import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

urls = sys.argv[1:]

if not urls:
    print(f"Usage: {sys.argv[0]} URL [URL ...]")
    raise SystemExit(2)

exit_code = 0

for url in urls:
    try:
        with urlopen(url, timeout=10) as response:
            print(f"{url} -> HTTP {response.status}")
    except HTTPError as error:
        print(f"{url} -> HTTP error: {error.code}")
        exit_code = 1
    except TimeoutError as error:
        print(f"{url} -> Timeout: {error}")
        exit_code = 1
    except URLError as error:
        print(f"{url} -> Network error: {error.reason}")
        exit_code = 1

raise SystemExit(exit_code)
