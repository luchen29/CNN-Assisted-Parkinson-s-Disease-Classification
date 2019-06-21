#Read PPMI.cvs file to seprate PD and HC image datas

import os
#import sys
import csv
import shutil


def split_label(csv_file):
    # Read in the csv file.
    lable_file = open(csv_file,'r')
    reader = csv.reader(lable_file)
    header = next(reader)
    pic_Index = header.index('Subject')
    group_Index = header.index('Group')
    # Loop all rows in reader:
    for row in reader:
        if row[group_Index] == 'PD':
            PD.append( row[pic_Index])
        elif row[group_Index] == 'Control':
            HC.append( row[pic_Index])
        else:
            print("Unknown group")
    lable_file.close()

# Readin the PD/HC list
def labeled_img (labeled_list, ori_dir, new_dir):
    os.mkdir(new_dir)
    for num in labeled_list:
        for item in os.listdir(ori_dir):
            if num in item:
                shutil.copy(os.path.join(ori_dir, item),new_dir)
                input_f = os.path.join(ori_dir, item)
                #ex_command = "med2image -i %s -d ./%s -o mwp1%s.jpg -s m" %(input_f,new_dir,num)
                #os.system(ex_command)
                #else:
#labeled_list.remove(num)


                #shutil.copy(os.path.join(ori_dir, item),new_dir)
                # use this line if you don't want to keep the original data in the original GM/WM folder
                # shutil.copy(os.path.join(ori_dir, item),new_dir)


# Please change path
file_Path = "/Users/luchenliu/Documents/UAlberta_CS_MM/deep_learning/project/Sara_Info"
#GM_path = "/Users/luchenliu/Documents/UAlberta_CS_MM/deep_learning/project/Sara_Info/gm"
WM_path = "/Users/luchenliu/Documents/UAlberta_CS_MM/deep_learning/project/Sara_Info/wm"


# Change target directory
#gm_PD_folder = 'gmPD_slice'
#gm_HC_folder = 'gmHC_slice'
wm_PD_folder = 'wmPD_slice'
wm_HC_folder = 'wmHC_slice'

csv_file = 'PPMI.csv'
PD=[]
HC=[]
split_label(csv_file)

labeled_img(HC,WM_path,wm_HC_folder)
labeled_img(PD,WM_path,wm_PD_folder)
#labeled_img(HC,GM_path,gm_HC_folder)
#labeled_img(PD,GM_path,gm_PD_folder)
