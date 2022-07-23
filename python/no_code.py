'''
this code does not run we are still working on it
"its just a copy pase of some source codes with some changes
'''



# importing used library
#import tensorflow as tf
import numpy as np
#import pandas as pd
import os
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import cv2


# image generating
'''
"https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator#flow_from_directory"
'''

def image_generator(main_path,save_path):
    '''
    Generate the Images

    rotation_range: 'Int. Degree range for random rotations'.
    zoom_range: 'Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range]'.
    main_path: Directory of the main images.
    save_path: where to save the created images.

    "created images have size of target_size=(100, 100) and format: jpg"
    '''
    # train_datagen = ImageDataGenerator(rotation_range=rotation,brightness_range=None,zoom_range=zoom,dtype=None)
    #                 # featurewise_center=False,# samplewise_center=False,
    #                 # featurewise_std_normalization=False,
    #                 # samplewise_std_normalization=False,
    #                 # zca_whitening=False,
    #                 # zca_epsilon=1e-06,
    #                 # rotation_range=rotation,
    #                 # width_shift_range=0.0,
    #                 # height_shift_range=0.0,
    #                 # channel_shift_range=0.0,
    #                 # fill_mode='nearest',
    #                 # cval=0.0,
    #                 # horizontal_flip=False,
    #                 # vertical_flip=False,
    #                 # rescale=None,
    #                 # preprocessing_function=None,
    #                 # data_format=None,
    #                 # validation_split=0.0,
    #                 # interpolation_order=1,
    #                 # shear_range=0.0,
    # train_generator = train_datagen.flow_from_directory('/Users/alivarastehranjbar/Nextcloud/HaarClassifier/images_2',  # this is the target directory
    #                                                     target_size=(100, 100),  # all images will be resized to 100*100
    #                                                     class_mode='binary',
    #                                                     batch_size = 25,
    #                                                     save_to_dir= '/Users/alivarastehranjbar/Nextcloud/HaarClassifier/images_2/',
    #                                                     save_format= 'jpg')


    train_datagen = ImageDataGenerator(rescale=1.0/255,rotation_range=rotation,zoom_range=zoom)

    train_generator = train_datagen.flow_from_directory(main_path,  # this is the target directory
                                                        target_size=(100, 100),  # all images will be resized to 224x224
                                                        batch_size=16,
                                                        save_to_dir= save_path,
                                                        save_format= 'jpg',
                                                        class_mode='binary')


#     # show the generated images
#     x, y = train_generator.next()

#     plt.figure(figsize=(9, 9))
#     for i, (img, label) in enumerate(zip(x, y)):
#         plt.subplot(4, 4, i+1)
#         if label == 1:
#             plt.title('D')
#         else:
#             plt.title('U')
#         plt.axis('off')
#         plt.imshow(img, interpolation="nearest")
#-----------------------------------------------------------------------------------

def rename_file(path):
    os.getcwd()
    for i, filename in enumerate(os.listdir(path)):
        os.rename(path + filename, path + 'image' + "_" + str(i) + ".jpg")

#-----------------------------------------------------------------------------------
# Read and creating images with opencv
def store_raw_images(path):
#     neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
#     neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1

#     if not os.path.exists('neg'):
#         os.makedirs('neg')
#     import cv2
#     import glob

#     images = [cv2.imread(file) for file in glob.glob('path/to/files/*.jpg')]

    for i, filename in enumerate(os.listdir(path)):
        try:
            print(i)
            # urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")

            # try to read image with opencv
            # img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            img = cv2.imread(path + filename, path + 'image' + "_" + str(i) + ".jpg",cv2.IMREAD_GRAYSCALE)

            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 60))
            # resized_image = cv2.resize(img)
            cv2.imwrite(path + filename, path + 'image' + "_" + str(i) + ".jpg",resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

# path = '/Users/alivarastehranjbar/Nextcloud/HaarClassifier/images_2/pos_generated/'
# store_raw_images()
#----------------------------------------------------------------------------------

# # find ugly images
# def find_uglies():
#     match = False
#     for file_type in ['neg']:
#         for img in os.listdir(file_type):
#             for ugly in os.listdir('uglies'):
#                 try:
#                     current_image_path = str(file_type)+'/'+str(img)
#                     ugly = cv2.imread('uglies/'+str(ugly))
#                     question = cv2.imread(current_image_path)
#                     if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
#                         print('That is one ugly pic! Deleting!')
#                         print(current_image_path)
#                         os.remove(current_image_path)
#                 except Exception as e:
#                     print(str(e))

#----------------------------------------------------------------------------------

# create the descriptor file
def create_pos_n_neg():
    for file_type in [path]:

        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 100 60\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
#----------------------------------------------------------------------------------s            
if __name__ == "__main__":
    '''Function for generate the images'''
    main_path = '/opencv_workspace/haarclass/images_1/pos'
    save_path = '/opencv_workspace/haarclass/images_1/pos/pos_generated/'
    image_generator(main_path,save_path)

    '''Function for renname'''
    rename_file(save_path)

    '''Function for POS'''
    path = 
    store_raw_images(path)

    '''Function for NEG'''
    path = 
    store_raw_images(path)

    '''Function to create neg and pos'''
    path =
    create_pos_n_neg(path)
# lets find opencv_createsamples
# opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
# opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec

# lets find opencv_traincascade
# opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
