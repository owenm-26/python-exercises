import requests

def get_api_request(url: str):
    try:
        response = requests.get(url)
        return response.text
        
    except:
        print(f"ERROR: failed to fetch from {url}")


if __name__ == "__main__":
    str1: str = "abcdef"
    api_url: str = "http://127.0.0.1:5000/fruits"

    response_txt = get_api_request(api_url)
    print(response_txt)