import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

# Creacion de la figura
def crear_figura():
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes([0.1, 0.1, 0.6, 0.8]) # [left, bottom, width, height]
    ax.set_title("Perceptrón - Clasificación de puntos")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("X1", fontsize=12)
    ax.set_ylabel("X2", fontsize=12)
    #Dibujo de ejes
    ax.axhline(y=0, color='black', linewidth=0.7)
    ax.axvline(x=0, color='black', linewidth=0.7)
    
    return fig, ax

#Evento para agregar puntos con el mouse
def onclick(event):
    if event.inaxes:
        print(f"Clicked at: ({event.xdata:.2f}, {event.ydata:.2f})")
        

fig, ax = crear_figura()
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()