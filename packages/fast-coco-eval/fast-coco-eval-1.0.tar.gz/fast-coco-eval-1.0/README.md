# Fast-COCO-Eval 
This package wraps a facebook C++ implementation of COCO-eval operations found in the 
[pycocotools](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools) package.
This implementation greatly speeds up the evaluation time
for coco's AP metrics, especially when dealing with a high number of instances in an image.

### Comparison

For our use case with a test dataset of 1500 images that contains up to 2000 instances per image we saw up to a 100x faster 
evaluation using fast-coco-eval (FCE) compared to the original pycocotools code.
````
Seg eval pycocotools 4 hours 
Seg eval FCE: 2.5 min

BBox eval pycocotools: 4 hours 
BBox eval FCE: 2 min
````

# Getting started

### Install
````python
pip install fast-coco-eval
````
If you clone the repo and install it locally, the following command is recommended

````python
pip install -e .
````
given that you are in the fast-coco-eval directory. There seem to be an 
[issue](https://stackoverflow.com/questions/61004746/cannot-import-c-extension-if-in-the-package-root-directory) with 
loading the C++ extensions when installing it from the root directory without the -e flag.

## Usage

This package contains a faster implementation of the 
[pycocotools](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools) `COCOEval` class. 
Due to torch being used to compile and access the C++ code, it needs to be imported before using the package. 
To import and use `COCOeval_fast` type:

````python
import torch
from fast_coco_eval import COCOeval_fast
````

For usage, look at the original `COCOEval` [class documentation.](https://github.com/cocodataset/cocoapi)


### Dependencies

- pytorch>=1.5
- pycocotools
- pybind11
- numpy

It would be nice to decouple it from the pytorch build tool for the 
c++ compilation.

# TODOs
- [x] Wrap c++ code
- [x] Get it to compile
- [x] Add COCOEval class wraper
- [x] Remove detectron2 dependencies
- [ ] Check if it works on windows
- [ ] Remove torch dependencies

# License

Distributed under the apache version 2.0 license, see [license](LICENSE) for more information.
© 2021 Sartorius AG