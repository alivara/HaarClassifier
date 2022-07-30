### Loader functions:

_VERSION = '1.0.0'

def setversion(version):
    if version != _VERSION:
        raise ValueError('Dynamic versioning not available')

def setalphaversions(*alpha_versions):
    if alpha_versions != ():
        raise ValueError('Dynamic versioning not available')

def version(alpha = 0):
    if alpha:
        return ()
    else:
        return _VERSION

def installedversions(alpha = 0):
    if alpha:
        return ()
    else:
        return (_VERSION,)


######################################################################
### File: main_code.py


import os
import cv2
import subprocess
import getopt
import sys
import os.path
import glob
from xml.etree import ElementTree


class opencv_python():
    '''
    thie class is for creating the image and running the opencv modules
    '''
    def __init__(self,path):
        self.path = path

    def rename_file(self,path):
        '''
        This Function will rename the files
        '''
        os.getcwd()
        for i, filename in enumerate(os.listdir(path)):
            os.rename(path + filename, path + 'image' + "_" + str(i) + ".jpg")

    def store_raw_images(self,path,dim):
        '''
        This Function will read the files with opencv and resize them
        '''
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

    # need to be edited
    def call_opencv_createsamples(self,self.config_createsamples):
        '''
        This Function will call opencv_createsamples
        '''
        print(subprocess.run(["opencv_createsamples"]))
        subprocess.run(["opencv_createsamples -img /opencv_workspace/haarclass/images/pos/image_0.jpg -bg bg.txt -info /opencv_workspace/haarclass/image_0/info/info.lst -pngoutput /opencv_workspace/haarclass/image_0/info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000"])

    # need to be edited
    def call_opencv_traincascade(self,self.config_traincascade):
        '''
        This Function will call opencv_traincascade
        '''
        print(subprocess.run(["opencv_traincascade"]))
        subprocess.run(["opencv_traincascade -data /opencv_workspace/haarclass/image_0/data -vec /opencv_workspace/haarclass/image_0/positives.vec -bg bg.txt -numPos 2600 -numNeg 1300 -numStages 10 -w 20 -h 20"])


    def store_XML(self,XML_path):
        '''
        This Function will call opencv_traincascade
        '''
        print(subprocess.run(["opencv_traincascade"]))
        subprocess.run(["rm -rf /opencv_workspace/haarclass/XML_file"])
        subprocess.run(["mkdir /opencv_workspace/haarclass/XML_file"])
        subprocess.run(["cd /opencv_workspace/haarclass/XML_file/"])


    # need to be edited
    def XML_merge(self,files):
        '''
        This Functions is for combination of XML files
        '''
        xml_files = glob.glob(files +"/*.xml")
        xml_element_tree = None
        for xml_file in xml_files:
            data = ElementTree.parse(xml_file).getroot()
            # print ElementTree.tostring(data)
            for result in data.iter('results'):
                if xml_element_tree is None:
                    xml_element_tree = data
                    insertion_point = xml_element_tree.findall("./results")[0]
                else:
                    insertion_point.extend(result)
        if xml_element_tree is not None:
            print ElementTree.tostring(xml_element_tree)


# # need to be edited
# try:
#     opts, args = getopt.getopt(sys.argv[1:], "hds:p:t:r:", ["help", "debug","output="])
# except getopt.GetoptError as err:
#     # print help information and exit:
#     print(err)  # will print something like "option -a not recognized"
#     usage()
#     sys.exit(2)
# # output = None
# # verbose = False
# for opt, arg in opts:
#     if opt == "-v":
#         verbose = True
#     elif opt in ("-h", "--help"):
#         usage()
#         sys.exit()
#     elif opt in ("-o", "--output"):
#         output = arg
#     else:
#         assert False, "unhandled option"
# # ...



if __name__ == "__main__":
    print ("--------------- Starting the opencv with python code ---------------")

    img_type = str(input('Please specify the image kind (pos or neg): '))
    path = str(input('\nPlease insert the path: '))

    opencv_python = opencv_python()
    ''' Function For rename the images '''
    opencv_python.rename_file(path)

    print("\nNow please insert the x and y for resize.")
    x = int(input("x size: "))
    y = int(input("y size: "))

    ''' Function For read the images with opencv '''
    opencv_python.store_raw_images(path,(x,y))


    os.getcwd()
    for i, filename in enumerate(os.listdir(path)):
        '''
        starting program for all images in the pos path
        '''

        '''Function to run opencv_createsamples'''
        opencv_python.call_opencv_createsamples()


        '''Function to run opencv_traincascade'''
        opencv_python.call_opencv_traincascade()

    '''Function to merge all the XML files'''
    opencv_python.XML_merge(files)




    # ''' Function For resize the images '''
    # img_type = str(input('Please specify the image kind (pos or neg): '))
    # path = str(input('\nPlease insert the path: '))

    # ''' Function For rename the images '''
    # rename_file(path)

    # print("\nNow please insert the x and y for resize.")
    # x = int(input("x size: "))
    # y = int(input("y size: "))
    #
    # ''' Function For read the images with opencv '''
    # store_raw_images(path,(x,y))

    '''Function to run opencv_createsamples'''
    # call_opencv_createsamples()


    '''Function to run opencv_traincascade'''
    # call_opencv_traincascade()
