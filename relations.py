def MSE(x,y,a,b):
    mse=(sum((y-(a*x+b))**2))/len(y)
    return mse

def derv_mse_a(x,y,a,b):
    return (2/len(y)) * sum(x * ((a*x + b) - y))


def derv_mse_b(x,y,a,b):
    return (2/len(y)) * sum((a*x+b)-y)

def gradient_descent(x,y,learning_rate=0.01,iterations=1000):
    a=0
    b=0
    for i in range(iterations):
        a-=learning_rate * derv_mse_a(x,y,a,b)
        b-=learning_rate * derv_mse_b(x,y,a,b)
        if i % 100 == 0:
            current_mse = MSE(x, y, a, b)
            print(f"Iteration {i}: MSE={current_mse}, a={a}, b={b}")
    return a,b

def predictions(x,y,a,b):
    for i,j in zip(x,y):
        y_pred=a*i+b
        print(f"For x={i}, predicted y={y_pred}, actual y={j}")

