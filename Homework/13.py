# input an integer number of seconds and print is as HH:MM:SS (Zero-padded).
seconds = int(input("Enter total seconds: "))

print(f"{seconds//3600:02.0f}:{seconds%3600//60:02.0f}:{(seconds%3600)%60:02.0f}")
