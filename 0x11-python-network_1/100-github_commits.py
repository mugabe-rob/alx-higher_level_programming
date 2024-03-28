#!/usr/bin/python3
"""To show the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    commits = get(url).json()
    try:
        for counter in range(10):
            print("{}: {}".format(
                commits[counter].get("sha"),
                commits[counter].get("commit").get("author").get("name")))
    except IndexError:
        pass
