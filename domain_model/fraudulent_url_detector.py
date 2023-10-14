import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the model
model = tf.keras.models.load_model('domain_model/url_scanner.keras')

def predict(predict_msg):
    token = Tokenizer()
    token.fit_on_texts(predict_msg)
    padding_type='post'
    new_seq = token.texts_to_sequences(predict_msg)
    padded = pad_sequences(new_seq, maxlen =50,
                    padding = padding_type,
                    truncating='post')
    return (model.predict(padded))
    
test_string_positive=[
    "aaaalimos.com",
    "pkmadhav.net",
    "pngfp.com"
]

test_string_negative=[
    "google.com",
    "youtube.com",
    "github.com"
]
print("Positive examples:")
print(predict(test_string_positive))
print("\n\nNegative examples:")
print(predict(test_string_negative))