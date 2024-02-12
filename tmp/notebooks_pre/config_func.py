import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def set_colorbar(ax, im):
    """set colorbar into the same size with figure"""
    divider = make_axes_locatable(ax)
    cax  = divider.append_axes("right", size="5%", pad=0.1)
    cbar = plt.colorbar(im, cax=cax)