import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

data = pd.read_csv('domain_model/dataset_phishing1.csv')

legit_urls = data[data.status =='legitimate']
phishing_urls = data[data.status=='phishing']
legit_urls=legit_urls.sample(n=len(phishing_urls),random_state=42)
balanced_data = pd.concat([legit_urls,phishing_urls])
balanced_data['label']=balanced_data['status'].map({'legitimate':0,'phishing':1})

train_msg, test_msg, train_labels, test_labels =train_test_split(balanced_data['domain'],balanced_data['label'],test_size=0.2,random_state=434)

vocab_size=500
oov_tok='<OOV>'
max_len=50

#preprocessing making tokens out of text
token=Tokenizer(num_words=vocab_size,oov_token=oov_tok)
token.fit_on_texts(train_msg)

padding_type='post'
truncate_type='post'
Trainning_seq=token.texts_to_sequences(train_msg)
Trainning_pad=pad_sequences(Trainning_seq,maxlen=50,padding=padding_type,truncating=truncate_type)

Testing_seq=token.texts_to_sequences(test_msg)
Testing_pad=pad_sequences(Testing_seq,maxlen=50,padding=padding_type,truncating=truncate_type)

model=tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size,64,input_length=max_len),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.summary()

num_epochs=20
history=model.fit(Trainning_pad,train_labels,epochs=num_epochs,validation_data=(Testing_pad,test_labels),verbose=2)
model.save('domain_model/url_scanner.keras')

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')

plt.show(block=True)