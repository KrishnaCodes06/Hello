try:
    name = input("Enter your name: ")
    if not name.strip():
        raise ValueError("Name cannot be empty")
    print(greet(name))
except ValueError as e:
    print("Error:", e)
