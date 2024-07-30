import re


def normalize_path(path):
    # Replace multiple slashes with a single slash
    path = re.sub(r"/+", "/", path)
    return path


def is_valid_directory_name(name):
    # Check if the directory name contains only alphanumeric characters or valid special cases ('.' and '..')
    if name == "." or name == "..":
        return True
    return name.isalnum()


def construct_new_path(current_path, new_path):
    # Normalize both paths
    current_path = normalize_path(current_path)
    new_path = normalize_path(new_path)

    # If new_path is an absolute path
    if new_path.startswith("/"):
        path = new_path.split("/")
    else:
        path = current_path.split("/") + new_path.split("/")

    # Use a stack to process the path
    stack = []
    for part in path:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        elif is_valid_directory_name(part):
            stack.append(part)
        else:
            return f"{new_path}: No such file or directory"

    return "/" + "/".join(stack)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: mycd <current_directory> <new_directory>")
        sys.exit(1)

    current_directory = sys.argv[1]
    new_directory = sys.argv[2]

    result = construct_new_path(current_directory, new_directory)
    print(result)
