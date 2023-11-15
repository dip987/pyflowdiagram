from typing import List, Tuple, Optional
from collections import Counter
from matplotlib import colormaps

# All colormaps
cmap_names = ['Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
              'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
cmap = colormaps['Purples']

RGBType = List[Tuple[float, float, float, float]]


def get_color_list(group_ids: List[int], alpha: float) -> RGBType:
    """
    Get a list of (r, g, b, a) color values based on the group_ids. Same group members will have similar coloring
    :param group_ids: integer list of group ids; example: [0, 1, 0, 2, 2, 1]
    :param alpha: replaces the alpha of each color with this value
    :return: (r, g, b, a) list of colors corresponding to the group_ids

    Note: Currently only support 17 unique groups. Anything beyond this will use recycled colors
    """
    group_length_counter = Counter(group_ids)
    # Start the count for each group from 1 and end at the length
    current_counter = {k: 1 for k in group_length_counter.keys()}

    color_list = []
    for group_id in group_ids:
        color_bar_fraction = current_counter[group_id] / group_length_counter[group_id] / 2  # Only use half the space
        group_colormap = colormaps[cmap_names[group_id % len(cmap_names)]]
        color_list.append(group_colormap(color_bar_fraction))
        current_counter[group_id] += 1

    # Update alpha
    color_list = [(x[0], x[1], x[2], alpha) for x in color_list]
    return color_list
