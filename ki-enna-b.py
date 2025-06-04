#################
### KI-ENNA-B ###
#################

####################
# (1) VORTRAINIERT #
####################

# Setup
import math

# ReLU
def relu(x):
    y = []
    for i in range(len(x)):
        if x[i] >= 0:
            y.append(x[i])
        else:
            y.append(0)
    return y

# Leaky ReLU
def leaky_relu(x, alpha=0.01):
    p = []
    for i in range(len(x)):
        if x[i] >= 0:
            p.append(x[i])
        else:
            p.append(alpha * x[i])
    return p

# Tanh
def tanh(x):
    t = [(math.exp(x[val]) - math.exp(-x[val])) / (math.exp(x[val]) + math.exp(-x[val])) for val in range(len(x))]
    return t

# Sigmoid
def sigmoid(x):
    z = [1 / (1 + math.exp(-x[val])) for val in range(len(x))]
    return z

# Softmax
def softmax(x):
    max_x = max(x[val])
    exp_x = [math.exp(val - max_x) for val in range(len(x))]
    sum_exp_x = sum(exp_x)
    s = [j / sum_exp_x for j in exp_x]
    return s

# Single Neuron
def neuron(x, w, b, activation):

    tmp = zero_dim(x[0])

    for i in range(len(x)):
        tmp = add_dim(tmp, [(float(w[i]) * float(x[i][j])) for j in range(len(x[0]))])

    if activation == "sigmoid":
        yp = sigmoid([tmp[i] + b for i in range(len(tmp))])
    elif activation == "relu":
        yp = relu([tmp[i] + b for i in range(len(tmp))])
    elif activation == "leaky_relu":
        yp = relu([tmp[i] + b for i in range(len(tmp))])
    elif activation == "tanh":
        yp = tanh([tmp[i] + b for i in range(len(tmp))])
    elif activation == "softmax":
        yp = tanh([tmp[i] + b for i in range(len(tmp))])
    else:
        print("Function unknown!")

    return yp

# Mathematical Basics - I
def zero_dim(x):
    z = [0 for i in range(len(x))]
    return z

# Mathematical Basics - II
def add_dim(x, y):
    z = [x[i] + y[i] for i in range(len(x))]
    return z

