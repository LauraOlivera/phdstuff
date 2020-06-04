import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def nice_colorbar(im,ax,side="right",size="5%",pad=0.05):
    """Make colorbars when using plt.imshow() that look nice
	(see https://github.com/matplotlib/matplotlib/issues/17559)
	Inputs:
		im = plt.imshow(you_data)
		ax = axis of the figure
		side = where you want the colorbar to go
		size = proportional to the main axis dimensions
		pad = distance to main figure """

    if side is "right" or side is "left":
        orientation = 'vertical'
    else:
        orientation = 'horizontal'
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(side, size=size, pad=pad)
    cbar = plt.colorbar(im, cax=cax,orientation=orientation)
