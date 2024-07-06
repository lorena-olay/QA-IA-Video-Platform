#Este script prueba una simple red neuronal que predice valores en función de una entrada.

import unittest
import tensorflow as tf
import numpy as np

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),
        tf.keras.layers.Dense(units=1)
    ])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    return model

class TestAlgorithms(unittest.TestCase):
    def test_prediction(self):
        model = create_model()
        input_data = np.array([[10.0]])
        prediction = model.predict(input_data)
        self.assertIsNotNone(prediction)

if __name__ == '__main__':
    unittest.main()
