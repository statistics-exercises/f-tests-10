import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_gen_samples(self) :
        ddd = gen_samples( 10,5 )
        lll, uuu = scipy.stats.norm.ppf(0.005), scipy.stats.norm.ppf(0.995)
        for i in range(10) : 
            for j in range(5) : self.assertTrue( lll<ddd[i,j] and ddd[i,j]<uuu, "Your code to generate the matrix of samples is not correct.  I test this function by performing a hypothesis test with a 1% significance limit.  There is thus a small probability that this test fails even when the code is correct." )
            
    def test_treatment_sum_of_squares(self) : 
        ddd, mu = gen_samples( 10, 20 ), np.zeros( 10 )
        for i in range(10) : mu[i] = sum( ddd[i,:] ) / len( ddd[i,:] )
        fmu, t = sum(mu) / len(mu), 0 
        for i in range(10) : t = t + 20*(mu[i] - fmu)*(mu[i] - fmu)
        self.assertTrue( np.abs( t - treatment_sum_of_squares(ddd) )<1e-7, "Your code for calculating the treatment sum of squares is not correct" )
        
    def test_treatment_sum_of_squares2(self) :
        ddd, mu = gen_samples( 10, 20 ), np.zeros( 10 )
        for i in range(10) : mu[i] = sum( ddd[i,:] ) / len( ddd[i,:] )
        fmu, t = sum(mu) / len(mu), 0 
        for i in range(10) : t = t + (mu[i] - fmu)*(mu[i] - fmu)
        self.assertFalse( np.abs( t - treatment_sum_of_squares(ddd) )<1e-7, "Your code for calculating the treatment sum of squares is not correct.  The expression is not simply the sum of the squares of the difference from the means.  You need multiply the square of the difference from the mean by the number of variables from which each mean was calculated." )
    
