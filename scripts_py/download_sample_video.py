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
os.chdir(path_cwd)
#### Downloading sample videos
url = "https://dl.fbaipublicfiles.com/eft/sampledata_frank.tar"
filename = 'sample_data_frank.tar'
print ('Downloading: '+filename)
download(url,filename)

tf = tarfile.open(filename)
tf.extractall()