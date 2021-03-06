from __future__ import print_function
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils

np.random.seed(1671)  # 재현을 위한 설정

# 네트워크와 학습 설정
NB_EPOCH = 200
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10   # 출력 범주 = 숫자의 종류 0~9
OPTIMIZER = SGD() # SGD 옵티마이저, 이 장 후반부에서 설명
N_HIDDEN = 128
VALIDATION_SPLIT=0.2 # 학습 데이터 중에 얼마나 검증 데이터로 할당할지 지정

# 데이터 : 무작위로 섞고, 학습 데이터와 테스트 데이터로 나눔
#
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# X_train은 60000 개의 행으로 구성되고 28x28 개의 값을 갖음 --> 60000 x 784 형태로 변환
RESHAPED = 784
#
X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# 정규화
#
X_train /= 255
X_test /= 255
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# 범주 벡터를 이진 범주 행렬로 변환
Y_train = np_utils.to_categorical(y_train, NB_CLASSES)
Y_test = np_utils.to_categorical(y_test, NB_CLASSES)

# 10 개의 출력
# 최종 단계는 소프트맥스

model = Sequential()
model.add(Dense(NB_CLASSES, input_shape=(RESHAPED,)))
model.add(Activation('softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=OPTIMIZER,
              metrics=['accuracy'])

history = model.fit(X_train, Y_train,
                    batch_size=BATCH_SIZE, epochs=NB_EPOCH,
                    verbose=VERBOSE, validation_split=VALIDATION_SPLIT)
score = model.evaluate(X_test, Y_test, verbose=VERBOSE)
print("\nTest score:", score[0])
print('Test accuracy:', score[1])
