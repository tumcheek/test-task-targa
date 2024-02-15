from typing import List
from datetime import datetime


class MetaDataMixin:
    def __init__(self):
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        self.__size = 0

    def update_timestamp(self):
        self.__updated_at = datetime.now()

    def get_size(self):
        return self.__size

    def update_size(self, size):
        self.__size = size

    def get_meta_data(self):
        return {
            'size': self.__size,
            'created_at': self.__created_at,
            'updated_at': self.__updated_at
        }


class File(MetaDataMixin):
    def __init__(self, name, content):
        self.name = name
        self.content = content
        super().__init__()
        self.update_size(len(self.content))

    def update_file(self, content):
        self.content = content
        self.update_timestamp()
        self.update_size(len(self.content))


class FileOperationMixin:
    def __init__(self):
        self.files = {}

    def create_file(self, name: str, content: str) -> None:
        if self.files.get(name):
            raise KeyError(f'File already exists: {name}')
        self.files[name] = File(name, content)

    def read_file(self, name: str) -> str:
        file = self.files.get(name, None)
        if file is None:
            raise KeyError(f'File not found: {name}')
        return self.files[name].content

    def update_file(self, name: str, content: str) -> None:
        file = self.files.get(name, None)
        if file is None:
            raise KeyError(f'File not found: {name}')
        self.files[name].update_file(content)

    def delete_file(self, name) -> None:
        file = self.files.get(name, None)
        if file is None:
            raise KeyError(f'File not found: {name}')
        del self.files[name]

    def get_list_files(self) -> List[str]:
        return list(self.files.keys())


class Directory(FileOperationMixin, MetaDataMixin):
    def __init__(self, name: str):
        self.name = name
        self.directories = {}
        super().__init__()
        MetaDataMixin.__init__(self)

    def get_list_directories(self) -> List[str]:
        return list(self.directories.keys())

    def create_directory(self, name: str):
        directory = self.directories.get(name, None)
        if directory:
            raise KeyError(f'Directory already exists: {name}')
        self.directories[name] = Directory(name)
        self.update_size(len(self.directories.keys()) + len(self.files))

    def remove_directory(self, name: str):
        directory = self.directories.get(name, None)
        if directory is None:
            raise KeyError(f'Directory not found: {name}')
        del self.directories[name]

    def get_directory(self, name: str):
        directory = self.directories.get(name, None)
        if directory is None:
            raise KeyError(f'Directory not found: {name}')
        return directory


class SimpleFileSystem(Directory):
    def __init__(self, name='root'):
        super().__init__(name)

    @staticmethod
    def tree(dir: Directory, level=0) -> None:
        files = dir.files.keys()
        sub_dirs = dir.directories.keys()
        print(' ' * level, dir.name)
        if len(files) > 0:
            for file in files:
                print(' ' * (level+2), file)
        if len(sub_dirs) > 0:
            for sub_dir in sub_dirs:
                SimpleFileSystem.tree(dir.directories[sub_dir], level + 2)
