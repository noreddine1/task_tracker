from command_parser import parse_command

def main():
    try:
        while True:
            command_line = input("task-tracker-> ")
            parse_command(command_line)
    except KeyboardInterrupt:
        print("\nExiting....")
    except EOFError:
        print("\nExiting....")

if __name__ == "__main__":
    main()