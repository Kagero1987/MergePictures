import os
import cv2
import numpy as np



def rename_files(folder_path):
   # 获取文件夹中的所有文件
   image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    # 获取图像文件的名称
   image_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]

   # 遍历文件列表
   for file in image_files:
       # 获取文件名和扩展名
       name, ext = os.path.splitext(file)

       # 计算新的文件名
       new_name = str(0)*(3-len(name)) + name + ext

       # 创建新的文件名
       os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

def get_image_files(folder_path):
    # 获取图像文件的扩展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    # 获取图像文件的名称
    image_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]
    # 根据文件名排序
    image_files.sort()
    return image_files

def merge_images(folder_path, output_path):
    # 重命名文件
    rename_files(folder_path)
    # 获取图像文件
    image_files = get_image_files(folder_path)
    #print(image_files)
    
    # 遍历每张图像
    for image_file in image_files:
        # 输出处理进度
        print("processing "+str(image_files.index(image_file))+" of "+str(len(image_files))+" images")
        if image_file == image_files[0]:
            image = cv2.imread(os.path.join(folder_path, image_file),cv2.IMREAD_GRAYSCALE)
            if image is None:
                print("Image is empty.")
            # 将图像旋转90度
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            # 将图像拼接到merged_image上
            merged_image=image
        
        else:
            image = cv2.imread(os.path.join(folder_path, image_file),cv2.IMREAD_GRAYSCALE)
            # 将图像旋转90度
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            # 将merged_image和image拼接到merge_image上
            merged_image=cv2.hconcat([merged_image,image])
    # 将merge_image保存到output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    cv2.imwrite(os.path.join(output_path, file_name) , merged_image)
    print("success!")



if __name__ == '__main__':
    folder_path = 'your_data_path'
    output_path = folder_path+"\\output"
    file_name = 'merged_image.png'
    merge_images(folder_path, output_path)
