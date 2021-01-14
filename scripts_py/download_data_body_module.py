import os
from requests import get  # to make GET request
import urllib, tarfile

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

path_cwd = os.getcwd()
path = path_cwd+"/extra_data/body_module"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:
    print ("Successfully created the directory %s " % path)
    os.chdir(path)
    
url = "http://visiondata.cis.upenn.edu/spin/data.tar.gz"
filename = 'data.tar.gz'
print ('Downloading: '+filename)
download(url,filename)

tf = tarfile.open(filename)
tf.extractall()

os.rename('data','data_from_spin')


path = path_cwd+"/extra_data/body_module/pretrained_weights"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:
    print ("Successfully created the directory %s " % path)
    os.chdir(path)
    
print('####Downloading pretrained_weights')
url = "https://dl.fbaipublicfiles.com/eft/2020_05_31-00_50_43-best-51.749683916568756.pt"
filename = '2020_05_31-00_50_43-best-51.749683916568756.pt'
print ('Downloading: '+filename)
download(url,filename)

url = "https://dl.fbaipublicfiles.com/eft/fairmocap_data/body_module/smplx-03-28-46060-w_spin_mlc3d_46582-2089_2020_03_28-21_56_16.pt"
filename = 'smplx-03-28-46060-w_spin_mlc3d_46582-2089_2020_03_28-21_56_16.pt'
print ('Downloading: '+filename)
download(url,filename)


path = path_cwd+"/extra_data/body_module"
os.chdir(path)

print('####Downloading other data')
url = "https://dl.fbaipublicfiles.com/eft/fairmocap_data/body_module/J_regressor_extra_smplx.npy"
filename = 'J_regressor_extra_smplx.npy'
print ('Downloading: '+filename)
download(url,filename)