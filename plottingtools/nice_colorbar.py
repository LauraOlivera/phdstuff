import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def nice_colorbar(im,ax,side="right",size="5%",pad=0.05):
    if side is "right" or side is "left":
        orientation = 'vertical'
    else:
        orientation = 'horizontal'
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(side, size=size, pad=pad)
    cbar = plt.colorbar(im, cax=cax,orientation=orientation)
