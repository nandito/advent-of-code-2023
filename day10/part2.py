import shapely
import numpy as np
from rasterio.features import rasterize


shapes = {
    "|": ((0.5, 1), (0.5, 0)),
    "-": ((0, 0.5), (1, 0.5)),
    "L": ((0.5, 1), (0.5, 0.5), (1, 0.5)),
    "J": ((0.5, 1), (0.5, 0.5), (0, 0.5)),
    "7": ((0.5, 0), (0.5, 0.5), (0, 0.5)),
    "F": ((0.5, 0), (0.5, 0.5), (1, 0.5)),
}
shapes = {k: np.array(v) for k, v in shapes.items()}


def make_line(shape: str, crds):
    try:
        return shapely.LineString(shapes[shape] + crds)
    except KeyError:
        return None


def solve_part2(lines):
    maze = np.array([list(line.strip()) for line in lines])
    coords = np.indices(maze.shape)[::-1, ::-1, :]
    lines = [
        make_line(shp, crds)
        for shp, crds in zip(maze.ravel(), np.stack(coords, axis=-1).reshape(-1, 2))
    ]

    lines = [*shapely.line_merge(shapely.union_all(lines)).geoms]
    loop = lines[np.argmax([*map(shapely.length, lines)])]

    loop_mask = rasterize(
        [loop],
        maze.shape,
        all_touched=True,
    )

    poly_mask = rasterize(
        [shapely.Polygon(loop)],
        maze.shape,
        all_touched=True,
    )

    print("Part 2:", np.sum(poly_mask) - np.sum(loop_mask))

