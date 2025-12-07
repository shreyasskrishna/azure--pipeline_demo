from datetime import datetime

if __name__ == "__main__":
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Hello, Azure Pipeline!")
