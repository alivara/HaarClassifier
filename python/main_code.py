######################################################################
"""
File: main_code.py
Author: alivarasteh100@gmail.com
Date: .../08/2022
Use python3 to run this program
copy positive files to "/opencv_workspace/haarclass/images/pos/"
"""
import os
import cv2
import subprocess
import getopt
import sys
import os.path
import glob
import struct
import argparse
import traceback
from xml.etree import ElementTree

def rename_file(path_rename):
    '''
    This Function will rename the files.
        path: locarion of the files;
            Example: /.../.../
    '''
    os.getcwd()
    for m, filename in enumerate(os.listdir(path_rename)):
        os.rename(path_rename + filename, path_rename + 'image' + "_" + str(m) + ".jpg")

def store_raw_images(path_raw,dim):
    '''
    This Function will read the files with opencv and resize them.
        path: location of raw images to be resized and read with opencv.
        dim: (x,y) new size of the images.

    ## another way to resize
    # scale_percent = 60 # percent of original size
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # dim = (100, 60)
    # should be larger than samples / pos pic (so we can place our image on it)
    # resized_image = cv2.resize(img)
    '''
    pic_num = 1

    for j, filename in enumerate(os.listdir(path_raw)):
        try:
            print("image number: ",j)

            # try to read image with opencv
            img = cv2.imread(path_raw + 'image' + "_" + str(j) + ".jpg",cv2.IMREAD_GRAYSCALE)

            ## Second way to resize
            resized_image = cv2.resize(img, dim,interpolation = cv2.INTER_AREA)
            cv2.imwrite(path_raw + 'image' + "_" + str(j) + ".jpg",resized_image)
            pic_num += 1

            # For negative images we need to create bg.txt file
            if path_raw == "/opencv_workspace/haarclass/images/neg/":
                line = path_raw + 'image' + "_" + str(j) + ".jpg"+'\n'
                with open('/opencv_workspace/haarclass/bg.txt','a') as f:
                    f.write(line)

        except Exception as e:
            print(str(e))

def call_opencv_createsamples(pos_image_path,num_pos,conf_opencv_createsamples):
    '''
    This Function will call opencv_createsamples.
        pos_image_path: Location of positive images.
        num_pos: The number of positive image which is using in opencv_createsamples.
        conf_opencv_createsamples: Default configuration of opencv_createsamples.
    '''
    # print(subprocess.run(["opencv_createsamples"]))
    print("\ndefault config is:","\n opencv_createsamples -img /opencv_workspace/haarclass/images/pos/image_i.jpg\
     -bg bg.txt -info /opencv_workspace/haarclass/image_i/info/info.lst -pngoutput /opencv_workspace/haarclass/image_i/info\
      -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000 -w 20 -h 20 -vec /opencv_workspace/haarclass/image_i/positives.vec")

    try:
        ## Choosing the configuration mode
        conf_mode = 'default'
        conf_mode = input(str("\n setting for opencv_createsamples: default or customise? "))

        # if user prefered to write own config
        if conf_mode == 'customise':
            conf_opencv_createsamples[0] = str(input('maxxangle: '))
            conf_opencv_createsamples[1] = str(input('maxyangle: '))
            conf_opencv_createsamples[2] = str(input('maxzangle: '))
            conf_opencv_createsamples[3] = str(input('number of samples: '))
            conf_opencv_createsamples[4] = str(input('sample width: '))
            conf_opencv_createsamples[5] = str(input('sample height: '))

        elif (conf_mode != 'default') and (conf_mode != 'customise'):
            print("No operation chosed")
            exit()

        ## Running opencv_createsamples
        # first config
        subprocess.run(["opencv_createsamples","-img",str(pos_image_path),"-bg","bg.txt",
            "-info","/opencv_workspace/haarclass/images_data/image_"+str(num_pos)+"/info/info.lst",
            "-pngoutput","/opencv_workspace/haarclass/images_data/image_"+str(num_pos)+"/info",
            "-maxxangle",conf_opencv_createsamples[0],"-maxyangle",conf_opencv_createsamples[1],
            "-maxzangle",conf_opencv_createsamples[2],"-num",conf_opencv_createsamples[3]])

        # second config for create vec file
        subprocess.run(["opencv_createsamples","-info","/opencv_workspace/haarclass/images_data/image_"+str(num_pos)+"/info/info.lst",
            "-num",conf_opencv_createsamples[3],"-w",conf_opencv_createsamples[4],"-h",conf_opencv_createsamples[5],"-vec",
            "/opencv_workspace/haarclass/images_data/image_"+str(num_pos)+"/positives.vec"])

    except Exception as e:
        print(str(e))

