from_future_import print_function
from keras.layers import Dense, Activation 
from keras.layers.recurrent import SimpleRNN 
from keras.models import Sequential
from keras.utils.visualize_util import plot 
import numpy as np

fin = open("../data/alice_in_wonderland.txt", 'rb') 
lines = []
for line in fin:
	line = line.strip().lower()
	line = line.decode("ascii", "ignore") 
	if len(line) == O:
		continue 
	lines.append(line)
fin.close()
text = " ".join(lines)

chars = set([c for c in text]) 
nb_chars = len(chars)
char2index = dict((c, i) for i, c in enumerate(chars)) 
index2char = dict((i, c) for i, c in enumerate(chars))

SEQLEN = lO STEP = l

input_chars = [] label_chars = []
for i in range(O, len(text) – SEQLEN, STEP): 
	input_chars.append(text[i:i + SEQLEN]) 
	label_chars.append(text[i + SEQLEN])
X = np.zeros((len(input_chars), SEQLEN, nb_chars), dtype=np.bool) 
y = np.zeros((len(input_chars), nb_chars), dtype=np.bool)
for i, input_char in enumerate(input_chars): 
	for j, ch in enumerate(input_char):
		X[i, j, char2index[ch]] = l
	y[i, char2index[label_chars[i]]] = l
	
HIDDEN_SIZE = l28 
BATCH_SIZE = l28 
NUM_ITERATIONS = 25
NUM_EPOCHS_PER_ITERATION = l 
NUM_PREDS_PER_EPOCH = lOO

model = Sequential()
model.add(SimpleRNN(HIDDEN_SIZE, return_sequences=False, 
	input_shape=(SEQLEN, nb_chars),
	unroll=True)) model.add(Dense(nb_chars)) 
model.add(Activation("softmax"))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

for iteration in range(NUM_ITERATIONS): print("=" * 5O)
print("Iteration #: %d" % (iteration))
model.fit(X, y, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS_PER_ITERATION)

test_idx = np.random.randint(len(input_chars)) 
test_chars = input_chars[test_idx] 
print("Generating from seed: %s" % (test_chars)) 
print(test_chars, end="")
for i in range(NUM_PREDS_PER_EPOCH):
	Xtest = np.zeros((l, SEQLEN, nb_chars)) 
	for i, ch in enumerate(test_chars):
		Xtest[O, i, char2index[ch]] = l
	pred = model.predict(Xtest, verbose=O)[O] 
	ypred = index2char[np.argmax(pred)] 
	print(ypred, end="")
	# move forward with test_chars + ypred 
	test_chars = test_chars[l:] + ypred
print()






