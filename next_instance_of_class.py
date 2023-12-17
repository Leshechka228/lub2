import os

def next_instance_of_class(class_label: str, dataset_path: str, visited_instances: set = set()) -> str:
    """
    Находит следующий экземпляр класса в директории с набором данных.
    
    Аргументы:
        class_label (str): Метка класса, которую требуется найти.
        dataset_path (str): Путь к директории с набором данных для поиска.
        visited_instances (set, опционально): Множество для отслеживания посещенных экземпляров. 
                                              По умолчанию пустое множество.

    Возвращает:
        str: Путь к следующему экземпляру указанного класса, либо None, если экземпляры больше не найдены.
    """
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                instance_class = file[:-9]
                if instance_class == class_label and file_path not in visited_instances:
                    visited_instances.add(file_path)
                    return file_path
    return None