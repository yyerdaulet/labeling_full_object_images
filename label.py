import os
import sys

image_file = sys.argv[1]
label_file = sys.argv[2]
processes = ["train","val","test"]


def create_dir():
    for process in processes:
        os.makedirs(os.path.join(label_file,process),exist_ok=True)

def collect_class_names() -> list:
    classes = []
    for class_name in os.listdir(os.path.join(image_file,'train')):
       if class_name == ".DS_Store":
           continue
       classes.append(class_name)
    return classes

def create_annotations(classes:list):
    for process in processes:
        for class_idx,class_name in enumerate(classes):
            current_file = os.path.join(image_file,f"{process}/{class_name}")
            for file_name in os.listdir(current_file):
                file_name,ext = os.path.splitext(file_name)
                new_name = f"{file_name}_{class_name}"
                os.rename(os.path.join(current_file,f"{file_name}{ext}"),os.path.join(current_file,f"{new_name}{ext}"))
                with open(f"{label_file}/{process}/{new_name}.txt",'w') as file:
                    file.write(f"{class_idx} 0.5 0.5 1.0 1.0")

def main():
    create_dir()
    classes = collect_class_names()
    create_annotations(classes)

if __name__ == "__main__":
    main()
