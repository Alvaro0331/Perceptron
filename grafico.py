import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import perceptron as p
import numpy as np

# Creacion de la figura
def crear_figura():
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes([0.1, 0.1, 0.6, 0.8]) # [left, bottom, width, height]
    ax.set_title("Perceptrón - Clasificación de puntos")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("X2", fontsize=12)
    ax.set_ylabel("X1", fontsize=12)
    #Dibujo de ejes
    ax.axhline(y=0, color='black', linewidth=0.7)
    ax.axvline(x=0, color='black', linewidth=0.7)
    
    #Leyenda
    leyenda = [
        plt.Line2D([0], [0], marker='o', color='w', label='Clase 0', markerfacecolor='blue', markersize=8),
        plt.Line2D([0], [0], marker='o', color='w', label='Clase 1', markerfacecolor='red', markersize=8),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=8, label='Sin clasificar'),
        plt.Line2D([0], [0], linestyle='--', color='green', label='Frontera'),
    ]
    ax.legend(handles=leyenda, loc='upper right', fontsize=8)
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
markers = [] # Lista para almacenar los objetos de los puntos dibujados
lineas = [] # Lista para almacenar la línea dibujada
def onclick(event):
    if event.inaxes == ax:
        x, y = event.xdata, event.ydata
        marker, = ax.plot(x, y, 'ko')  # Dibuja un punto negro en la posición clickeada
        puntos.append((x, y))  # Agrega el punto a la lista de puntos
        markers.append(marker)  # Agrega el objeto del punto a la lista de markers
        fig.canvas.draw()  # Actualiza la figura para mostrar el nuevo punto


#Evento para limpiar los puntos
def clear(event):
    for marker in markers:
        marker.remove()  # Elimina el punto de la figura
    markers.clear()  # Reinicia la lista de markers
    puntos.clear() # Reinicia la lista de puntos
    clear_line()  # Limpia la línea de decisión

#Funcion para limpiar la linea
def clear_line():
    for linea in lineas:
        linea.remove()  # Elimina la línea de la figura
    lineas.clear()  # Reinicia la lista de líneas
    fig.canvas.draw()  # Actualiza la figura para reflejar los cambios

#Funcion para ejecutar el perceptron
def plot(event):
    w0=float(w0Box.text)
    w1=float(w1Box.text)
    w2=float(w2Box.text)
    w=np.array([w0,w1,w2])
    x=np.array(puntos)
    m, c = calcular(w0, w1, w2)
    if len(x) > 0:
        y=p.perceptron(w,x)
        #Recolorear los puntos segun su clase
        for i, marker in enumerate(markers):
            if y[i] == 0:
                marker.set_color('blue')  # Clase 0 en azul
            else:
                marker.set_color('red') # Clase 1 en rojo
    #Dibujar la linea
    clear_line()  # Limpia la línea de decisión anterior antes de dibujar la nueva
    if m is not None:
        x_vals=np.linspace(-10, 10, 200)
        y_vals=m*x_vals+c
        linea, = ax.plot(x_vals, y_vals, 'g--', linewidth=1.5,)  # Dibuja la línea de decisión
        lineas.append(linea)
    fig.canvas.draw()  # Actualiza la figura para mostrar los cambios


#Funcion para calcular m y c
def calcular(w0,w1,w2):
    if w2 == 0:
        return None, None  # Evitar división por cero
    m = -w1 / w2
    c = -w0 / w2
    return m, c

fig, ax = crear_figura()
w0Box, w1Box, w2Box, plotButton, clearButton = crear_widgets(fig)
plotButton.on_clicked(plot)
clearButton.on_clicked(clear)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()