import os
import csv

def create_annotation_file(dataset_path: str, annotation_file_path: str):
    """
    Создает CSV-файл с аннотациями для датасета.

    Args:
        dataset_path (str): Абсолютный путь к датасету.
        annotation_file_path (str): Абсолютный путь к файлу аннотаций.
    """
    with open(annotation_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['absolute path', 'relative path', 'class label'])

        for root, _, files in os.walk(dataset_path):
            for file in files:
                if file.endswith(".txt"):
                    absolute_path = os.path.join(root, file)
                    relative_path = os.path.relpath(absolute_path, dataset_path)
                    class_label = file.split('_')[0]
                    writer.writerow([absolute_path, relative_path, class_label])