def call_opencv_traincascade(mergedvec,conf_opencv_traincascade,nohup_mode = "False"):
    '''
    This Function will call opencv_traincascade.
        mergedvec: Location of merged vec files or one sinlge image vec.
        conf_opencv_traincascade: Default configuration of opencv_traincascade.
        nohup_mode: This parameter is "False" by default, it can change to "True"
    '''
    # print(subprocess.run(["opencv_traincascade"]))
    print("\ndefault config is:","\n opencv_traincascade -data /opencv_workspace/haarclass/image_i/data\
     -vec (merged file or one single) -bg bg.txt -numPos 3000 -numNeg 1500 -numStages 10 -w 20 -h 20","\n nohup: False")

    try:
        ## Choosing the configuration mode
        conf_mode_t = 'default'
        conf_mode_t = input(str("\n setting for opencv_traincascade: default or customise? "))

        # if user prefered to write own config
        if conf_mode_t == 'customise':
            conf_opencv_traincascade[0] = str(input('number of Positive: '))
            conf_opencv_traincascade[1] = str(input('number of Negative: '))
            conf_opencv_traincascade[2] = str(input('sample width: '))
            conf_opencv_traincascade[3] = str(input('sample height: '))
            conf_opencv_traincascade[4] = str(input('Nember of Stage: '))
            nohup_mode = str(input('nohup: True or False'))

        elif (conf_mode_t != 'default') and (conf_mode_t != 'customise'):
            print("No operation chosed")
            exit()

        ## Running opencv_traincascade
        if nohup_mode == "True":
            subprocess.run(["nohup","opencv_traincascade","-data","/opencv_workspace/haarclass/images_data/data","-vec",
                str(mergedvec),"-bg","bg.txt","-numPos",str(conf_opencv_traincascade[0]),"-numNeg",str(conf_opencv_traincascade[1]),
                "-numStages",conf_opencv_traincascade[4],"-w",conf_opencv_traincascade[2],"-h",conf_opencv_traincascade[3],"&"])

        elif nohup_mode == "False":
            subprocess.run(["opencv_traincascade","-data","/opencv_workspace/haarclass/images_data/data","-vec",str(mergedvec),
                "-bg","bg.txt","-numPos",str(conf_opencv_traincascade[0]),"-numNeg",str(conf_opencv_traincascade[1]),"-numStages",
                conf_opencv_traincascade[4],"-w",conf_opencv_traincascade[2],"-h",conf_opencv_traincascade[3]])

        else:
            print("No operation chosed")
            exit()

    except Exception as e:
        print(str(e))

