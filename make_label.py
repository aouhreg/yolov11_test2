import os
import json
from tqdm import tqdm
import argparse

#json_path = r'/home/usr/Desktop/yolo_v11/coco2017/coco2017/annotations/instances_val2017.json'
#label_path = r'/home/usr/Desktop/yolo_v11/datasets/labels/train2017'

# 驗證

# json_path = r'/home/usr/Desktop/yolo_v11/coco2017/coco2017/annotation/instances_val2017.json'
# label_path = r'/home/usr/Desktop/yolo_v11/datasets/labels/val2017'
json_path = r''
label_path = r'/home/usr/Desktop/yolo_v11/datasets/labels/val2017'

parser = argparse.ArgumentParser()
parser.add_argument('--json_path', default=json_path, type=str, help='input: coco format(json)')
parser.add_argument('--save_path', default=label_path ,type=str,  help='specify where to save the output dir of labels')
args = parser.parse_args()

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[2]
    h = box[3]


    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

if __name__ == '__main__':
    json_file= args.json_path # coco object instance type's valid
    ana_txt_save_path = args.save_path # save path

    data = json.load(open(json_file, 'r'))
    if not os.path.exists(ana_txt_save_path):
        os.makedirs(ana_txt_save_path)

    id_map = {}
    for i ,category in enumerate(data['categories']):
        id_map[category['id']] = i

    #pre create table to low time complexity
    max_id = 0
    for img in data['images']:
        max_id = max(max_id, img['id'])

    img_ann_dict = [[] for i in range(max_id+1)]
    for i , ann in enumerate(data['annotations']):
        img_ann_dict[ann['image_id']].append(i)

    for img in tqdm(data['images']):
        filename = img['file_name']
        img_width = img['width']
        img_height = img['height']
        img_id = img['id']
        head, tail = os.path.splitext(filename)
        ana_txt_name = head + ".txt"
        f_txt = open(os.path.join(ana_txt_save_path, ana_txt_name), 'w')
        for ann_id in img_ann_dict[img_id]:
            ann = data['annotations'][ann_id]
            box = convert((img_width, img_height), ann['bbox'])
            f_txt.write("%s %s %s %s %s\n" % (id_map[ann['category_id']], box[0], box[1], box[2], box[3]))
        f_txt.close()