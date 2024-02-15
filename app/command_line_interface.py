from command_line_helper import see_file_content, show_directory_contents, delete_file, update_file

COMMANDS = {
    'cat': see_file_content,
    'ls': show_directory_contents,
    'rm': delete_file,
    'ed': update_file

}


def command_line(user_input: str) -> None:
    user_command, *args = user_input.split()
    command = COMMANDS.get(user_command)
    if command is None:
        raise KeyError(f'Command not found: {command}')

    print(command(*args))


if __name__ == '__main__':
    while True:
        command = input()
        if command == 'exit':
            break
        command_line(command)

