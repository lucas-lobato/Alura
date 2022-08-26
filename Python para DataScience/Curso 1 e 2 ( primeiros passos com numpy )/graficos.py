import matplotlib.pyplot as plt
from random import randrange

x = list(range(20))
y = []
for i in range(20):
    y.append(randrange(0,10))

plt.plot(x, y, marker = 'o')
plt.title('Notas')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()