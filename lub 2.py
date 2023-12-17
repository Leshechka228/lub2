import os
from create_annotation_file import create_annotation_file
from copy_dataset_with_class_names import copy_dataset_with_class_names
from copy_dataset_with_random_number import copy_dataset_with_random_number
from next_instance_of_class import next_instance_of_class
from ClassIterator import ClassIterator

if __name__ == "__main__":
    class_labels = ['good', 'bad']
    home = os.path.expanduser('~')
    home_path = os.path.join(home, "Desktop")
    
    dataset_dir = os.path.join(home_path, "dataset")
    target_dir = os.path.join(home_path, "dataset\\annotation.csv")
    create_annotation_file(dataset_dir, target_dir)

    dataset_dir = os.path.join(home_path, "dataset")
    target_dir = os.path.join(home_path, "copy dataset")
    copy_dataset_with_class_names(dataset_dir, target_dir, class_labels)

    dataset_dir = os.path.join(home_path, "copy dataset")
    target_dir = os.path.join(home_path, "copy dataset\\annotation.csv")
    create_annotation_file(dataset_dir, target_dir)

    dataset_dir = os.path.join(home_path, "dataset")
    target_dir = os.path.join(home_path, "random")
    copy_dataset_with_random_number(dataset_dir, target_dir)

    dataset_dir = os.path.join(home_path, "random")
    target_dir = os.path.join(home_path, "random\\annotation.csv")
    create_annotation_file(dataset_dir, target_dir)

    dataset_path = os.path.join(home_path, "random")
    class_label = 'good'

    next_instance = next_instance_of_class(class_label, dataset_path)
    if next_instance:
        print(f"Следующий экземпляр класса '{class_label}': {next_instance}")
    else:
        print(f"Экземпляры класса '{class_label}' закончились")
    
    class_instance_iterator = ClassIterator(class_label, dataset_path)
    for instance in class_instance_iterator:
        print(f"Следующий экземпляр класса '{class_label}': {instance}")
    else:
        print(f"Экземпляры класса '{class_label}' закончились")