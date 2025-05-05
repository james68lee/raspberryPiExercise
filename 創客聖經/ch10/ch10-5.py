from ultralytics import YOLO

# 載入物體偵測模型
model = YOLO('yolo11n.pt')
# 轉換成NCNN格式的模型
model.export(format="ncnn")  # 'yolo11n_ncnn_model'

# 載入影像分割模型
model = YOLO('yolo11n-seg.pt')
# 轉換成NCNN格式的模型
model.export(format="ncnn")  # 'yolo11n-seg_ncnn_model'

# 載入姿態評估與追蹤模型
model = YOLO('yolo11n-pose.pt')
# 轉換成NCNN格式的模型
model.export(format="ncnn")  # 'yolo11n-pose_ncnn_model'
