# This module was deprecated in favor of the Keras_CrossValidation module.
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

Data_Source = pd.read_csv(
    r'C:\Users\txl78\PycharmProjects\SecurityOperationsCenterRetrieval\Data\processFile\NumberEndFile.csv')
feature_cols = ['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
                'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
                'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
                'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8']
X = Data_Source[feature_cols].values
Y = Data_Source['Result'].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
# create model
model = Sequential()
model.add(Dense(12, input_dim=32, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.compile(loss="mean_squared_error", optimizer="adam", metrics=['accuracy'])
print("model summary:")
print(model.summary())
# Fit the model
model.fit(X_train, Y_train, epochs=100)
# evaluate the model
score = model.evaluate(X_test, Y_test, verbose=1)
print()
print("model metrics: {}".format(model.metrics_names))
print(model.metrics_names[0], ":", score[0])
print(model.metrics_names[1], ":", score[1])
