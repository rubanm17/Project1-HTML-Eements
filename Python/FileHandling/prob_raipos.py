import scipy.stats as stats

prob_1 = stats.poisson.pmf(6,10)
print("The prob of getting rain in 6 days is:",prob_1)

prob_2 =  stats.poisson.cdf(12,10) + stats.poisson.pmf(13,10) + stats.poisson.pmf(14,10)
print("The prob of raining for 12-14 days is:",prob_2)