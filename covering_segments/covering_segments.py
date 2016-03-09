"""
Uses python3

Given a set of n segments { [a_0, b_0], [a_1, b_1], ..., [a_n-1, b_n-1] } with integer coordinates on a line,
find the minimum number m of points such that each segment contains at least one point.
That is find a set of Integers X of the minimum size such that for any segment [a_i, b_i] there is a point x,
such that a_i <= x <= b_i

Input:
The First line contains number of segments n.
Each of next n lines contains pair a_i, b_i separated by space

"""
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def main():
    segments = initialize_data()
    points = get_optimal_points(segments)
    print("Number of minimal common points:", len(points))
    print("Common points:", end=' ')
    for p in points:
        print(p, end=' ')


def initialize_data():
    input_data = sys.stdin.read()
    n, *data = map(int, input_data.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    return sorted(segments, key=lambda s: s.start)


def get_optimal_points(segments):
    points = []
    common_segment = segments.pop(0)
    while segments:
        next_segment = segments.pop(0)
        common_segment = get_covering_segment_and_append_common_points(common_segment, next_segment, points)
    points.append(common_segment.end)
    return points


def get_covering_segment_and_append_common_points(common_segment, next_segment, points):
    if get_common_segment(common_segment, next_segment) is not None:
        common_segment = get_common_segment(common_segment, next_segment)
    else:
        points.append(common_segment.end)
        common_segment = next_segment
    return common_segment


def get_common_segment(s1, s2):
    start = get_common_start(s1, s2)
    end = get_common_end(s1, s2)
    if start is not None:
        common_segment = Segment(start, end)
        return common_segment
    else:
        return None


def get_common_start(s1, s2):
    if s1.end >= s2.start:
        return s2.start
    else:
        return None


def get_common_end(s1, s2):
    if s1.end >= s2.end:
        return s2.end
    else:
        return s1.end

if __name__ == '__main__':
    main()
