import scipy.stats as stats

x = 3
n = 10

prob_1 = stats.binom.pmf(x,n, 0.5)
print("Probabilty of getting 3 heads ") 
print(prob_1)

prob_2 = 1-stats.binom.pmf (0,n,0.5)-stats.binom.pmf(1,n,0.5)-stats.binom.pmf(2,n,0.5)
print("Probabilty of getting more than 2 heads is", prob_2)