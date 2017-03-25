# Matrix Algebra
import numpy as np

A = [[1, 2, 3], [2, 7, 4]]
B = [[1, -1], [0, 1]]
C = [[5, -1], [9, 1], [6, 0]]
D = [[3, -2, -1], [1, 2, 3]]
u = [6, 2, -3, 5]
v = [3, 5, -1, 4]
w = [[1], [8], [0], [5]]

A = np.array(A)
B = np.array(B)
C = np.array(C)
D = np.array(D)
u = np.array(u)
v = np.array(v)
w = np.array(w)
alpha = 6

# print(A)
# print(B)
# print(C)
# print(u)
# print(v)
# print(w)

# 2.1
ans2_1 = u + v
print(ans2_1)
print('')

# 2.2
ans2_2 = u - v
print(ans2_2)
print('')

# 2.3
ans2_3 = alpha * u
print(ans2_3)
print('')

# 2.4
ans2_4 = u.dot(v)
print(ans2_4)
print('')

# 2.5
ans2_5 = np.linalg.norm(u)
print(ans2_5)
print('')

# 3.1 - undefined
# ans3_1 = A + C
# print(ans3_1)
# print('')

# 3.2
ans3_2 = A-C.transpose()
print(ans3_2)
print('')

# 3.3
ans3_3 = C.transpose() + 3 * D
print(ans3_3)
print('')

# 3.4
ans3_4 = B.dot(A)
print(ans3_4)
print('')

# 3.5
# ans3_5 = B.dot(A.transpose())
# print(ans3_5)
# print('')

# 3.6
# ans3_6 = B.dot(C)
# print(ans3_6)
# print('')

# 3.7
ans3_7 = C.dot(B)
print(ans3_7)
print('')

# 3.8
ans3_8 = B.dot(B.dot(B.dot(B)))
print(ans3_8)
print('')

# 3.9
ans3_9 = A.dot(A.transpose())
print(ans3_9)
print('')

# 3.10
ans3_10 = D.transpose().dot(D)
print(ans3_10)
print('')



