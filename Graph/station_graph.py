def create_station_nodes(input_file):
    stations = {}

    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:
            subway_line = line.strip().split("-")

            for name in subway_line:
                station_name = name.strip()

                if station_name not in stations:
                    stations[station_name] = StationNode(station_name)

    return stations

class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name


stations = create_station_nodes("./stations.txt")

for station in sorted(stations.keys()):
    print(stations[station].station_name)