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
### Use python3 to run this program

import os
import cv2
import subprocess
import getopt
import sys
import os.path
import glob
from xml.etree import ElementTree

# default configurations
# conf_opencv = [pos_image_path,opencv_maxxangle,opencv_maxyangle,opencv_maxzangle,opencv_w,opencv_h]
# conf_opencv = "opencv_createsamples -img /opencv_workspace/haarclass/images/pos/image_0.jpg -bg bg.txt \
#                     -info /opencv_workspace/haarclass/image_0/info/info.lst -pngoutput /opencv_workspace/haarclass/image_0/info \
#                     -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000"


class opencv_python():
    '''
    thie class is for creating the image and running the opencv modules
    '''
    def __init__(self,path,conf_opencv):
        self.path = path
        self.conf_opencv = conf_opencv

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
    def call_opencv(self,conf_mode,self.conf_opencv,nohup_mode):
        '''
        This Function will call opencv_createsamples and opencv_traincascade
        '''
        print(subprocess.run(["opencv_createsamples"]))
        print("default config is:","\n opencv_createsamples -img /opencv_workspace/haarclass/images/pos/image_0.jpg\
         -bg bg.txt -info /opencv_workspace/haarclass/image_0/info/info.lst -pngoutput /opencv_workspace/haarclass/image_0/info\
          -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000 -w 20 -h 20 -vec /opencv_workspace/haarclass/image_0/positives.vec")

        print(subprocess.run(["opencv_traincascade"]))
        print("default config is:","\n opencv_traincascade -data /opencv_workspace/haarclass/image_0/data\
         -vec /opencv_workspace/haarclass/image_0/positives.vec -bg bg.txt -numPos 3000 -numNeg 1500 -numStages 10 -w 20 -h 20","\n nohup: False")


        conf_mode = input(str("default of customise"))

        # if user prefered to write own config
        if conf_mode == 'customise':
            self.conf_opencv[0] = input(str('write the positive images path'))
            self.conf_opencv[1] = input(str('maxxangle: '))
            self.conf_opencv[2] = input(str('maxyangle: '))
            self.conf_opencv[3] = input(str('maxzangle: '))
            self.conf_opencv[4] = input(str('number of samples: '))
            self.conf_opencv[5] = input(str('sample width: '))
            self.conf_opencv[6] = input(str('sample height: '))
            self.conf_opencv[7] = input(str('Nember of Stage: '))
            self.conf_opencv[8] = input(str('nohup: True or False'))
            # creating the new config of the opencv_createsamples
            # self.conf_opencv = [pos_image_path,opencv_maxxangle,opencv_maxyangle,opencv_maxzangle,opencv_w,opencv_h]

        ## Running opencv_createsamples
        # first config
        subprocess.run(["opencv_createsamples","-img",self.conf_opencv[0],"-bg","bg.txt","-info",self.conf_opencv[0]+"info.lst","-pngoutput",\
        self.conf_opencv[0]+"info","-maxxangle",self.conf_opencv[1],"-maxyangle",self.conf_opencv[2],"-maxzangle",self.conf_opencv[3],\
        "-num",self.conf_opencv[4]])

        # second config for create vector file
        subprocess.run(["-info",self.conf_opencv[0]+"info.lst","-num",self.conf_opencv[4],"-w",self.conf_opencv[5],"-h",self.conf_opencv[6],"-vec",self.conf_opencv[0]+"positives.vec"])

        ## Running opencv_traincascade
        if nohup_mode == 'True':
            subprocess.run(["nohup","opencv_traincascade","-data",self.conf_opencv[0]+"data","-vec",self.conf_opencv[0]+"positives.vec",\
            "-bg","bg.txt","-numPos",str(int(self.conf_opencv[4])-int((int(self.conf_opencv[4])/10))),"-numNeg",str(int(self.conf_opencv[4])/2),\
            "-numStages",self.conf_opencv[6],"-w",self.conf_opencv[5],"-h",self.conf_opencv[6]],"&")
        else:
            subprocess.run(["opencv_traincascade","-data",self.conf_opencv[0]+"data","-vec",self.conf_opencv[0]+"positives.vec",\
            "-bg","bg.txt","-numPos",str(int(self.conf_opencv[4])-int((int(self.conf_opencv[4])/10))),"-numNeg",str(int(self.conf_opencv[4])/2),\
            "-numStages",self.conf_opencv[6],"-w",self.conf_opencv[5],"-h",self.conf_opencv[6]])


    def store_XML(self,XML_path):
        '''
        This Function will call opencv_traincascade
        '''
        print(subprocess.run(["opencv_traincascade"]))
        # check the file names
        xml_files = glob.glob(files +"/haarclass.xml")
        subprocess.run(["rm","-rf","/opencv_workspace/haarclass/XML_file"])
        subprocess.run(["mkdir","/opencv_workspace/haarclass/XML_file"])
        subprocess.run(["cd","/opencv_workspace/haarclass/XML_file/"])

        return XML_path

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

    # opencv default config:
    conf_opencv = ["/opencv_workspace/haarclass/images/pos/","0.5","0.5","0.5","3000","20","20","10","False"]

    os.getcwd()
    for i, filename in enumerate(os.listdir(path)):
        '''
        starting program for all images in the pos path
        '''
        # running opencv modules for creating samples and training
        '''Function to run opencv_createsamples and opencv_traincascade'''
        opencv_python.call_opencv(conf_mode)

    '''Function to copy all the XML files'''
    opencv_python.store_XML(self)

    '''Function to merge all the XML files'''
    opencv_python.XML_merge(XML_path)




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
