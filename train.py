from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()
    model = YOLO("yolo11n.pt")

    result = model.train(data='data.yaml', epochs = 1, imgsz = 640)