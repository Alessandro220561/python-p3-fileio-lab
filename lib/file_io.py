# def write_file(file_name, file_content):
#     file_name = file_name + '.txt'
#     with open(file_name, mode='w', encoding='utf-8') as file:
#         file.write(file_content)


# def append_file(file_name, append_content):
#     file_name = file_name + '.txt'
#     with open(file_name.txt, mode='a', encoding='utf-8') as file:
#         file.append(append_content)


# def read_file(file_name):
#     file_name = file_name + '.txt'
#     open(file_name.txt, encoding='utf-8')
#     file_name.read()

from pathlib import Path  # Import the pathlib module


def write_file(file_name, file_content):
    if isinstance(file_name, Path):
        file_name = str(file_name)  # Convert PosixPath to string
    file_name = file_name + '.txt'  # Add .txt extension to the file_name
    with open(file_name, mode='w', encoding='utf-8') as file:
        file.write(file_content)


def append_file(file_name, file_content):
    if isinstance(file_name, Path):
        file_name = str(file_name)  # Convert PosixPath to string
    file_name = file_name + '.txt'  # Add .txt extension to the file_name
    with open(file_name, mode='a', encoding='utf-8') as file:
        file.write(file_content)


def read_file(file_name):
    if isinstance(file_name, Path):
        file_name = str(file_name)  # Convert PosixPath to string
    file_name = file_name + '.txt'  # Add .txt extension to the file_name
    with open(file_name, encoding='utf-8') as file:
        file_content = file.read()
    return file_content
