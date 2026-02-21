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

#Creacion de los widgets
def crear_widgets(fig):
    # TextBoxes para los pesos
    w0Box=widgets.TextBox(plt.axes([0.75, 0.8, 0.1, 0.05]), 'w0', initial='1')
    w1Box=widgets.TextBox(plt.axes([0.75, 0.7, 0.1, 0.05]), 'w1', initial='1')
    w2Box=widgets.TextBox(plt.axes([0.75, 0.6, 0.1, 0.05]), 'w2', initial='-1.5')
    # Botones
    plotButton=widgets.Button(plt.axes([0.75, 0.3, 0.1, 0.15]), 'Plot', color='lightblue', hovercolor='skyblue')
    clearButton=widgets.Button(plt.axes([0.75, 0.1, 0.1, 0.05]), 'Clear', color='lightcoral', hovercolor='salmon')

    return w0Box, w1Box, w2Box, plotButton, clearButton

#Evento para agregar puntos con el mouse
puntos = []  # Lista para almacenar los puntos clickeados

def onclick(event):
    if event.inaxes == ax:
        x, y = event.xdata, event.ydata
        ax.plot(x, y, 'ro')  # Dibuja un punto rojo en la posición clickeada
        puntos.append((x, y))  # Agrega el punto a la lista de puntos
        fig.canvas.draw()  # Actualiza la figura para mostrar el nuevo punto
        print(f"Current points: {puntos}")

fig, ax = crear_figura()
w0Box, w1Box, w2Box, plotButton, clearButton = crear_widgets(fig)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()