from dataclasses import dataclass

@dataclass
class Stats:
    count: int
    distance: float
    moving_time: float
    elapsed_time: float
    elevation_gain: float

    def __init__(self, json):
        self.count = json['count']
        self.distance = json['distance']
        self.moving_time = json['moving_time']
        self.elapsed_time = json['elapsed_time']
        self.elevation_gain = json['elapsed_time']

    def print_as_line_protocol(self, tag):
        print("bicycle,time_range=" + tag + " count=" + str(self.count) + ",distance=" + str(self.distance) + ",moving_time=" + str(self.moving_time) + ",elapsed_time=" + str(self.elapsed_time) + ",elevation_gain=" + str(self.elevation_gain))

    def as_dict(self):
        return {
                'count': self.count,
                'distance': self.distance,
                'moving_time': self.moving_time,
                'elapsed_time': self.elapsed_time,
                'elevation_gain': self.elevation_gain
                }
