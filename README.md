# frankmocap_win_install

#Video Tutorial  
[![Video Tutorial to instal Frankmocap](https://img.youtube.com/vi/MYLMM7jOMS4/0.jpg)](https://www.youtube.com/watch?v=MYLMM7jOMS4) 


# Instructions

Software to install before doing Frankmocap installation:

<ul>
  <li>VisualStudio 2017</li>
  <li>Nvidia Cuda Driver 10.0</li>
  <li>Miniconda</li>
  <li>FFMPEG</li>
</ul>
 

Download Visual Studio 2017 and install it (or use the vs_community.exe in this github)
https://visualstudio.microsoft.com/pt-br/vs/older-downloads/

the option I think is the most important is the C++ package


Download CUDA 10.0
https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10

Miniconda  
https://docs.conda.io/en/latest/miniconda.html

FFMPEG  
https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip


## unpack to the same folder
https://github.com/facebookresearch/frankmocap  
and  
https://github.com/carlosedubarreto/frankmocap_win_install



## Create virtual enviroment in conda
conda create -n frankmocap python=3.7  
conda activate frankmocap  

## Install cuda 
conda install cudatoolkit=10.1 cudnn=7.6.0

## Install pytorch and torchvision 
conda install -c pytorch pytorch==1.6.0 torchvision cudatoolkit=10.1

## Install GIT (not explained in the video)
conda install -c anaconda git

## run this comand
"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars64.bat"

# Execute this batch to Install other required libraries
install_win_full_body.bat


## Setting SMPL/SMPL-X Models  
below you will have 2 links that you must register and download some files  

Goto:  
http://smplify.is.tue.mpg.de/downloads   
Download the file: mpips-smplify_public_v2.zip

extract the file (that is inside the zip)  
\smplify_public\code\models\basicModel_neutral_lbs_10_207_0_v1.0.0.pkl

to  
 ./extra_data/smpl/  


Goto:
https://smpl-x.is.tue.mpg.de/  
Download the file: models_smplx_v1_1.zip  
  
extract the file (that is inside the zip)  
\models\smplx\SMPLX_NEUTRAL.pkl  

to  
 ./extra_data/smpl/  
  
  
## execution test  
python -m demo.demo_frankmocap --input_path ./sampledata/single_totalbody.mp4 --out_dir ./mocap_output --save_pred_pkl


# Blender addon to import data

There is a Blender addon that you can download for free to import the data in a easier way.
Go to https://gum.co/mocap_import and download it.

To use to import VIBE pkl data, it is needed to install a python package first.
To install it on windows, replace the following code with the directory where your blender is installed (or unzipped)

```bash
D:\Blender\blender-2.92.0-windows64\2.92\python\bin\python.exe D:\Blender\blender-2.92.0-windows64\2.92\python\lib\site-packages\pip install joblib'
```

