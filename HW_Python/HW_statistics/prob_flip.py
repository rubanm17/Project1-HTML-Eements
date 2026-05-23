import scipy.stats as stats

prob1 = stats.binom.pmf(4,n=10,p=0.5)
print("prob of getting 4 heads in 10 flips:",prob1)

prob11 = 1-stats.binom.pmf(2,n=10,p=0.5)-stats.binom.pmf(3,n=10,p=0.5)-stats.binom.pmf(4,n=10,p=0.5)
print("The probability of getting at least 2-4 heads:")
print(prob11)