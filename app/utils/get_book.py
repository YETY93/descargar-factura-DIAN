import os


def list_dir_path():
    PATH_CURRENT:str = os.path.abspath(os.getcwd())
    path_data: str = PATH_CURRENT + r"\data"
    list_files_path: list = os.listdir(path_data)
    list_documents: list = []
    for file in list_files_path:
        if os.path.isfile(os.path.join(path_data, file)) and file.endswith('.xlsx'):
            document_path = path_data + "\\" + file
            list_documents.append(document_path)

    return list_documents

