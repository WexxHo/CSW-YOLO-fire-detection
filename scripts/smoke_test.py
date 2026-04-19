from ultralytics import YOLO

model = YOLO('yolo11n.pt')
results = model('https://ultralytics.com/images/bus.jpg')

for r in results:
    print('检测到的对象数量:', len(r.boxes))
    print('各对象的类别:', r.boxes.cls.tolist() if r.boxes is not None else '无')
    print('各对象的置信度:', r.boxes.conf.tolist() if r.boxes is not None else '无')