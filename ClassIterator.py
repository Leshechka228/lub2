import os

class ClassIterator:
    def __init__(self, class_label, dataset_path):
        self.class_label = class_label
        self.dataset_path = dataset_path
        self.visited_instances = set()
        self.current_instance = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            self.current_instance = self._get_next_instance()
            if self.current_instance is None:
                raise StopIteration
            return self.current_instance
    
    def _get_next_instance(self):
        for root, dirs, files in os.walk(self.dataset_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    instance_class = file[:-9]
                    if instance_class == self.class_label and file_path not in self.visited_instances:
                        self.visited_instances.add(file_path)
                        return file_path
        return None