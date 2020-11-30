class Town:
    def __init__(self,town):
        self.town = town
        self.latitude = ''
        self.longitude = ''

    def set_latitude(self,latitude):
        self.latitude = latitude

    def set_longitude(self,longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.town} | Latitude: {self.latitude} | Longitude: {self.longitude}"
