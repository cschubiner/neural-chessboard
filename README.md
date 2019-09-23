## Clay stuff
Build the container:
docker build -t chess-container .
docker tag chess-container gcr.io/chess-ec2/chess-container
docker push gcr.io/chess-ec2/chess-container

docker run -it chess-container /bin/bash

docker run -it --mount src="$(pwd)",target=/test_container,type=bind chess-container /bin/bash

python3 main.py detect --input="clayboards/IMG_1353.jpg" --output="clayboards_out/board_1353.jpg"


pip3 install -r requirements.txt   # toolkit for machine learning

python3 dataset.py
python3 train.py 50

python3 main.py test

python3 main.py detect --input=photo.jpg --output=board.jpg
python3 main.py detect --input="clayboards/IMG_1353.jpg" --output=board.jpg


For cloud run:
  gcloud builds submit --tag gcr.io/chessboard-classification/board-fitter --timeout=86399
  gcloud beta run deploy --image gcr.io/chessboard-classification/board-fitter --platform managed

## ♔ Docker ♔
https://cloud.google.com/container-registry/docs/pushing-and-pulling?hl=en_US

docker tag chess-container gcr.io/chess-ec2/chess-container
docker push gcr.io/chess-ec2/chess-container

ON EC2:
docker run -it gcr.io/chess-ec2/chess-container /bin/bash

if that doesn't work, transfer over the docker image:
  save it first locally:
    docker save -o docker_img.tar chess-container
  then transfer over:
    In the GCP Console, go to the VM Instances page.
    GO TO THE VM INSTANCES PAGE
    In the list of virtual machine instances, click SSH in the row of the instance that you want to connect to.
    SSH button next to instance name.
    After the connection is established, click the gear icon in the top right of the SSH from the Browser window and select Upload File. Alternatively, select Download File to download a file from the instance.
  then load it:
    docker load docker_img.tar


## EC2
Use the no cache dir argument to avoid all those MemoryErrors
sudo pip3 install --no-cache-dir  -r requirements.txt
sudo pip install --no-cache-dir  -U git+https://github.com/chsasank/image_features.git
<!-- sudo pip3 install --no-cache-dir  opencv-python -->
sudo pip install opencv-python-headless


## ♔ Neural Chessboard ♔

An Extremely Efficient Chess-board Detection for Non-trivial Photos

[arxiv:1708.03898](https://arxiv.org/abs/1708.03898)

![](docs/animated.gif)

> _Computer Vision! Machine learning! A E S T H E T I C!_

## Getting Started

__Dependencies Installation (macOS):__
```
$ brew install opencv3               # toolkit for computer vision
$ pip3 install -r requirements.txt   # toolkit for machine learning
```

__Dataset & Training:__
```
$ python3 dataset.py
$ python3 train.py 50
```

__Testing:__
```
$ python3 main.py test
```

__Example:__
```
$ python3 main.py detect --input=photo.jpg --output=board.jpg
```

__Producing FEN:__
> NON-PUBLIC ALGORITHM
```
$ python3 fen.py --input=board.jpg
```

__Dependencies:__

- [Python 3](https://www.python.org/downloads/)
- [Scipy 0.19.1](https://www.scipy.org/)
- [OpenCV 3](http://opencv.org/)
- [Tensorflow](https://www.tensorflow.org/) (with [tflearn](https://github.com/tflearn/tflearn) support)
- [Pyclipper](https://github.com/greginvm/pyclipper)

----

**Raw Process:**

![](docs/appendix.jpg)

**BONUS (old gif):**

![](docs/steps.gif)
