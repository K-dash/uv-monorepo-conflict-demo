import requests
from common.hoge import hoge

def main():
    print("Hello from repo-a!")
    hoge()
    requests.get("https://example.com")


if __name__ == "__main__":
    main()
