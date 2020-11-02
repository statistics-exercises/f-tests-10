# The treatment sum of squares

We will now consider the other important quantity that we need in order to calculate the statistic that we will use to solve the farmer's problem that was introduced in the previous but one task.  This quantity is called the treatment sum of squares (![](https://render.githubusercontent.com/render/math?math=SS_T)).  Once again we will assume that we have t samples the jth of which contains ![](https://render.githubusercontent.com/render/math?math=n_j) data points.  The treatment sum of squares is defined as:

![](https://render.githubusercontent.com/render/math?math=SS_T=\sum_{j=1}^t\sum_{i=1}^{n_j}(\overline{X}_j-\overline{X})^2\qquad\textrm{where}\qquad\overline{X}_j=\frac{1}{n_j}\sum_{i=1}^{n_j}X_i\qquad\textrm{and}\qquad\overline{X}=\frac{1}{t}\sum_{=1}^t\overline{X}_j)

In these expressions, ![](https://render.githubusercontent.com/render/math?math=X_i) is just a random variable.  ![](https://render.githubusercontent.com/render/math?math=\overline{X_j}) is thus a sample mean that has been computed using the ![](https://render.githubusercontent.com/render/math?math=n_j) data points in the jth sample.  ![](https://render.githubusercontent.com/render/math?math=\overline{X}), meanwhile, is a sample mean that has been computed using the data in all T samples.  

__To complete this task I would like you to write code to compute the treatment sum of squares.   I would also like you to write a function to generate a data set for which we will compute the treatment sum of squares as this will prepare you for what we are going to do in the next few tasks.__  In practice completing this task will involve completing the following functions:

1. `gen_samples` - this function generates the data for which the treatment sum of squares will be computed.  It takes two input arguments `T` and `N`.  `T` is the number of samples of size `N` that you would like to take.  The output from this function is thus a 2D NumPy array called `data`, which has `T` rows and `N` columns.  Each element in this array should be a standard normal random variable.

2. `treatment_sum_of_squares` - this function takes a 2D NumPy array called `data` in input.  Within the function, you should add code to calculate and return the treatment sum of squares using the formula above.

Once you have completed this function and run the code a data set will be output. The treatment sum of squares for this data set will then be output.
