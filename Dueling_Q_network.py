import tensorflow as tf
import tensorflow.keras as keras
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np


class Dueling_Q_network(keras.Model):
    def __init__(self):
        super(Dueling_Q_network, self).__init__()
        self.dens1 = keras.layers.Dense(128, activation='relu')
        self.dens2 = keras.layers.Dense(128, activation='relu')
        self.V = keras.layers.Dense(1, activation=None)
        self.A = keras.layers.Dense(5, activation=None)

    def call(self, state):
        x = self.dens1(state)
        x = self.dens2(x)
        V = self.V(x)
        A = self.A(x)

        Q = (V + (A - tf.math.reduce_mean(A, axis=1, keepdims=True)))

        return Q
