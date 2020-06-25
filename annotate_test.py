import matplotlib.pyplot as plt
from skimage.draw import line_aa, circle
import os

a = "22_9_1"


def main():
    img = plt.imread("dataset/{}_{}.png".format(*a.split('_')[:2]))
    with open("annotations/" + a) as f:
        xmin, ymin, xmax, ymax = map(int, f.readline().split(','))
    angle_annotation = "annotations/" + a + "_a"

    img[:, :, 3] = 0.3
    img[ymin:ymax, xmin:xmax, 3] = 1

    if os.path.exists(angle_annotation):
        with open("annotations/" + a + "_a") as f:
            x0, y0, x1, y1 = map(int, f.readline().split(','))
            xx, yy, val = line_aa(x0, y0, x1, y1)
            val = val.reshape(-1, 1)
            img[yy, xx, :3] = val * (1, 0, 0) + (1 - val) * img[yy, xx, :3]
            xx, yy = circle(x1, y1, 5)
            img[yy, xx, :3] = (1, 0, 0)

    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
