import os
import shutil
import random

def copy_dataset_with_random_number(dataset_dir: str, target_dir: str):
    """
    Копирует датасет с случайными номерами файлов.

    Args:
        dataset_dir (str): Абсолютный путь к исходному датасету.
        target_dir (str): Абсолютный путь к целевой папке, куда будут скопированы файлы.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for class_label in os.listdir(dataset_dir):
        if os.path.splitext(class_label)[1] in [".csv", ".txt"]:
            continue
        for filename in os.listdir(os.path.join(dataset_dir, class_label)):
            if os.path.splitext(filename)[1] != ".txt":
                continue
            
            src_file = os.path.join(dataset_dir, class_label, filename)

            random_number = random.randint(0, 10000)
            new_filename = f"{class_label}_{random_number:04}.txt"
            dst_file = os.path.join(target_dir, new_filename)

            shutil.copy2(src_file, dst_file)
