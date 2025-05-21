from datetime import date

class Task:
    id: int
    descrption: str
    status: str
    create_at: date
    update_at: date
    
    def __init__(name :str):
        pass
        
    

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