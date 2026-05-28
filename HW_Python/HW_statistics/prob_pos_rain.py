import scipy.stats as stats

prob_1 = stats.poisson.pmf(12,10)
print("The prob of getting rain in 12 days is:",prob_1)

prob_2 =  stats.poisson.pmf(18,10) - stats.poisson.pmf(11,10)
print("The prob of raining on day 12 and 18  is:",prob_2)