import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import tensorflow as tf
import math

DATA = pd.read_csv('data.csv')

ages = []
inclusive = []

# for age in DATA['Patient Age']:
#     if not math.isnan(age):
#         ages.append(age)
#     inclusive.append(age)

# print(len(ages))
# print(len(inclusive))
