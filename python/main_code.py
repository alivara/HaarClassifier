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



# need to be edited
def install_opencv():
    # check version ubuntu
    # lsb_release -a
    # lsb_release -d
    
    ### installation opencv 3.4.4
    #Specify OpenCV version
    # cvVersion="3.4.4"

    # mkdir installation
    # mkdir installation/OpenCV-"$cvVersion"
    #
    # sudo apt -y update
    # sudo apt -y upgrade
    #
    # sudo apt -y remove x264 libx264-dev
    #
    # ## Install dependencies
    # sudo apt -y install build-essential checkinstall cmake pkg-config yasm
    # sudo apt -y install git gfortran
    # sudo apt -y install libjpeg8-dev libpng-dev
    #
    # sudo apt -y install software-properties-common
    # sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
    # sudo apt -y update
    #
    # sudo apt -y install libjasper1
    # sudo apt -y install libtiff-dev
    #
    # sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
    # sudo apt -y install libxine2-dev libv4l-dev
    # cd /usr/include/linux
    # sudo ln -s -f ../libv4l1-videodev.h videodev.h
    # cd "$cwd"
    #
    # sudo apt -y install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
    # sudo apt -y install libgtk2.0-dev libtbb-dev qt5-default
    # sudo apt -y install libatlas-base-dev
    # sudo apt -y install libfaac-dev libmp3lame-dev libtheora-dev
    # sudo apt -y install libvorbis-dev libxvidcore-dev
    # sudo apt -y install libopencore-amrnb-dev libopencore-amrwb-dev
    # sudo apt -y install libavresample-dev
    # sudo apt -y install x264 v4l-utils
    #
    # # Optional dependencies
    # sudo apt -y install libprotobuf-dev protobuf-compiler
    # sudo apt -y install libgoogle-glog-dev libgflags-dev
    # sudo apt -y install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen
    #
    # sudo apt -y install python3-dev python3-pip python3-vev
    # sudo -H pip3 install -U pip numpy
    # sudo apt -y install python3-testresources
    #
    # pip install wheel numpy scipy matplotlib scikit-image scikit-learn ipython dlib
    #
    # git clone https://github.com/opencv/opencv.git
    # cd opencv
    # git checkout 3.4
    # cd ..
    #
    # git clone https://github.com/opencv/opencv_contrib.git
    # cd opencv_contrib
    # git checkout 3.4
    # cd ..
    #
    # cd opencv
    # mkdir build
    # cd build
    #
    # sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
    #     libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    #     libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
    #     gfortran openexr libatlas-base-dev python3-dev python3-numpy \
    #     libtbb2 libtbb-dev libdc1394-22-dev
    #
    #
    # cmake -D CMAKE_BUILD_TYPE=RELEASE \
    #     -D CMAKE_INSTALL_PREFIX=/usr/local \
    #     -D INSTALL_C_EXAMPLES=ON \
    #     -D INSTALL_PYTHON_EXAMPLES=ON \
    #     -D OPENCV_GENERATE_PKGCONFIG=ON \
    #     -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    #     -D BUILD_EXAMPLES=ON ..
    #
    # make -j8
    #
    # sudo make install






def rename_file(path):
    '''
    This Function will rename the files
    '''
    os.getcwd()
    for i, filename in enumerate(os.listdir(path)):
        os.rename(path + filename, path + 'image' + "_" + str(i) + ".jpg")

def store_raw_images(path,dim):
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
def call_opencv_createsamples():
    '''
    This Function will call opencv_createsamples
    '''
    print(subprocess.run(["opencv_createsamples"]))
    subprocess.run(["opencv_createsamples -img /opencv_workspace/haarclass/images/pos/image_0.jpg -bg bg.txt -info /opencv_workspace/haarclass/image_0/info/info.lst -pngoutput /opencv_workspace/haarclass/image_0/info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000"])

# need to be edited
def call_opencv_traincascade():
    '''
    This Function will call opencv_traincascade
    '''
    print(subprocess.run(["opencv_traincascade"]))
    subprocess.run(["opencv_traincascade -data /opencv_workspace/haarclass/image_0/data -vec /opencv_workspace/haarclass/image_0/positives.vec -bg bg.txt -numPos 2600 -numNeg 1300 -numStages 10 -w 20 -h 20"])


# need to be edited
def XML_merge(files):
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

# need to be edited
try:
    opts, args = getopt.getopt(sys.argv[1:], "hds:p:t:r:", ["help", "debug","output="])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    usage()
    sys.exit(2)
# output = None
# verbose = False
for opt, arg in opts:
    if opt == "-v":
        verbose = True
    elif opt in ("-h", "--help"):
        usage()
        sys.exit()
    elif opt in ("-o", "--output"):
        output = arg
    else:
        assert False, "unhandled option"
# ...




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

'''Function to run opencv_createsamples'''
# call_opencv_createsamples()


'''Function to run opencv_traincascade'''
# call_opencv_traincascade()
