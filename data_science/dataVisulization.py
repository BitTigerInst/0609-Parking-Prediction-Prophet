import matplotlib.pyplot as plt

'''read csv train'''
import pandas as pd
data = pd.read_csv("train.csv")

'''plot as hisotgram'''
plt.figure(figsize=(12,9))
ax = plt.subplot(111)

plt.hist(list(data['occupancy']),bins=100)
