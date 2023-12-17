import os
import shutil

def copy_dataset_with_class_names(dataset_dir: str, target_dir: str, class_labels: list):
    """
    Копирует датасет с классовыми названиями.

    Args:
        dataset_dir (str): Абсолютный путь к исходному датасету.
        target_dir (str): Абсолютный путь к целевой директории для копии датасета.
        class_labels (list): Список классовых названий.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for class_label in class_labels:
        for index, filename in enumerate(os.listdir(os.path.join(dataset_dir, class_label))):
            if os.path.splitext(filename)[1] != ".txt":
                continue
            src_file = os.path.join(dataset_dir, class_label, filename)
            new_filename = f'{class_label}_{index:04}{os.path.splitext(filename)[1]}'
            dst_file = os.path.join(target_dir, new_filename)
            shutil.copyfile(src_file, dst_file)