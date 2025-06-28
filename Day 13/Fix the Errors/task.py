while True:
    try:
        age = int(input("How old are you?"))
        break
    except ValueError:
        print("Invalid input")

if age > 18:
    print(f"You can drive at age {age}.")
print("done")