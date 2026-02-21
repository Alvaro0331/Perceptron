import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

# Creacion de la figura
fig = plt.figure(figsize=(8, 6))
ax = plt.axes([0.1, 0.1, 0.6, 0.8]) # [left, bottom, width, height]
#Dibujo de ejes
ax.axhline(y=0.5, color='black', linewidth=0.7)
ax.axvline(x=0.5, color='black', linewidth=0.7)


plt.show()