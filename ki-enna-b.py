#################
### KI-ENNA-B ###
#################

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
