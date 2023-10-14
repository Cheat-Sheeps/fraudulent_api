import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the model
model = tf.keras.models.load_model('ai_model/phishing_detection.keras')

class FraudulentWebsiteDetector:
    def predict(self, predict_msg):
        token = Tokenizer()
        token.fit_on_texts(predict_msg)
        padding_type='post'
        new_seq = token.texts_to_sequences(predict_msg)
        padded = pad_sequences(new_seq, maxlen =50,
                        padding = padding_type,
                        truncating='post')
        return (model.predict(padded))
    
    def test(self):
        test_string_positive=[
            "Your account has been compromised. Please click on the link to reset your password.",
            "You have won a free trip to Hawaii! Click here to claim your prize.",
            "Your bank account has been locked. Please click on the link to unlock it.",
            "Your account has been suspended. Please click on the link to reactivate it.",
            "Your email account has been hacked. Please click on the link to secure it.",
            "You have been selected for a job interview. Click here to confirm your attendance.",
            "Your credit card has been charged for an unauthorized purchase. Click here to dispute the charge.",
            "Your subscription has expired. Please click on the link to renew it.",
            "You have received a new voicemail message. Click here to listen to it.",
            "Your account has been flagged for suspicious activity. Please click on the link to verify your identity."
        ]

        test_string_negative=[
            "I'm looking forward to seeing you tomorrow.",
            "The weather is beautiful today.",
            "I'm sorry, I can't make it to the meeting.",
            "I'm going to the gym after work.",
            "What time is the movie tonight?",
            "I'm running late. Can we reschedule?",
            "I'm excited to try the new restaurant in town.",
            "I'm going to the park this weekend.",
            "I'm taking a break from work next week.",
            "What are your plans for the weekend?"
        ]
        print("Positive examples:")
        print(FraudulentWebsiteDetector.predict(test_string_positive))
        print("\n\nNegative examples:")
        print(FraudulentWebsiteDetector.predict(test_string_negative))