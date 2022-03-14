#A convolutional neural network
#The model
# receives black and white 64 x 64 images as input, then has a sequence of two convolutional and
# pooling layers as feature extractors, followed by a fully connected layer to interpret the features
# and an output layer with a sigmoid activation for two-class predictions.

# Convolutional Neural Network
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from tensorflow.keras.activations import relu
from tensorflow.keras.activations import sigmoid

visible = Input(shape=(64,64,1))
conv1 = Conv2D(32, kernel_size=4, activation=  relu  )(visible)
pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
conv2 = Conv2D(16, kernel_size=4, activation=  relu  )(pool1)
pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
hidden1 = Dense(10, activation=  relu  )(pool2)
output = Dense(1, activation=  sigmoid  )(hidden1)
model = Model(inputs=visible, outputs=output)
# summarize layers

model.summary()
# plot graph
plot_model(model)