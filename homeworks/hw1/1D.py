from cmath import sqrt
from itertools import combinations
import math

def euclidDist(points: list):
    points = combinations(points, 2)
    #print(list(points))
    ps = []
    for p1, p2 in points:
        d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
        if d > 0 and d < 3:
            ps += [(p1, p2)]
    return ps

if __name__ == "__main__":
    points = ((0, 1, 2), (0, -1, 2), (0, 1, -2), (0, -1, -2), (1, 2, 0), (-1, 2, 0), (1, -2, 0), (-1, -2, 0), (2, 0, 1), (-2, 0, 1), (2, 0, -1), (-2, 0, -1))
    ps = euclidDist(points)
    for t in ps:
        print(t)
    print(len(points))
