
def main():
    try:
        while 1:
            command_line = input("task-tracker->")
            print(command_line)
    except KeyboardInterrupt:
        print("\nExiting....")
    except EOFError:
        print("\nExiting....")

if __name__ == "__main__":
    main()