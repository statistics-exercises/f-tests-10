import numpy as np 


def gen_samples( T, N ) :
  data = np.zeros([T,N])
  # You need to add code here to set each element of the 2D NumPy array called data 
  # to a standard normal random variable
  
  return data
  

def treatment_sum_of_squares( data ) :
  # You need to add code here to compute the treatment sum of treatment sum of squares
  # from the input 2D NumPy array called data.  This quantity should then be returned
  # from the function.
  

# This generates the data and outputs the quantity of interet
mydata = gen_samples( 10, 20 )
print("The treatment sum of squares for the generated data is", treatment_sum_of_squares( mydata ) )
