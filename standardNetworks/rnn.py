#A recurrent neural network
#a long short-term memory recurrent neural network for sequence
# classification. The model expects 100 time steps of one feature as input. The model has a single
# LSTM hidden layer to extract features from the sequence, followed by a fully connected layer to
# interpret the LSTM output, followed by an output layer for making binary predictions.


# Recurrent Neural Network
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers.recurrent import LSTM
from tensorflow.keras.activations import relu
from tensorflow.keras.activations import sigmoid

visible = Input(shape=(100,1))
hidden1 = LSTM(10)(visible)
hidden2 = Dense(10, activation=  relu  )(hidden1)
output = Dense(1, activation=  sigmoid  )(hidden2)
model = Model(inputs=visible, outputs=output)
# summarize layers
model.summary()
# plot graph
plot_model(model)
