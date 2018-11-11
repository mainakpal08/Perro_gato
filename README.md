# :smiley_dog: Perro_gato :smiley_cat:
[![Python](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/)
[![nn](https://img.shields.io/badge/Powered_by-Python-blue.svg)](https://www.python.org/)
[![author](https://img.shields.io/badge/Author-Mainak-orange.svg)](https://mpalrocks.github.io/)


An image classifier that uses deep learning to detect if it is a "cat" image or a "dog" image<br/>

## Example:

### Cat image :
<img src="test1.jpg?raw=true" width="400">
- Result :
<img src="ss_cat.jpg?raw=true" width="400">
<br/>
### Dog image :
<img src="test2.jpg?raw=true" width="400">
- Result :
<img src="ss_dog.jpg?raw=true" width="400">
<br/>

## Dependancies

- Used Python Version: 3.6.0
- Install necessary modules with `sudo pip3 install -r requirements.txt` command.

## Predict an image :
You can predict an image with the exsisting trained model by-->
`python3 predict.py <ImageFileName>`

## Model Training:

To train the model-->
`python3 train.py`

## Model Architecture:
- Input Data
Shape: 64x64x3

Layer 1:
- Convolutional Layer
32 filter
Filter shape: 3x3

- Activation
Function: ReLu

- Max Pooling
Pool shape: 2x2

Layer 2:
- Convolutional Layer
32 filter
Filter shape: 3x3

- Activation
Function: ReLu

- Max Pooling
Pool shape: 2x2

Layer 3:
- Convolutional Layer
64 filter
Filter shape: 3x3

- Activation
Function: ReLu

- Max Pooling
Pool shape: 2x2

Classification:
- Flatten

- Dense
Size: 64

- Activation
Function: ReLu

- Dropout
Rate: 0.5

- Dense
Size: 2

- Activation
Function: Sigmoid

### Optimizer: Adadelta
### Loss: Binary Crossentropy

## Author

Mainak Pal ( @mpalrocks )