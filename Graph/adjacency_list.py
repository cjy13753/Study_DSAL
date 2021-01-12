class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
    
    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)

    def __str__(self):
        res_str = f"{self.station_name}: "

        for station in self.adjacent_stations:
            res_str += f"{station.station_name} "

        return res_str

def create_subway_graph(input_file):
    with open(input_file) as raw_file:
        subway_graph = {}
        
        for line in raw_file:
            subway_line = line.strip().split('-')

            previous_station = None
            for name in subway_line:
                station_name = name.strip()

                if station_name not in list(subway_graph.keys()):
                    subway_graph[station_name] = StationNode(station_name)
                                
                if previous_station is not None:
                    subway_graph[station_name].add_connection(subway_graph[previous_station])
                previous_station = station_name
        
    return subway_graph


stations = create_subway_graph("./stations.txt")

for station in sorted(stations.keys()):
    print(stations[station])