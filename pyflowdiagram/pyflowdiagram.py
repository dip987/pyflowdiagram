"""Main module."""
from typing import List, Optional

import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure
from pyflowdiagram.visual_elements import draw_block, create_axes, draw_arrow
from pyflowdiagram.colors import get_color_list


def draw_process_flow(labels: List[str], rect_width: float, rect_height: float,
                      group_ids: Optional[List[int]] = None) -> Figure:
    """
    Draw a linear process from diagram connecting all the labels in [labels], starting from the first element.

    Note: Call plt.show() afterward to view the diagram

    :param labels: List of the process flow labels. Preferably a single word, or words attached by \n
    :param rect_width: width of each block within the process flow diagram (cm)
    :param rect_height: height of each block within the process flow diagram (cm)
    :param group_ids: group ID corresponding to each label, used for coloring. Labels with the same group have will
    have similar coloring in the process flow graph
    :return: Matplotlib Figure containing the process flow
    """
    # Defaults to group 0 if no group_ids are provided
    if group_ids is None:
        group_ids = [0] * len(labels)

    spacing = rect_width * 0.4

    # All the flow blocks fit within the center_frame, but make the actual figure 10% larger
    center_frame_width = rect_width * len(labels) + spacing * (len(labels) - 1)
    fig_width = center_frame_width * 1.1

    fig_height = rect_height * 2    # Twice as high as each individual block

    # width and height are in cm -> convert to inches before passing to [plt.figure()]
    fig: Figure
    fig = plt.figure(figsize=(fig_width / 2.54, fig_height / 2.54))
    ax = create_axes(fig, fig_width, fig_height)

    first_block_center_x = (fig_width - center_frame_width) / 2 + rect_width / 2
    centers = []
    for i in range(len(labels)):
        centers.append((first_block_center_x + i * (rect_width + spacing), fig_height / 2))

    color_list = get_color_list(group_ids, 0.5)

    for i in range(len(labels)):
        draw_block(labels[i], centers[i], ax, rect_width, rect_height, color_list[i])

    for i in range(len(labels) - 1):
        draw_arrow(centers[i], centers[i + 1], ax, (rect_width, rect_width))

    return fig
