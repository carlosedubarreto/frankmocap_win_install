import os
from requests import get  # to make GET request
import git
import urllib
        
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

# define the name of the directory to be created
path_cwd = os.getcwd()
path = path_cwd+"/detectors"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
    
### download human pose estimation git
if not os.path.exists(path+'/body_pose_estimator'):
    if not os.path.exists(path+'/lightweight-human-pose-estimation.pytorch'):
        os.chdir(path)
        print('downloading lightweight-human-pose-estimation.pytorch')
        git.Git(path).clone('https://github.com/jhugestar/lightweight-human-pose-estimation.pytorch.git')
        if not os.path.exists(path+'/body_pose_estimator'):
            os.rename('lightweight-human-pose-estimation.pytorch','body_pose_estimator')
    else:
        print('lightweight-human-pose-estimation.pytorch already exists')
        if not os.path.exists(path+'/body_pose_estimator'):
            os.chdir(path)
            os.rename('lightweight-human-pose-estimation.pytorch','body_pose_estimator')
            print('folder renamed to body_pose_estimator')


path = path_cwd+"/extra_data/body_module/body_pose_estimator"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:
    print ("Successfully created the directory %s " % path)
    os.chdir(path)


### falta baixar pre trained model

url = "https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth"
filename = 'checkpoint_iter_370000.pth'

print ('Downloading: '+filename)
download(url,filename)