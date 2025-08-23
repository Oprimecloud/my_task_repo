# check if string starts with "https://"
# Using the "if-else" and "while true" statements.

try:
    user_url = input("Enter a URL: ")
    if user_url.startswith("https://"):
        print("\nHello world")
    else:
        print("Incorrect URL")
except Exception as e:
    print(f"An error occurred: {e}")
