from file_system import find_file_directory_by_path, find_directory_by_path
from config import ROOT


def see_file_content(path=None):
    if not isinstance(path, str):
        print('Input correct path')
        exit()
    file_name = path.split('/')[-1]
    file_directory = find_file_directory_by_path(path, ROOT)
    if file_directory:
        print(file_directory.read_file(file_name))
    else:
        print('File not found')


def delete_file(path=None):
    if not isinstance(path, str):
        print('Input correct path')
        exit()
    file_name = path.split('/')[-1]
    file_directory = find_file_directory_by_path(path, ROOT)
    if file_directory:
        print(file_directory.delete_file(file_name))
    else:
        print('File not found')


def update_file(path=None, content=None):
    if not isinstance(path, str):
        print('Input correct path')
        exit()
    if not isinstance(content, str):
        print('Input correct content')
        exit()
    file_name = path.split('/')[-1]
    file_directory = find_file_directory_by_path(path, ROOT)
    if file_directory:
        print(file_directory.update_file(file_name, content))
    else:
        print('File not found')


def show_directory_contents(path=None):
    directory = find_directory_by_path(path, ROOT) if path else ROOT
    if directory is not None:
        for subdir in directory.get_list_directories():
            print(subdir)
        for file in directory.get_list_files():
            print(file)
    else:
        print('Directory not found')