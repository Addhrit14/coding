while True:
    command = input("type a command, or -1 to quit:").strip()
    if command == "-1":
        break
    print("command received:",command)
print("session ended")