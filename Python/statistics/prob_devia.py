import numpy as np

pup = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p = pup.mean()
print("Mean:",p)
print("Standard Deviation:",pup.std())
print("Variance:",pup.var())

np.random.choice(pup, size=(1,5),replace=True)
np.random.choice(pup,size=(1,5),replace=True).mean()

print("\n Sampling Distribution with size 5: \n")
sample_props = []
for i in range(10000):
    sample = np.random.choice(pup,5,replace=True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)

sm = sample_props.mean()
print("Mean",sm)
print("Standard Deviation:",sample_props.std())
print("Variance:",sample_props.var())

print("\n Sampling Distribution with size 20: \n")

twenty_sample_props = []
for i in range(10000):
    sample = np.random.choice(pup,20,replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

tm = twenty_sample_props.mean()
print("Mean",tm)
print("Standard Deviation:",twenty_sample_props.std())
print("Variance:",twenty_sample_props.var())