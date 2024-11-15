import requests

def get_api_request(path: str):
    ''' Method to get text back from API can if not throws error'''
    try:
        response = requests.get(f"http://127.0.0.1:5000/{path}")
        return response
        
    except:
        print(f"ERROR: failed to fetch from {path}")
        return ConnectionError("Connection not made")

# STRING PRACTICE METHODS
def clean_fruit_response():
    ''' Method that gets a list of weirdly capitalized / sorted fruits and makes them 
        title case and sorts them'''
    try:
        response = get_api_request('fruits')
        print(response.json())

        fruits: list = response.json()

        # properly case the fruits
        for i in range(len(fruits)):
            fruits[i] = fruits[i].title()
        
        # sort alphabetically
        fruits.sort()
        
        return fruits

    except:
        print("ERROR in clean_fruit_response")
        return ConnectionError("Failed")
    
def process_logs(seconds: int):
    try:
        print(f'Running logs for {seconds} seconds...')
        response = get_api_request(f'logs/{seconds}')
        print(response.text)

    except:
        print("ERROR in process_logs")
        return ConnectionError("Failed")

if __name__ == "__main__":
    str1: str = "abcdef"
    api_path: str = "fruits"

    # print(clean_fruit_response())
    print(process_logs(5))
    