import os,tarfile
from requests import get  # to make GET request

path_cwd = os.getcwd()
os.chdir(path_cwd)
#### Downloading sample videos
url = "https://dl.fbaipublicfiles.com/eft/sampledata_frank.tar"
filename = 'sample_data_frank.tar'
print ('Downloading: '+filename)
download(url,filename)

tf = tarfile.open(filename)
tf.extractall()