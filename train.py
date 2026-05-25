import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

network_input = np.random.rand(100, 50, 1)
network_output = np.random.rand(100, 1)

model = Sequential()

model.add(LSTM(
    256,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))

model.add(Dropout(0.2))

model.add(LSTM(256))

model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(network_input, network_output, epochs=5, batch_size=32)

model.save("music_model.h5")

print("Model Trained Successfully")
