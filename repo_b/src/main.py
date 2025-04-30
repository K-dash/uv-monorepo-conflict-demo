from common.hoge import hoge
import requests

def main():
    print("Hello from repo-b!")
    hoge()
    requests.get("https://example.com")


if __name__ == "__main__":
    main()
