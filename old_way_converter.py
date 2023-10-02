import os
from shutil import copy2 as copy
path = './aldi-sabo/waveform/'

for folders in os.listdir(path):
    count = 0
    for file in os.listdir(path+folders):
        src_path = path+folders+"/"+file
        dest_path = "./waveform/mix/"+folders[0]+str(count)+".png"
        copy(src_path,dest_path)
        count = count+1
