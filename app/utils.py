from fastapi import HTTPException

from config import ROOT
from file_system import Directory
from schemas import DirectoryInfo, FileInfo


def find_file_directory_by_path(path: str, root: Directory) -> str:
    *directories, file_name = path.split('/')
    if directories:
        for directory in directories:
            current_dir = root.get_directory(directory)
            if current_dir:
                root = current_dir

    if file_name in root.files:
        return root
    else:
        return None


def find_directory_by_path(path: str, root: Directory) -> Directory:
    *directories, directory_name = path.split('/')

    if directories:
        for directory in directories:
            current_dir = root.get_directory(directory)
            if current_dir:
                root = current_dir

    if directory_name in root.directories:
        return root.get_directory(directory_name)
    else:
        return None


def get_metadata(directory: Directory) -> list:
    return [directory.name, directory.get_meta_data()]


def get_directory_by_path(path) -> DirectoryInfo:
    directory = find_directory_by_path(path, ROOT)
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    return DirectoryInfo(
        path=path,
        files=list(map(get_metadata, directory.files.values())),
        directories=list(map(get_metadata, directory.directories.values()))
    )


def get_file_by_path(path) -> FileInfo:
    file_name = path.split('/')[-1]
    directory = find_file_directory_by_path(path, ROOT)
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    return FileInfo(path=path, name=file_name,  content=directory.files[file_name].content)


def search_directory(root, dir_name, path=''):
    result = {}
    if dir_name in root.directories:
        result['path'] = path
        result['is_file'] = False
        return result
    elif dir_name in root.files:
        result['path'] = path
        return result

    for name, dir in root.directories.items():
        current_path = f'{path}/{name}' if path else name
        current_result = search_directory(dir, dir_name, current_path)
        if current_result:
            return current_result

    return None

