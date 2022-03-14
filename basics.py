# import keras

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from keras.models import Sequential
from tensorflow.keras import layers


#DEFINE THE NETWORK

# model = Sequential()   #define model to be sequential
# model.add(layers.Dense(2))  #Add la dense layer with 2 neurons in the model

#a small multilayer perceptron model with 2 inputs in the visible layer, 5 neurons in the hidden layer and 1 neuron in the output layer
model = Sequential()
model.add(Dense(5, input_dim=2))
model.add(layers.Activation('relu'))
model.add(Dense(1)) 
model.add(layers.Activation('sigmoid'))

#COMPILE THE MODEL
#in compiling, you specify the optimization algorithm to use to train the network, and the loss function used to evaluate the network

model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])  #sgd means stochastic gradient descent

#FIT THE NETWORK
X, y = {}
history = model.fit(X, y, batch_size=10, epochs=100, verbose=0)  #set verbose to 2 to display only the losses on each epoch, setting to zero will not display any information of epochs

#EVALUATE THE NETWORK
loss, accuracy = model.evaluate(X, y, verbose=0)

#MAKE PREDICTIONS
#After being satisfied with the performance of the model fit, we can use the model to predict on new data

predictions = model.predict(X) 

#predictions will be returned in the format provided by the output layer of the network

#creating models with functional API rather than sequential API
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
visible = Input(shape=(2,))
hidden = Dense(2)(visible)
model = Model(inputs=visible, outputs=hidden)  #got two different layers, input layer and dense layer. connect the layers to make a model using the Model function from keras

