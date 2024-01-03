import sys
from itertools import permutations
from sys import maxsize

import pandas as pd
import requests

from map import drawRoute

api_file = open("api_key.txt")
API_KEY = api_file.read()
api_file.close()

file_path = './starbucks_2018_11_06.csv'


def getLocationList(country_name, num):
    df = pd.read_csv(file_path)

    df = df[df.state == country_name]
    df = df.head(num)
    df = df[['latitude', 'longitude']]

    points_list = list(df.to_records(index=False))

    return points_list


def getDistanceMatrix(points_list):
    http_body = "|".join([f"{x[0]},{x[1]}" for x in points_list])

    url = ("https://maps.googleapis.com/maps/api/distancematrix/json?language=en-US&units=meters"
           + "&origins={}"
           + '&destinations={}'
           + '&key={}').format(http_body, http_body, API_KEY)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    content = response.json()

    final_response = content['rows']

    distance_arr = []
    for ele in final_response:
        ori_des_dis = []
        info = ele["elements"]
        for dis in info:
            ori_des_dis.append(dis['distance']['value'])
        distance_arr.append(ori_des_dis)

    return distance_arr


def find_center(distance_matrix):
    # find point that is closest to other point(i.e. min(sum of d_i - d) for i in range of 1 to n)
    # brute force

    min_val = sys.maxsize
    index = -1

    for i in range(len(distance_matrix)):
        sum = 0
        for j in range(len(distance_matrix[i])):
            sum += distance_matrix[i][j]
        if sum < min_val:
            min_val = sum
            index = i

    print(str(min_val) + " " + str(index))
    return index


def travellingSalesmanProblem(distance_arr, center):
    path = []
    V = len(distance_arr)
    vertex = []
    for i in range(V):
        if i != center:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = center
        for j in i:
            current_pathweight += distance_arr[k][j]
            k = j
        current_pathweight += distance_arr[k][center]

        # update minimum
        if min_path > current_pathweight:
            min_path = current_pathweight
            path_list = i

    path.append(center)
    for i in path_list:
        path.append(i)
    path.append(center)

    return path, min_path


# def drawMap(points_list, center):
#     temp_points = points_list.copy()
#     temp = temp_points.pop(center)
#
#     gmaps.configure(api_key=API_KEY)
#
#     fig = gmaps.figure(map_type='ROADMAP')
#     markers = gmaps.marker_layer(temp_points)
#     center_markers = gmaps.marker_layer([temp], label='C')
#     fig.add_layer(markers)
#     fig.add_layer(center_markers)
#     return fig
#
#
# def drawRoute(points_list, center, path):
#     temp_points = points_list.copy()
#     temp = temp_points.pop(center)
#     fig = gmaps.figure(map_type='ROADMAP')
#
#     for i in range(len(path) - 1):
#         ori = points_list[path[i]]
#         des = points_list[path[i + 1]]
#         fig.add_layer(gmaps.directions_layer(ori, des, stroke_color='red', show_markers=False, stroke_weight=1.0,
#                                              stroke_opacity=1.0))
#
#     markers = gmaps.marker_layer(temp_points)
#     center_markers = gmaps.marker_layer([temp], label='C')
#     fig.add_layer(markers)
#     fig.add_layer(center_markers)
#     return fig


if __name__ == "__main__":
    location_list = (getLocationList("GB", 7))

    distance_matrix = getDistanceMatrix(location_list)
    center_point = find_center(distance_matrix)
    print(location_list)

    path, min_cost = travellingSalesmanProblem(distance_matrix, center_point)

    print(path)
    print(min_cost, "m")

    drawRoute(location_list, center_point, path)
