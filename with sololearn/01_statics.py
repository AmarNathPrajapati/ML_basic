# numpy modules
import numpy as np;
data = [1,2,3,4,50];
print("mean: ",np.mean(data));#calculating of the mean
print("median: ",np.median(data));
print("50th percentile or median: ",np.percentile(data,50));
print("25th percentile: ",np.percentile(data,25));
print("75th percentile: ",np.percentile(data,75));
print("variance: ",np.var(data));
print("Standard deviatoin:",np.std(data));