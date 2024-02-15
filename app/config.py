from file_system import SimpleFileSystem

ROOT = SimpleFileSystem()


def create_dummy_data():
    ROOT.create_directory("dir1")
    ROOT.create_directory("dir2")
    ROOT.create_file("text.txt", 'hi')

    dir1 = ROOT.get_directory("dir1")
    dir2 = ROOT.get_directory("dir2")

    dir1.create_file('dir1.txt', 'Hello, dir1!')
    dir1.create_directory('dir3')
    dir2.create_file('dir2.txt', 'Hello, dir2!')
    dir3 = dir1.get_directory('dir3')
    dir3.create_file('dir3.txt', 'Hello, dir3!')

create_dummy_data()
