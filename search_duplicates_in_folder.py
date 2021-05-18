# -----
# Поиска повторяюшихся файлов в папке
# -----
import os


def read_file(file):
    """чтение файла"""
    with open(file, "rb") as f:
        file_b = f.read()
    return file_b


def search_duplicates_in_folder(dir: str):
    """поиск дубликатов в папке"""
    files = {}
    
    # загрузка данных файлов в словарь {<имя файла>: <содержимое файла>}
    for filename in os.listdir(dir):
        files[filename] = read_file(f"./{dir}/{filename}")

    temp_data_files = [i for i in files.values()]
    
    # удаление не дублирующихся данных
    for i in files.values():
        if temp_data_files.count(i) < 2:
            temp_data_files.pop(temp_data_files.index(i))

    # проверка на наличие дубликатов
    if not temp_data_files:
        print("--== Дубликатов нет ==--")
        exit()

    duplicates = tuple(set(temp_data_files))
    
    # вывод результата
    for duplicate in duplicates:
        print("-" * 20)
        for filename, value in files.items():
            if value == duplicate:
                print(filename)
