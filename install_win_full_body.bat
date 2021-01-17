
rem ####### installing files pre packed

REM pip install whl/faster_rcnn-0.1-cp37-cp37m-win_amd64.whl
pip install whl/detectron2-0.3-cp37-cp37m-win_amd64.whl
pip install whl/opendr-0.73-py3-none-any.whl

pip install -r requirements_alter.txt

echo Installing a third-party 2D keypoint detector
python scripts_py/install_pose2d.py

echo Download extra data for body module
python scripts_py/download_data_body_module.py

echo Installing a third-party hand detector
python scripts_py/install_hand_detectors.py 

rem installing the hand object detector
"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars64.bat"
set DISTUTILS_USE_SDK=1
cd detectors\hand_object_detector\lib
python setup.py build develop
cd ../../..


echo Download extra data for hand module
python scripts_py/download_data_hand_module.py

echo Downloading sample videos
python scripts_py/download_sample_video.py
