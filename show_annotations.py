# import keras_retinanet drawing
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

# import miscellaneous modules
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# load label to names mapping for visualization purposes
labels_to_names = {0: 'band', 1: 'big pulley', 2: 'motor', 3: 'big bearing', 4: 'small pulley', 5: 'small bearing',
                   6: 'rod', 7: 'screw', 8: 'big washer', 9: 'cap', 10: 'small washer', 11: 'nut'}

scene = "20_9"

img = cv2.imread("dataset/{}.png".format(scene), cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for obj_id in range(12):
    a_path = Path("annotations") / "{}_{}".format(scene, obj_id)
    if not a_path.exists():
        print(a_path)
        continue
    anno = open(a_path).readline()
    bbox = [int(v) for v in anno.split(",")]
    caption = labels_to_names[obj_id]
    color = label_color(obj_id)
    draw_box(img, bbox, color=color)
    draw_caption(img, bbox, caption)

plt.imshow(img)
plt.show()
