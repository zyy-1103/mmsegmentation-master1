from PIL import Image
import cv2
import os  # 读取系统的内照片
def change_pixel(img):
    width = img.shape[0]  # 长度
    height = img.shape[1]  # 宽度
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            if (img[i, j] == 128):
                img[i, j] = 1
            elif (img[i, j] == 255):
                img[i, j] = 2
            else:
                img[i, j] = 0
    return img
if __name__ =="__main__":
    filePath = '/Users/qdd/Desktop/mmsegmentation-master/Mydataset1/ann_dir/val/'
    savePath = '/Users/qdd/Desktop/mmsegmentation-master/Mydataset/ann_dir/val/'
    name = os.listdir(filePath)
    print(name)
    for i in name:
        image_path = os.path.join(filePath,i)
        image_save_Path = os.path.join(savePath,i)
        image = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
        img = change_pixel(image)
        cv2.imwrite(image_save_Path, img)
