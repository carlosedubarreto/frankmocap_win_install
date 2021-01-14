import os
from requests import get  # to make GET request
import git,gdown

path_cwd = os.getcwd()
path = path_cwd+"/detectors"


folder_orig = 'hand_detector.d2'
folder_dest= 'hand_only_detector'
### Install 100-DOH hand-only detectors
if not os.path.exists(path+'/'+folder_dest):
    if not os.path.exists(path+'/'+folder_orig):
        os.chdir(path)
        print('downloading '+folder_orig)
        git.Git(path).clone('https://github.com/ddshan/hand_detector.d2.git')
        if not os.path.exists(path+'/'+folder_dest):
            os.rename(folder_orig,folder_dest)
    else:
        print(folder_orig+' already exists')
        if not os.path.exists(path+'/'+folder_dest):
            os.chdir(path)
            os.rename(folder_orig,folder_dest)
            print('folder renamed to '+folder_dest)
       

### downloading weights       
path = path_cwd+"/extra_data/hand_module/hand_detector"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:
    print ("Successfully created the directory %s " % path)
    os.chdir(path)
    
    
url1 = 'https://drive.google.com/uc?id=1H2tWsZkS7tDF8q1-jdjx6V9XrK25EDbE'
url2 = 'https://drive.google.com/uc?id=1OqgexNM52uxsPG3i8GuodDOJAGFsYkPg'
#output = 'spam.txt'
gdown.download(url1, quiet=False) 
gdown.download(url2, quiet=False) 

