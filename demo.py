from qt_plot import Plotter
import numpy as np

if __name__ == '__main__':
    plotter = Plotter()
    triangle = np.array([[0,0], [0,1], [1,0]])
    triangle2 = np.array([[0, 0], [0, -1], [1, 0]])

    plotter.draw_contours('./layout.png', [('lightgray', triangle), ('lightblue', triangle2)])
