# SYSU_MM01_pythoneval
(Re-)implementation of evaluation code for SYSU_MM01 dataset in python

The code is a python translation of the Matlab-code provided by SYSU-MM01 dataset authors <a href="https://github.com/wuancong/SYSU-MM01" target="_blank">here</a>.

## Dataset download

Baiduyun: http://pan.baidu.com/s/1gfIlcmZ

Dropbox: https://www.dropbox.com/sh/v036mg1q4yg7awb/AABhxU-FJ4X2oyq7-Ts6bgD0a?dl=0

Please refer the <a href="https://github.com/wuancong/SYSU-MM01" target="_blank">readme</a> file of original Matlab version of evaluation code for more information about the dataset and evaluation  protocol.

## Usage

As per original protocol, the feature vectors are to be stored in `.mat` files for each camera in a particular directory.
Then you can run the evaluation to get the performance numbers. 

check the file `src/evaluate_SYSU_MM01.py` to locate the function call for evaluation.

```
evaluate_results(feature_dir, prefix, mode, number_shot, total_runs=10)

# feature_dir = the directory path where the camera based features are stored
# prefix = prefix of the files or model name
# mode = all | indoor
# number_shot = 1 = single-shot | 10 = multi-shot
# total_runs = number of test iterations to run (usually 10, as given in the original paper)
```

## Citation

You can cite the original paper from Wu et al., if you use the dataset.

```
Ancong Wu, Wei-Shi Zheng, Hong-Xing Yu, Shaogang Gong and Jianhuang Lai. RGB-Infrared Cross-Modality Person Re-Identification. IEEE International Conference on Computer Vision (ICCV), 2017.
```