def merge_vec_files(vec_directory, output_vec_file):
	"""
    File: mergevec.py
    Author: blake.w.wulfe@gmail.com
    Date: 6/13/2014
    File Description:
    	This file contains a function that merges .vec files called "merge_vec_files".
    	I made it as a replacement for mergevec.cpp (created by Naotoshi Seo.
    	See: http://note.sonots.com/SciSoftware/haartraining/mergevec.cpp.html)
    	in order to avoid recompiling openCV with mergevec.cpp.

    	To use the function:
    	(1) Place all .vec files to be merged in a single directory (vec_directory).
    	(2) Navigate to this file in your CLI (terminal or cmd) and type "python mergevec.py -v your_vec_directory -o your_output_filename".

    		The first argument (-v) is the name of the directory containing the .vec files
    		The second argument (-o) is the name of the output file

	Iterates throught the .vec files in a directory and combines them.

	(1) Iterates through files getting a count of the total images in the .vec files
	(2) checks that the image sizes in all files are the same
    --------------------------------------------------------------------------------
	The format of a .vec file is:

	4 bytes denoting number of total images (int)
	4 bytes denoting size of images (int)
	2 bytes denoting min value (short)
	2 bytes denoting max value (short)

	ex: 	6400 0000 4605 0000 0000 0000

		hex		6400 0000  	4605 0000 		0000 		0000
			   	# images  	size of h * w		min		max
		dec	    	100     	1350			0 		0

	:type vec_directory: string
	:param vec_directory: Name of the directory containing .vec files to be combined.
				Do not end with slash. Ex: '/Users/username/Documents/vec_files'

	:type output_vec_file: string
	:param output_vec_file: Name of aggregate .vec file for output.
		Ex: '/Users/username/Documents/aggregate_vec_file.vec'

	"""

	# Check that the .vec directory does not end in '/' and if it does, remove it.
	if vec_directory.endswith('/'):
		vec_directory = vec_directory[:-1]
	# Get .vec files
	files = glob.glob('{0}/*.vec'.format(vec_directory))

	# Check to make sure there are .vec files in the directory
	if len(files) <= 0:
		print('Vec files to be mereged could not be found from directory: {0}'.format(vec_directory))
		sys.exit(1)
	# Check to make sure there are more than one .vec files
	if len(files) == 1:
		print('Only 1 vec file was found in directory: {0}. Cannot merge a single file.'.format(vec_directory))
		sys.exit(1)

	# Get the value for the first image size
	prev_image_size = 0
	try:
		with open(files[0], 'rb') as vecfile:
			content = b''.join((line) for line in vecfile.readlines())
			val = struct.unpack('<iihh', content[:12])
			prev_image_size = val[1]
	except IOError as e:
		print('An IO error occured while processing the file: {0}'.format(f))
		exception_response(e)

	# Get the total number of images
	total_num_images = 0
	for f in files:
		try:
			with open(f, 'rb') as vecfile:
				content = b''.join((line) for line in vecfile.readlines())
				val = struct.unpack('<iihh', content[:12])
				num_images = val[0]
				image_size = val[1]
				if image_size != prev_image_size:
					err_msg = """The image sizes in the .vec files differ. These values must be the same. \n The image size of file {0}: {1}\n
						The image size of previous files: {0}""".format(f, image_size, prev_image_size)
					sys.exit(err_msg)

				total_num_images += num_images
		except IOError as e:
			print('An IO error occured while processing the file: {0}'.format(f))
			exception_response(e)

	# Iterate through the .vec files, writing their data (not the header) to the output file
	# '<iihh' means 'little endian, int, int, short, short'
	header = struct.pack('<iihh', total_num_images, image_size, 0, 0)
	try:
		with open(output_vec_file, 'wb') as outputfile:
			outputfile.write(header)

			for f in files:
				with open(f, 'rb') as vecfile:
					content = b''.join((line) for line in vecfile.readlines())
					outputfile.write(bytearray(content[12:]))
	except Exception as e:
		exception_response(e)

def store_VEC():
    '''
    This Function will call create VEC_path and rename them which is needed for VEC_merge
    '''
    subprocess.run(["rm","-rf","/opencv_workspace/haarclass/VEC_file"])
    subprocess.run(["mkdir","/opencv_workspace/haarclass/VEC_file"])

    # copy all the VEC files to VEC_path
    path_store_VEC = "/opencv_workspace/haarclass/images_data/"
    for n, filename in enumerate(os.listdir(path_store_VEC)):
        # "/opencv_workspace/haarclass/images_data/image_"+str(i)
        subprocess.run(["cp","-r",str(path_store_VEC)+str(filename)+"/positives.vec","/opencv_workspace/haarclass/VEC_file/"])
        subprocess.run(["mv","/opencv_workspace/haarclass/VEC_file/positives.vec","/opencv_workspace/haarclass/VEC_file/positives_"+str(n)+".vec"])

# edit
def store_XML():
    '''
    This Function will store XML file to a path
    '''
    # xml_files = glob.glob(files +"/haarclass.xml")
    subprocess.run(["mkdir","/opencv_workspace/haarclass/XML_file"])

    # copy all the VEC files to VEC_path
    path = "/opencv_workspace/haarclass/images_data/"
    for n, filename in enumerate(os.listdir(path)):
        # "/opencv_workspace/haarclass/images_data/image_"+str(i)
        subprocess.run(["cp","-r",str(path)+str(filename)+"/cascade.xml","/opencv_workspace/haarclass/XML_file/"])

    VEC_path = "/opencv_workspace/haarclass/VEC_file/"
    return VEC_path

def XML_merge():
    '''
    This Functions is for combination of XML files.
    *** we do not use it in this case. ***
    '''
    XML_path = "/opencv_workspace/haarclass/XML_file/"
    xml_files = glob.glob(XML_path +"/*.xml")
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
        print(ElementTree.tostring(xml_element_tree))


