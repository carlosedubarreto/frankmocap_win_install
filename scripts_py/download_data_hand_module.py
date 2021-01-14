import os,tarfile
from requests import get  # to make GET request

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

path_cwd = os.getcwd()
path = path_cwd+"/extra_data/hand_module"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:
    print ("Successfully created the directory %s " % path)
    os.chdir(path)

#### downloading other data
url = "https://dl.fbaipublicfiles.com/eft/fairmocap_data/hand_module/SMPLX_HAND_INFO.pkl"
filename = 'SMPLX_HAND_INFO.pkl'
print ('Downloading: '+filename)
download(url,filename)

url = "https://dl.fbaipublicfiles.com/eft/fairmocap_data/hand_module/mean_mano_params.pkl"
filename = 'mean_mano_params.pkl'
print ('Downloading: '+filename)
download(url,filename)


path = path_cwd+"/extra_data/hand_module/pretrained_weights"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:
    print ("Successfully created the directory %s " % path)
    os.chdir(path)

url = "https://dl.fbaipublicfiles.com/eft/fairmocap_data/hand_module/checkpoints_best/pose_shape_best.pth"
filename = 'pose_shape_best.pth'
print ('Downloading: '+filename)
download(url,filename)

