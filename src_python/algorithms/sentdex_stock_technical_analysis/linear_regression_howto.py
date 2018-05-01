from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

#plt.plot(xs, ys) # line graph
#plt.scatter(xs, ys)

def create_dataset(num_datapoints, variance, step=2, correlation=False):
    xs = [i for i in range(num_datapoints)]
    
    first_y_val = 1
    ys = []
    for i in range(num_datapoints):
        y = first_y_val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation=='pos':
            first_y_val += step
        elif correlation and correlation=='neg':
            first_y_val == step
    
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

# calculate the slope using formula
# formula: m = [mean(x)mean(y) - mean(x*y)]/[mean(x)^2 - mean(x^2)]
def best_fit_slope(xs, ys):
    mean_x_mean_y = mean(xs)*mean(ys)
    xy_mean = mean(xs*ys)
    mean_x_sq = mean(xs)**2
    x_sq_mean = mean(xs**2)
    m = (mean_x_mean_y - xy_mean)/(mean_x_sq - x_sq_mean)
    return m

# calculate b, the y-intercept
def y_intercept(xs, ys, m):
    b = mean(ys) - m*mean(xs)
    return b

def lin_reg_example():
    m = best_fit_slope(xs, ys)
    print("calculated slope: ", m)
    
    b = y_intercept(xs, ys, m)
    print("calculated y-int: ", b)
    
    # generate the line
    regression_line = [((m*x)+b) for x in xs]
    plt.plot(xs, regression_line)
    
    # make prediction
    pred_x = 8
    pred_y = (m*pred_x) + b
    plt.scatter(pred_x, pred_y)

# calculate the squared error
def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

# calculate the r_squared value
def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    sq_error_reg_line = squared_error(ys_orig, ys_line) # sq er. of y_hat
    sq_error_y_mean = squared_error(ys_orig, y_mean_line)
    r_squared = 1 - (sq_error_reg_line/sq_error_y_mean)
    return r_squared

# 1 or closer to 1, the better
def r_squared_theory():
    m = best_fit_slope(xs, ys)
    print("calculated slope: ", m)
    
    b = y_intercept(xs, ys, m)
    print("calculated y-int: ", b)
    
    # generate the line
    regression_line = [((m*x)+b) for x in xs]
    plt.plot(xs, regression_line)
    
    r_squared = coefficient_of_determination(ys, regression_line)
    print("r_squared: " , r_squared)

def test_create_dataset():
    xs, ys = create_dataset(40, 40, 2, correlation='pos')
    plt.scatter(xs,ys)

def main(): 
    #r_squared_theory()
    test_create_dataset()
    plt.show()
    
if __name__ == "__main__":
    main()
