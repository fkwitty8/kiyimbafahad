"""

##
Libraries
    nampy
    tensorflow(building and training module)->deeplearning(CNN cognitionary Neural Network)
    matplotlib(scoring for module)[get dataset, train, ]
    
    ##flattening images
    ##matplotlib(image the shows validation accuracy)-->not in validation loss then good performance
    ##batchsize:number of images processed at once
    ##numclsses: number of inside a module(in crops we healthy and infected, in animals we have do)
 
    
    3.12.3, 3.11
    
    .py used for web applications
    .ipyn used visuals
    
    flattening, density, filtering->with images 
    
    
    
    
    
"""
import os
import numpy as np
import tensorflow as tf#type: ignore
from tensorflow import keras # type:ignore
from tensorflow.keras.models import sequential #type:ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten, Dense, Dropout#type:ignore
from tensorflow.
 
print("h")

#minmum 20 times epochs


def create_model(input_shape, num_classes):
    model=Sequential([
        Conv2D(32"""filter""",(3,3), activation="relu",input_shape=input_shape)
        MaxPooling2D(2,2)
        Conv2D(128"""filter""",(3,3), activation="relu")
        MaxPooling2D(2,2)
        Conv2D(256"""filter""",(3,3), activation="relu")
        
        Flatening(),#flatten features map to 1D vector
        Dropout(0.5),#dropout to 50% of the neurons to prevent overfitting
        
        
        
    ])