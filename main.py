# the purpose of this exercise , is to explore the possibilities of finding the most specific and most general
# hypothesis
import numpy as np

x = np.array([['Sunny', 'Warm', 'Normal', 'String', 'Warm', 'Same', 'Yes'],
              ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
              ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
              ['Sunny', 'Warm', 'High', 'Strong', 'Cool','Change','Yes']])
r, c = x.shape
print('The number of rows and columns are:', r, 'and', c - 1)
print("The dataset is : \n", x)
s = []
s = np.empty(c - 1, dtype=object)
for i in range(c - 1):
    s[i] = "\u03A6"
print("\n Most specific hypothesis : \n", s)

for i in range(c - 1):
    s[i] = x[0, i]

for i in range(1, r):
    if x[i, c - 1] == 'No':
        continue
    else:
        for j in range(c - 1):
            if x[i, j] != s[j]:
                s[j] = '?'
print("\n Final hypothesis: \n", s)
