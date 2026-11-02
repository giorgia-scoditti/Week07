from dataclasses import  dataclass

@dataclass
class Trip:
    trip_id : int
    bike_id : int
    start_station_id : int
    end_station_id : int
    start_time : str
    end_time : str
    duration_seconds : int
    user_type : str

    def __str__(self):
        return f"Trip {self.trip_id}"