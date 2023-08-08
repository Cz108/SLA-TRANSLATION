import os

def open_docx_files_in_directory(root_dir):
    file_path_list = []
    file_name_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".docx"):
                file_path = os.path.join(dirpath, file)
                print(f"Opening {file_path}")
                print(f"Filenames {file}")
                file_path_list.append(file_path)
                file_name_list.append(file)
    return file_path_list, file_name_list


if __name__ == "__main__":
    # Set the directory you want to start from here:
    root_directory = "/Users/bilibala/Documents/Tmp/bg&hr&el&sr"
    file_path_list, file_name_list = open_docx_files_in_directory(root_directory)
