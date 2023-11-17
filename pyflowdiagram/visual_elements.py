from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib.pyplot import Rectangle, Axes, Figure


class CenteredRectangle(Rectangle):
    """
    Wrapper around Matplotlib.pyplot.Rectangle but with center_xy rather than bottom left corner xy
    """
    def __init__(self, center_xy: Tuple[float, float], width: float, height: float, **kwargs):
        left_x = center_xy[0] - width / 2
        bottom_y = center_xy[1] - height / 2
        super().__init__((left_x, bottom_y), width, height, **kwargs)
        self.center_xy = center_xy


def draw_block(text: str, xy: Tuple[float, float], axes: Axes, width: float,
               height: float, bg_color) -> None:
    """
    Draws a block with a text inside at the given xy
    :param text: Label at the center of the block
    :param xy: Center x,y (in cm)
    :param axes: Matplotlib Axes to draw the block on
    :param width: block width(cm)
    :param height: block height(cm)
    :param bg_color: Background color (Either a string or (r, g, b, a) values
    """
    rect = CenteredRectangle(xy, width, height, fc=bg_color, ec='k')
    axes.add_patch(rect)
    axes.text(xy[0], xy[1], text, horizontalalignment='center', verticalalignment='center')


def draw_arrow(xy1:  Tuple[float, float], xy2:  Tuple[float, float], axes: Axes,
               rect_width: Tuple[float, float]) -> None:
    """
    Draws an arrow between two blocks with centers xy1(Left) and xy2(Right)
    :param xy1: Center for the first block
    :param xy2: Center for the second block, points towards this block
    :param axes: Matplotlib Axes to draw the arrow on to
    :param rect_width: width of (block at xy1, block at xy2)
    :return:
    """
    axes.annotate("", (xy1[0] + rect_width[0] / 2, xy1[1]), (xy2[0] - rect_width[1] / 2, xy2[1]),
                  arrowprops={'arrowstyle': "<|-"})



def create_axes(fig: Figure, fig_width: float, fig_height: float) -> Axes:
    """
    Create the background axes for process flow diagrams
    :param fig: The figure to create the axes on
    :param fig_width: Width in cm (Used for setting limits)
    :param fig_height: Height in cm (Used for setting limits)
    """
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, fig_width)
    ax.set_ylim(0, fig_height)

    # Turn off ticks
    ax.tick_params(bottom=False, top=False, left=False, right=False)
    ax.set_facecolor('white')
    plt.axis('off')

    SIDES = ['top', 'bottom', 'left', 'right']
    SPINE_COLOR = "midnightblue"
    for side in SIDES:
        ax.spines[side].set_color(SPINE_COLOR)
        ax.spines[side].set_linewidth(4)
    return ax
