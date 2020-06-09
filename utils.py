import pygame


def binary_search_2d(p, grid):
    """
    find the nearest point in the 2d grid
    :param p:
    :param grid:
    :return:
    """

    first_row = grid[0]

    nearest_x = binary_search_1d(p.x, first_row, 1).centerx
    nearest_y = binary_search_1d(p.y, [row[0] for row in grid], 0).centery

    index_x = 0
    index_j = 0
    for j, cell in enumerate(first_row):
        if cell.centerx == nearest_x:
            index_j = j
            break

    col = [row[index_j] for row in grid]
    for i, cell in enumerate(col):
        if cell.centery == nearest_y:
            index_x = i

    return grid[index_x][index_j]


def binary_search_1d(value, li, axis=0):
    """
    find the nearest value in the list li, assuming the list is sorted
    :param value: the value to be searched
    :param li: list
    :param axis:
    :return: nearest cell in the list
    """
    if axis == 0:
        if value < li[0].centery:
            return li[0]

        if value > li[-1].centery:
            return li[-1]

        low = 0
        high = len(li) - 1

        while low <= high:
            # middle index
            mid = (high + low) // 2
            if value < li[mid].centery:
                high = mid - 1
            elif value > li[mid].centery:
                low = mid + 1
            else:
                return mid
        return li[low] if (li[low].centery - value) < (value - li[high].centery) else li[high]
    elif axis == 1:
        if value < li[0].centerx:
            return li[0]

        if value > li[-1].centerx:
            return li[-1]

        low = 0
        high = len(li) - 1

        while low <= high:
            # middle index
            mid = (high + low) // 2
            if value < li[mid].centerx:
                high = mid - 1
            elif value > li[mid].centerx:
                low = mid + 1
            else:
                return mid
        return li[low] if (li[low].centerx - value) < (value - li[high].centerx) else li[high]
