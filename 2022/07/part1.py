class Directory:
    def __init__(self, path, parent, subdirectories, size) -> None:
        self.path = path
        self.parent = parent
        self.subdirectories = subdirectories
        self.size = size

    def calculate_size(self):
        self.total_size = self.size
        self.total_size += (
            sum(subdir.calculate_size() for subdir in self.subdirectories)
            if self.subdirectories
            else 0
        )

        return self.total_size


def main():
    with open("input.txt") as f:
        commands = [command.strip().split("\n") for command in f.read().split("$ ")][2:]

    last_dir = Directory("~", None, [], 0)
    directories = {last_dir.path: last_dir}

    for command in commands:
        if len(command) == 1:  # cd command
            if ".." in command[0]:
                last_dir = last_dir.parent
                continue

            new_dir_name = last_dir.path + "/" + command[0].split()[1]
            new_dir = directories[new_dir_name]
            last_dir = new_dir

        else:
            for sub in command[1:]:
                arg0, arg1 = sub.split()
                if arg0 == "dir":
                    new_dir_name = last_dir.path + "/" + arg1
                    if not new_dir_name in directories:
                        new_dir = Directory(last_dir.path + "/" + arg1, last_dir, [], 0)
                        directories[new_dir.path] = new_dir
                        last_dir.subdirectories.append(new_dir)
                else:
                    size = int(arg0)
                    last_dir.size += size

    for directory in directories.values():
        directory.calculate_size()
        # print(directory.path, directory.total_size)
    print(
        sum(
            directory.total_size
            for directory in directories.values()
            if directory.total_size < 100_000
        )
    )


if __name__ == "__main__":
    main()
