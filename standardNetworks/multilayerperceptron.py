#Multilayer Perceptron model for binary classification

# Multilayer Perceptron
import tensorflow as tf
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from tensorflow.keras.activations import relu
from tensorflow.keras.activations import sigmoid



visible = Input(shape=(10,))
hidden1 = Dense(10, activation= relu )(visible)
hidden2 = Dense(20, activation= relu )(hidden1)
hidden3 = Dense(10, activation= relu )(hidden2)
output = Dense(1, activation= sigmoid )(hidden3)
model = Model(inputs=visible, outputs=output)
# summarize layers
model.summary()
# plot graph
# plot_model(model)