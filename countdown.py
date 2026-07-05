import time

t = int(input("Enter the countdown time in seconds: "))

for x in range(t, 0, -1):
    hours = x // 3600
    minutes = (x % 3600) // 60
    seconds = x % 60

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
