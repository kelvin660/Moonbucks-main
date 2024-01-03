import gmplot

api_file = open("api_key.txt")
key = api_file.read()
api_file.close()

filename = 'starbucks_2018_11_06.csv'


# def plotMap():
#     latitude = []
#     longitude = []
#     df = pd.read_csv(filename)
#     for index, rows in df.iterrows():
#         latitude.append(rows['latitude'])
#         longitude.append(rows['longitude'])
#
#     x = zip([latitude], [longitude])
#
#     gmap = gmplot.GoogleMapPlotter(0, 0, 5, apikey=key)
#     gmap.scatter(
#         latitude,
#         longitude,
#         color='red',
#         s=60,
#         ew=2,
#         marker=True,
#         symbol=None,
#         title=None,
#         # label=['A', 'B', 'C', 'D', 'E', 'F']
#     )
#     gmap.draw('map1.html')


#

# gmaps = googlemaps.Client(key=API_key)
#
# def pairwise(iterable):
#     a,b = tee(iterable)
#     next(b,None)
#     return zip(a,b)
#
# list =[0]
#

# for (i1,row1), (i2,row2) in pairwise(df.iterrows()):
#     # LatOrigin =row1['Latitude']
#     # LongOrigin = row1['Longitude']
#     origins = (22.28394,114.1582)
#
#     LatDest = row2['Latitude']
#     LongDest = row2['Longitude']
#     destination = (LatDest,LongDest)
#     # print(destination)
#
#     result = gmaps.distance_matrix(origins, destination, mode='walking')
#
#     print(result)
#     # list.append(result)
#     #
#     # df['Distance'] = list
#     #
#     # df.to_csv ('calculated_distances.csv', sep=';', index=None, header=['id','Latitude','Longitude','track_id','time','distance'])

# gmap.draw('map1.html')

def drawRoute(points_list, center_point, path):
    gmap = gmplot.GoogleMapPlotter(0, 0, 0, map_type='ROADMAP', title="Directions using TSP", apikey=key)

    char = 'A'

    for i in points_list:
        gmap.marker(i[0], i[1], label=char)
        char = chr(ord(char) + 1)

    routes = []
    for i in range(1, len(points_list) - 1):
        routes.append(points_list[i])

    print(routes)
    print(points_list[path[0]])

    gmap.directions(
        # points_list[path[0]],
        # points_list[path[0]],
        (37.799001, -122.442692),
        (37.832183, -122.477914),
        waypoints=routes

    )

    gmap.draw("map.html")