# *** we do not use it in this case. ***
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
    print ("--- Starting the program (if you choose default, it would be mostly auto) ---")
    print("\n-------------------- Create neg file to copy orginal Negative images.")
    subprocess.run(["rm","-rf","/opencv_workspace/haarclass/images/neg"])
    subprocess.run(["mkdir","/opencv_workspace/haarclass/images/neg"])
    subprocess.run(["cp","-r","/opencv_workspace/negative_images_backup/.","/opencv_workspace/haarclass/images/neg/"])

    print("\n-------------------- Create folder to store images data.")
    subprocess.run(["rm","-rf","/opencv_workspace/haarclass/images_data"])
    subprocess.run(["mkdir","/opencv_workspace/haarclass/images_data"])

    ## First part of program
    try:
        # start getting data from user for resizing images.
        for images_path in ["/opencv_workspace/haarclass/images/pos/","/opencv_workspace/haarclass/images/neg/"]:
            if images_path == "/opencv_workspace/haarclass/images/pos/" :
                # positive images need to be renamed
                rename_file(images_path)
                print("\n editing the positive images.")
                x = 100
                y = 60
                print("\ndefault resize for positive is x = {}, y = {}".format(x,y))

            if images_path == "/opencv_workspace/haarclass/images/neg/" :
                print("\n editing the negative images.")
                x = 680
                y = 480
                print("\ndefault resize for negative is x = {}, y = {}".format(x,y))

            change_size = str(input("\n resize settings: default or customise? "))

            if change_size == "customise":
                print("\nNow please insert the x and y for resize.")
                x = int(input("x size: "))
                y = int(input("y size: "))

            elif (change_size != 'default') and (change_size != 'customise'):
                print("No operation chosed")
                exit()

            ## Read and resize images with opencv
            store_raw_images(images_path,(x,y))

    except Exception as e:
        print(str(e))


    ## Second part of program
    path = "/opencv_workspace/haarclass/images/pos/"
    try:
        num_pos = 0
        os.getcwd()
        for i, filename in enumerate(os.listdir(path)):
            '''
            starting program for all images in the pos path
            '''
            # running opencv modules for creating samples and training
            ## Make a folder for store each positive image data
            subprocess.run(["mkdir","/opencv_workspace/haarclass/images_data/image_"+str(num_pos)])
            subprocess.run(["mkdir","/opencv_workspace/haarclass/images_data/image_"+str(num_pos)+"/info"])

            ## directory of positive image to be used
            pos_image_path = path + str("image_") + str(num_pos) + str(".jpg")
            ## Start opencv_createsamples
            # opencv_createsamples default config:
            conf_opencv_createsamples = ["0.5","0.5","0.5","3000","20","20"]
            call_opencv_createsamples(pos_image_path,num_pos,conf_opencv_createsamples)
            num_pos += 1

        if num_pos >1 :
            ## if we had more than one positive image
            # Running store_VEC to store all vectores to a directory
            store_VEC()

            ## Create path for store the merged vectors to a directory
            subprocess.run(["mkdir","/opencv_workspace/haarclass/VEC_file/Merged_VEC"])
            output_filename = "/opencv_workspace/haarclass/VEC_file/Merged_VEC/mrgvec"
            VEC_path = "/opencv_workspace/haarclass/VEC_file/"

            ## running the merge vect
            merge_vec_files(VEC_path, output_filename)
            subprocess.run(["mv","/opencv_workspace/haarclass/VEC_file/Merged_VEC/mrgvec","/opencv_workspace/haarclass/VEC_file/Merged_VEC/mrgvec.vec"])
            mergedvec = "/opencv_workspace/haarclass/VEC_file/Merged_VEC/mrgvec.vec"

        else:
            ## if we had just one positive image
            mergedvec = "/opencv_workspace/haarclass/images_data/image_0/positives.vec"

        # Running call_opencv_traincascade
        conf_opencv_traincascade = ["3000","1500","20","20","10"]
        subprocess.run(["mkdir","/opencv_workspace/haarclass/images_data/data"])
        call_opencv_traincascade(mergedvec,conf_opencv_traincascade,nohup_mode = "False")

        print("\n--------------------------- Done ---------------------------")

    except Exception as e:
        print(str(e))
