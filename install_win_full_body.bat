
rem ####### installing files pre packed

pip install whl/faster_rcnn-0.1-cp37-cp37m-win_amd64.whl
pip install whl/detectron2-0.3-cp37-cp37m-win_amd64.whl
pip install whl/opendr-0.73-py3-none-any.whl

pip install -r requirements_alter.txt

echo Installing a third-party 2D keypoint detector
python scripts_py/install_pose2d.py

echo Download extra data for body module
python scripts_py/download_data_body_module.py

echo Installing a third-party hand detector
python scripts_py/install_hand_detectors.py 

echo Download extra data for hand module
python scripts_py/download_data_hand_module.py

echo Downloading sample videos
python scripts_py/download_sample_video.py