# Mathematical Basics - III
def zeros(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M

# Mathematical Basics - IV
def transpose(M):
    if not isinstance(M[0], list):
        M = [M]
    rows = len(M)
    cols = len(M[0])
    MT = zeros(cols, rows)
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
    return MT

# Mathematical Basics - V
def print_matrix(M, decimals=3):
    for row in M:
        print([round(x, decimals) + 0 for x in row])

# Mathematical Basics - VI
def dense(nunit, x, w, b, activation):
    res = []
    for i in range(nunit):
        z = neuron(x, w[i], b[i], activation)
        res.append(z)
    return res

# Include Parameters from TensorFlow
w1 = [[-0.75323504, -0.25906014],
      [-0.46379513, -0.5019245 ],
      [ 2.1273055 ,  1.7724446 ],
      [ 1.1853403 ,  0.88468695]]
b1 = [0.53405946, 0.32578036]
w2 = [[-1.6785783,  2.0158117,  1.2769054],
      [-1.4055765,  0.6828738,  1.5902631]]
b2 = [ 1.18362  , -1.1555661, -1.0966455]
w3 = [[ 0.729278  , -1.0240695 ],
      [-0.80972326,  1.4383037 ],
      [-0.90892404,  1.6760625 ]]
b3 = [0.10695826, 0.01635581]
w4 = [[-0.2019448],
      [ 1.5772797]]
b4 = [-1.2177287]

# Transpose
w1 = transpose(w1)
w2 = transpose(w2)
w3 = transpose(w3)
w4 = transpose(w4)

# Standardized Dataset
Xtest = [[ 0.81575475, -0.21746808, -0.12904165, -0.65303909],
         [ 0.05761837,  1.59476592,  0.84485761,  1.71304456],
         [ 0.96738203,  0.68864892, -0.00730424, -0.41643072],
         [ 2.02877297,  0.38660992,  2.06223168,  1.00321947],
         [ 1.42226386,  0.99068792,  1.33180724,  0.29339437],
         [ 0.81575475,  0.99068792,  1.21006983,  1.4764362 ],
         [-1.00377258,  0.38660992, -0.49425387, -0.41643072],
         [ 0.05761837, -0.51950708, -0.00730424,  0.29339437],
         [ 0.36087292,  0.38660992,  1.08833242,  1.23982783],
         [ 0.66412748,  0.38660992,  0.35790798,  1.4764362 ],
         [ 0.05761837,  0.08457092,  0.84485761,  0.29339437],
         [-0.70051802, -0.51950708,  0.23617057,  0.53000274],
         [ 0.20924564, -0.21746808,  0.84485761,  1.00321947],
         [-0.24563619,  0.08457092, -0.25077906, -0.65303909],
         [-2.06516352, -1.42562408, -1.95510276, -1.59947255],
         [-1.15539985, -1.42562408, -1.34641572, -1.36286418],
         [ 0.05761837, -1.12358508, -0.00730424, -0.41643072],
         [ 0.20924564,  0.08457092, -0.73772869, -0.88964745],
         [-0.39726347, -0.51950708,  0.23617057, -0.17982236],
         [ 0.5125002 ,  0.08457092, -0.37251647, -0.88964745]]

ytrue = [0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0]
print(len(ytrue))

# Neural Network Architecture
yout1 = dense(2, transpose(Xtest), w1, b1, 'relu') # input layer (2 neurons)
yout2 = dense(3, yout1, w2, b2, 'sigmoid') # hidden layer (3 neurons)
yout3 = dense(2, yout2, w3, b3, 'relu') # hidden layer (2 neurons)
ypred = dense(1, yout3, w4, b4,'sigmoid') # output layer (1 neuron)
print(ypred)

# Confusion Matrix Basics
def classification_report(ytrue, ypred):
    TP = TN = FP = FN = 0
    
    for true, pred in zip(ytrue, ypred):
        if true == pred:
            if true == 1:
                TP += 1
            else:
                TN += 1
        else:
            if true == 1:
                FN += 1
            else:
                FP += 1

    accuracy = (TP + TN) / len(ytrue)
    conf_matrix = [[TN, FP], [FN, TP]]

    print("Accuracy: " + str(accuracy))
    print("Confusion Matrix:")
    print(print_matrix(conf_matrix))

# Confusion Matrix
ypred_class = [1 if i > 0.5 else 0 for i in ypred[0]]
print(ypred_class)
print(classification_report(ytrue,ypred_class))

#####################
# (2) SELBSTLERNEND #
#####################

# Libraries
import random
import math

# Standardized Dataset
Xtest = [[ 0.81575475, -0.21746808, -0.12904165, -0.65303909],
         [ 0.05761837,  1.59476592,  0.84485761,  1.71304456],
         [ 0.96738203,  0.68864892, -0.00730424, -0.41643072],
         [ 2.02877297,  0.38660992,  2.06223168,  1.00321947],
         [ 1.42226386,  0.99068792,  1.33180724,  0.29339437],
         [ 0.81575475,  0.99068792,  1.21006983,  1.4764362 ],
         [-1.00377258,  0.38660992, -0.49425387, -0.41643072],
         [ 0.05761837, -0.51950708, -0.00730424,  0.29339437],
         [ 0.36087292,  0.38660992,  1.08833242,  1.23982783],
         [ 0.66412748,  0.38660992,  0.35790798,  1.4764362 ],
         [ 0.05761837,  0.08457092,  0.84485761,  0.29339437],
         [-0.70051802, -0.51950708,  0.23617057,  0.53000274],
         [ 0.20924564, -0.21746808,  0.84485761,  1.00321947],
         [-0.24563619,  0.08457092, -0.25077906, -0.65303909],
         [-2.06516352, -1.42562408, -1.95510276, -1.59947255],
         [-1.15539985, -1.42562408, -1.34641572, -1.36286418],
         [ 0.05761837, -1.12358508, -0.00730424, -0.41643072],
         [ 0.20924564,  0.08457092, -0.73772869, -0.88964745],
         [-0.39726347, -0.51950708,  0.23617057, -0.17982236],
         [ 0.5125002 ,  0.08457092, -0.37251647, -0.88964745]]

ytrue = [0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0]

# Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivate of Sigmoid
def sigmoid_derivative(output):
    return output * (1 - output)

# ReLU
def relu(x):
    return max(0, x)

# Derivate of ReLU
def relu_derivative(output):
    return 1 if output > 0 else 0

# Forward Propagation
def dense_forward(inputs, weights, biases, activation='relu'):
    outputs = []
    pre_activations = []
    for w, b in zip(weights, biases):
        z = sum(i*w_ij for i, w_ij in zip(inputs, w)) + b
        pre_activations.append(z)
        if activation == 'sigmoid':
            outputs.append(sigmoid(z))
        elif activation == 'relu':
            outputs.append(relu(z))
        else:
            raise Exception("Unknown activation")
    return outputs, pre_activations

# Backward Propagation
def dense_backward(inputs, grad_outputs, outputs, pre_activations, weights, biases, activation='relu', lr=0.01):
    input_grads = [0.0 for _ in range(len(inputs))]
    for j in range(len(weights)):
        if activation == 'sigmoid':
            delta = grad_outputs[j] * sigmoid_derivative(outputs[j])
        elif activation == 'relu':
            delta = grad_outputs[j] * relu_derivative(pre_activations[j])
        else:
            raise Exception("Unknown activation")
        for i in range(len(inputs)):
            input_grads[i] += weights[j][i] * delta
            weights[j][i] -= lr * delta * inputs[i]
        biases[j] -= lr * delta
    return input_grads

# Loss Function
def binary_cross_entropy(predicted, target):
    epsilon = 1e-7
    return - (target * math.log(predicted + epsilon) + (1 - target) * math.log(1 - predicted + epsilon))

def binary_cross_entropy_derivative(predicted, target):
    epsilon = 1e-7
    return -(target / (predicted + epsilon)) + (1 - target) / (1 - predicted + epsilon)

# Function for Initializing Weights and Biases
def init_layer(input_size, output_size):
    weights = [[random.uniform(-0.5, 0.5) for _ in range(input_size)] for _ in range(output_size)]
    biases = [random.uniform(-0.5, 0.5) for _ in range(output_size)]
    return weights, biases

# Initialize Weights and Biases
w1, b1 = init_layer(4, 3)
w2, b2 = init_layer(3, 1)

# Epochs and Learning Rate for Training
epochs = 100
lr = 0.05

for epoch in range(epochs):
    total_loss = 0
    for xi, yi in zip(X, y):
        # Forward Pass
        out1, pre1 = dense_forward(xi, w1, b1, 'relu')
        out2, pre2 = dense_forward(out1, w2, b2, 'sigmoid')
        loss = binary_cross_entropy(out2[0], yi)
        total_loss += loss

        # Backward Pass
        dL_dout2 = [binary_cross_entropy_derivative(out2[0], yi)]
        dL_dout1 = dense_backward(out1, dL_dout2, out2, pre2, w2, b2, 'sigmoid', lr)
        _ = dense_backward(xi, dL_dout1, out1, pre1, w1, b1, 'relu', lr)

    if epoch % 10 == 0 or epoch == epochs - 1:
        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

# Prediction
def predict(x):
    out1, _ = dense_forward(x, w1, b1, 'relu')
    out2, _ = dense_forward(out1, w2, b2, 'sigmoid')
    return 1 if out2[0] > 0.5 else 0

ypred = [predict(xi) for xi in X]

# Confusion Matrix
def classification_report(ytrue, ypred):
    TP = TN = FP = FN = 0
    for true, pred in zip(ytrue, ypred):
        if true == pred:
            if true == 1:
                TP += 1
            else:
                TN += 1
        else:
            if true == 1:
                FN += 1
            else:
                FP += 1
    accuracy = (TP + TN) / len(ytrue)
    print("Accuracy: {:.3f}".format(accuracy))
    print("Confusion Matrix:")
    print("TN: {}, FP: {}".format(TN, FP))
    print("FN: {}, TP: {}".format(FN, TP))

# Generate predictions
ypred = [predict(xi) for xi in X]

# Show classification metrics
classification_report(y, ypred)
