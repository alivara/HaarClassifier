import os
import cv2

def rename_file(path):
    os.getcwd()
    for i, filename in enumerate(os.listdir(path)):
        os.rename(path + filename, path + 'image' + "_" + str(i) + ".jpg")

def store_raw_images(path,dim):
    pic_num = 1

    for i, filename in enumerate(os.listdir(path)):
        try:
            print(i)

            # try to read image with opencv
            # img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            img = cv2.imread(path + 'image' + "_" + str(i) + ".jpg",cv2.IMREAD_GRAYSCALE)
            # print(img)
            # scale_percent = 60 # percent of original size
            # width = int(img.shape[1] * scale_percent / 100)
            # height = int(img.shape[0] * scale_percent / 100)
            # dim = (100, 60)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, dim,interpolation = cv2.INTER_AREA)
            # resized_image = cv2.resize(img)
            cv2.imwrite(path + 'image' + "_" + str(i) + ".jpg",resized_image)
            pic_num += 1

            if img_type == 'neg':
                line = path + 'image' + "_" + str(i) + ".jpg"+'\n'
                with open('/opencv_workspace/haarclass/bg.txt','a') as f:
                    f.write(line)

        except Exception as e:
            print(str(e))


file_type = '/opencv_workspace/haarclass/images/neg'



''' Function For resize the images '''
img_type = str(input('Please specify the image kind (pos or neg): '))
path = str(input('\nPlease insert the path: '))

''' Function For rename the images '''
rename_file(path)

print("\nNow please insert the x and y for resize.")
x = int(input("x size: "))
y = int(input("y size: "))

''' Function For read the images with opencv '''
store_raw_images(path,(x,y))
