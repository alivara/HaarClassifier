import os
import cv2
def store_raw_images(dim):
#     neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
#     neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    path = '/Users/alivarastehranjbar/Nextcloud/HaarClassifier/images_1/'
#     if not os.path.exists('neg'):
#         os.makedirs('neg')
#     import cv2
#     import glob

#     images = [cv2.imread(file) for file in glob.glob('path/to/files/*.jpg')]

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

        except Exception as e:
            print(str(e))

x = int(input("x size"))
y = int(input("y size"))
store_raw_images((x,y))
