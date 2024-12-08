Enviroment Setup Steps:

1. Setup conda env

conda create -n maskrcnn opencv python=3.6.12

2. Install dependencies manually

pip install -r numpy scipy cython h5py==2.10.0 Pillow scikit-image tensorflow==1.14.0 keras==2.0.8 jupyter

(Note: can also install tensorflow-gpu==1.15.0 additionally)

3. Install mask-rcnn 2.1

gh repo clone matterport/Mask\_RCNN
cd ./Mask\_RCNN/
python setup.py install

4. Get weights from the cloned repo

Weights in mask\_rcnn\_coco.h5
