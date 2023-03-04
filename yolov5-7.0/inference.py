import torch

# Model
model = torch.hub.load('.', 'yolov5s',source='local')  # or yolov5n - yolov5x6, custom

# Images
img = 'D:\PycharmProjects\yolov5-7.0\data\images\zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results.show()