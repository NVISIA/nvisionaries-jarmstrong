# NV-Faceswap

A categorical face-swapping implementation coupled with a bolt-on classifier.

## Important note

The version of TensorFlow included in this Docker image is CPU-only. The image is tuned for OpenCV and dlib, which are compiled for GPU usage. The only reason TensorFlow is here is to load images and hand them off to the classifier, which uses a GPU-bound TensorFlow build.
