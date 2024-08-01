import numpy as np

#### SECTION 1 - FUNCTION DEFINITIONS ####
# Calculate minimum b-value of loss function analytically - given in assessment paper
def analytical_min(x: np.ndarray, y: np.ndarray) -> float:
    result = np.dot(x,y) / np.linalg.norm(x) ** 2
    return(result)

# Calculate derivative of loss function at a point analyically
# dL(b)/db = 2bxTx − 2xTy (where is transpose of preceding x)
def analytical_loss_derivative(x: np.ndarray, y: np.ndarray, b: float):
    result = 2*b*np.dot(x,x) - 2*np.dot(x,y)
    return(result)

# Calculate value of loss function given x,y,b
def loss(x: np.ndarray, y: np.ndarray, b: float) -> float:
    result = np.linalg.norm(y - b * x) ** 2
    return(result)

# Estimate derivative of loss function at a point numerically
def numerical_loss_derivative(x: np.ndarray, y: np.ndarray, b: float, delta_b=1e-9):
    delta_L = loss(x,y,b+delta_b) - loss(x,y,b)
    est = delta_L / delta_b

    return(est)

# Given x,y,b and a step size, perform a single iteration of gradient descent
def gradient_step(x: np.ndarray, y: np.ndarray, step_size: float, b: float):
    result = b - step_size * analytical_loss_derivative(x,y,b)
    return(result)

# Given x,y,b, step size (e) perform a a fixed number of iterations of gradient descent and return result
def gradient_descent(x: np.ndarray, y: np.ndarray, init_b: float, step_size: float, iterations=1_000):

    b = init_b

    for _ in range(0,iterations):
        b = gradient_step(x, y, step_size, b)

    return(b)


#### SECTION 2.1 - TESTING w/ random normalized vectors ####
# Test gradient_descent() with a set of normalized random vectors
vec_len = 100
value_bound = 50
step_size = 1e-6
iterations = 1_000

random_vectors_x = [np.random.randn(vec_len) for _ in range(0,vec_len)]
random_vectors_y = [np.random.randn(vec_len) for _ in range(0,vec_len)]
init = list(np.random.randint(-value_bound, value_bound, vec_len))

print('TEST WITH RANDOM, NORMALIZED VECTORS:')
for x, y, b_init in zip(random_vectors_x, random_vectors_y, init):
    approx_min = gradient_descent(x, y, b_init, step_size, iterations=iterations)
    true_min = analytical_min(x,y)
    delta = abs(true_min - approx_min)

    step_str = 'step-size:\t\t\t\t\t{}'.format(step_size)
    iter_str = '# of descent iterations:\t{}'.format(iterations)
    grad_str = '[1] Minimum \'b\' calculated via gradient descent implementation:\t\t\t\t{}'.format(approx_min)
    analytical_min_str = '[2] Minimum \'b\' calculated via analytic equation:\t\t\t\t\t\t\t{}'.format(true_min)
    delta_str = '[3] Difference b/w numerical gradient value and analytic value of \'b\':\t\t{}\n'.format(delta)

    print(step_str)
    print(iter_str)
    print(grad_str)
    print(analytical_min_str)
    print(delta_str)
    print()


#### SECTION 2.2 - TESTING w/ pairs of normal vectors ####
# Test gradient_descent() with a set of normal random vectors
vec_len = 2
value_bound = 33
step_size = 1e-4
iterations = 1_000

# used to create one set of vectors normal to another via rotation
cw_rotation_matrix = np.array([
    [ 0, 1],
    [-1, 0]
])

normal_vectors_x = [np.random.randint(-value_bound, value_bound, 2) for _ in range(0,100)]
normal_vectors_y = [np.dot(cw_rotation_matrix, vec) for vec in normal_vectors_x]
init = list(np.random.randint(-value_bound, value_bound, 100))

print('TEST WITH RANDOM, NORMAL VECTORS:')
for x, y, b_init in zip(normal_vectors_x, normal_vectors_y, init):
    approx_min = gradient_descent(x, y, 10, step_size, iterations=iterations)
    true_min = analytical_min(x,y)
    delta = abs(true_min - approx_min)

    step_str = 'step-size:\t\t\t\t\t{}'.format(step_size)
    iter_str = '# of descent iterations:\t{}'.format(iterations)
    grad_str = '[1] Minimum \'b\' calculated via gradient descent implementation:\t\t\t\t{}'.format(approx_min)
    analytical_min_str = '[2] Minimum \'b\' calculated via analytic equation:\t\t\t\t\t\t\t{}'.format(true_min)
    delta_str = '[3] Difference b/w numerical gradient value and analytic value of \'b\':\t\t{}\n'.format(delta)

    print(step_str)
    print(iter_str)
    print(grad_str)
    print(analytical_min_str)
    print(delta_str)
    print()


# SECTION 3 - Addressing Explicit Questions of Q2
# Generally, with a smaller step-value 'e', the algorithm requires more steps to adequately 
# converge to within a given distance of an answer and is thus slower. However, results, 
# especially at each step, are also generally more accurate w/ smaller steps. Algorithm tends
# to fail when, for a fixed number of iterations, the steps are 'too small' and the initial
# guess is to far away from true value. Notably, larger step sizes also tend to trigger 
# overflow errors due to size of intermediate values involved in calculating gradient.