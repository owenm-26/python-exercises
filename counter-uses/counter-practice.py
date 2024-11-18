from collections import Counter


if __name__  == "__main__":
    x: str = "Hi there, I am Owen Mariani"
    y = Counter(x)
    
    print('elements', list(y.values()))
    print('keys', list(y.keys()))

    print(f"\n Counter: {list(y.items())}")