import os
def create_pos_n_neg():
    file_type = '/Users/alivarastehranjbar/Desktop/neg_from_git/negatives'
    print(file_type)
    for img in os.listdir(file_type):
        print(img)
        line = file_type+'/'+img+'\n'
        with open('/Users/alivarastehranjbar/Desktop/bg.txt','a') as f:
            f.write(line)

create_pos_n_neg()
