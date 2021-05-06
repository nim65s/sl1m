import matplotlib.pyplot as plt
import numpy as np


COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']


def plot_point(ax, point, color="b", linewidth=2):
    """
    Plot a point
    """
    x = np.array(point)[0]
    y = np.array(point)[1]
    z = np.array(point)[2]
    ax.scatter(x, y, z, color=color, marker='o', linewidth=linewidth)


def plot_surface(points, ax, color_id=0, alpha=1.):
    """
    Plot a surface
    """
    xs = np.append(points[0, :], points[0, 0]).tolist()
    ys = np.append(points[1, :], points[1, 0]).tolist()
    zs = np.append(points[2, :], points[2, 0]).tolist()
    if color_id == -1:
        ax.plot(xs, ys, zs)
    else:
        ax.plot(xs, ys, zs, color=COLORS[color_id % len(COLORS)], alpha=alpha)


def draw_potential_surfaces(surfaces, gait, phase, ax=None, alpha=1.):
    """
    Plot all the potential surfaces of one phase of the problem
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    for surface in surfaces:
        plot_surface(surface, ax, gait[phase % (len(gait))])
    return ax


def draw_whole_scene(surface_dict, ax=None):
    """
    Plot all the potential surfaces
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    for key in surface_dict.keys():
        plot_surface(np.array(surface_dict[key][0]).T, ax, 5)
    return ax


def draw_scene(surfaces, gait, ax=None, alpha=1.):
    """
    Plot all the potential surfaces of the problem
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    for i, surfaces_phase in enumerate(surfaces):
        for surface in surfaces_phase:
            plot_surface(surface, ax, gait[i % len(gait)], alpha=alpha)
    return ax


def draw_first_surface(surfaces, gait, ax=None):
    """
    Plot all the potential surfaces
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    for surface in surfaces[0]:
        plot_surface(surface, ax, gait[0])
    return ax


def plot_initial_contacts(initial_feet_pose, ax=None):
    """
    Plot the initial feet positions
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    ax.grid(False)

    for i in range(len(initial_feet_pose)):
        plot_point(ax, initial_feet_pose[i], color=COLORS[i])


def plot_new_contact(moving_foot, moving_foot_pos, ax=None):
    """
    Plot the initial feet positions
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    ax.grid(False)

    plot_point(ax, moving_foot_pos, color=COLORS[moving_foot])


def plot_first_step(configs, coms, moving_foot_pos, gait, ax=None):
    """
    Plot the moving feet positions
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    ax.grid(False)

    plot_point(ax, configs[0], color=COLORS[len(gait) + 1])
    plot_point(ax, coms[0], color=COLORS[len(gait) + 2])
    plot_point(ax, moving_foot_pos[0], color=COLORS[gait[0]])


def plot_selected_surfaces(surfaces, surface_indices, gait, ax=None):
    """
    Plot the surface with the minimum alpha
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    for i, surfaces_phase in enumerate(surfaces):
        plot_surface(surfaces_phase[surface_indices[i]], ax, gait[i % len(gait)])
    return ax


def plot_heightmap(heightmap, alpha=1., ax=None):
    """
    Plot the heightmap
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    i = 0
    if alpha != 1.:
        i = 1
    ax.plot_surface(heightmap.xv, heightmap.yv, heightmap.zv, color=COLORS[i], alpha=alpha)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_zlim([np.min(heightmap.zv), np.max(heightmap.zv) + 1.])

    return ax


def plot_point_list(ax, wps, color="b", D3=True, linewidth=2):
    """
    Plot a list of points
    """
    x = np.array(wps)[:, 0]
    y = np.array(wps)[:, 1]
    if(D3):
        z = np.array(wps)[:, 2]
        ax.scatter(x, y, z, c=color, marker='o', linewidth=5)
    else:
        ax.scatter(x, y, color=color, linewidth=linewidth)


def plot_planner_result(coms, moving_foot_pos, all_feet_pos, ax=None, show=True):
    """
    Plot the feet positions and com positions
    """
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    ax.grid(False)
    ax.view_init(elev=8.776933438381377, azim=-99.32358055821186)

    for foot in range(len(all_feet_pos)):
        plot_point_list(ax, all_feet_pos[foot], color=COLORS[foot])
        px = [c[0] for c in all_feet_pos[foot]]
        py = [c[1] for c in all_feet_pos[foot]]
        pz = [c[2] for c in all_feet_pos[foot]]
        ax.plot(px, py, pz, color=COLORS[foot])

    plot_point_list(ax, coms, color=COLORS[len(all_feet_pos)+1])
    cx = [c[0] for c in coms]
    cy = [c[1] for c in coms]
    cz = [c[2] for c in coms]
    ax.plot(cx, cy, cz, color=COLORS[len(all_feet_pos)+1])
    if show:
        plt.draw()
        plt.show()