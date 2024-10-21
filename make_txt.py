import os

folder_path = r'/home/usr/PycharmProjects/yolov11_test/datasets/images/train/images'
output_file = "train.txt"

# folder_path = r'/home/usr/PycharmProjects/yolov11_test/datasets/images/valid/images'
# output_file = 'val.txt'

file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

with open(output_file, "w") as f:
    for file_path in file_paths:
        f.write(file_path + "\n")

print(f"file path stored at {output_file} .")