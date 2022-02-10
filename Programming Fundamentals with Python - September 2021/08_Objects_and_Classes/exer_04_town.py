# class Town:
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def set_latitude(self, latitude=0):
#         self.latitude = latitude
#
#     def set_longitude(self, longitude=0):
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


class Town:
    def __init__(self, name: str):
        self.name = name

    def set_latitude(self, latitude=0):
        self.latitude = latitude

    def set_longitude(self, longitude=0):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
