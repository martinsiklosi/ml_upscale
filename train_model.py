import tensorflow as tf
from tensorflow import keras
# import numpy as np
import json
from settings import *

with open("data.json", "r") as infile:
    in_data, out_data = json.load(infile)

# in_data, out_data = np.asarray(in_data), np.asarray(out_data)

cutoff = round(len(in_data)*TRAINING_RATIO)
train_in_data, train_out_data = in_data[:cutoff], in_data[:cutoff]
test_in_data, test_out_data = in_data[cutoff:], in_data[cutoff:]

# setup model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(IN_SIZE, IN_SIZE)),
    keras.layers.Dense(1024, activation=tf.nn.relu),
    keras.layers.Dense(1024, activation=tf.nn.relu),
    keras.layers.Dense(OUT_SIZE**2, activation=tf.nn.relu),
    keras.layers.Reshape((OUT_SIZE, OUT_SIZE))
])

model.compile(
    optimizer=tf.optimizers.Adam(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# train model
model.fit(train_in_data, train_out_data, epochs=EPOCHS)

# save model
model.save('model')
