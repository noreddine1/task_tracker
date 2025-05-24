from icecream import ic


def extract_command(line: str):
    index: int = line.find(' ')
    command = line[:index] if index != -1 else line
    rest = line[index+1:] if index != -1 else ""
    return command, rest.strip()
         

def parse_command(line: str):
    line = line.strip()
    command, argument = extract_command(line)
    ic(command, argument)
    return command, argument
