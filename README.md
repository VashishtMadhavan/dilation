# Multi-Scale Context Aggregation by Dilated Convolutions

## Introduction

Properties of dilated convolution are discussed in the [arXiv report](http://arxiv.org/abs/1511.07122) under ICLR 2016 review. It can be used for semantic image segmentation and learning context information. This repo releases the network definition discussed in the report and the trained models.

If you find the code or model useful in your research, please consider citing:
```
@article{yu2015multi,
  title   = {Multi-Scale Context Aggregation by Dilated Convolutions},
  author  = {Yu, Fisher and Koltun, Vladlen},
  journal = {arXiv preprint arXiv:1511.07122},
  year    = {2015}
}
```

## Installation
### Caffe

Install [Caffe](https://github.com/BVLC/caffe) and its Python interface. Make sure Caffe version is newer than commit [08c5df](https://github.com/BVLC/caffe/commit/08c5dfd53e6fd98148d6ce21e590407e38055984).

### Python

The companion Python script is used to demo the network definition and trained weights.

The required Python packages are numba numpy opencv. Python release from Anaconda is recommended. 

In the case of using Anaconda
```
conda install numba numpy opencv
```

## Running Demo

* Clone the code from Github	
   
    ```
    git clone git@github.com:fyu/dilation.git
    cd dilation
    ```
* Download pretrained network

    ```
    sh pretrained/download.sh
    ```
* Run front end model on GPU 0
    
    ```
    python predict.py images/dog.jpg --gpu 0
    ```
    The results is saved as images/dog_front.png.
* Run front end mode together with context module on GPU 0
    
    ```
    python predict.py images/dog.jpg --context 1 --gpu 0
    ```
    The results is saved as images/dog_context.png.