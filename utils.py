import os


def load_data(folder_path: str):
    """
    Load data from txt files in the folder_path
    """
    folder_path = f"data/{folder_path}"
    file_list = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            path = os.path.join(folder_path, file_name)
            print(path)
            if path.endswith('.txt'):
                file = open(path, 'r').read()
                file_list.append(file)
    return file_list