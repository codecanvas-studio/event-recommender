from geopy.distance import geodesic

class GeoFilterEvents:
    def __init__(self, reference_location, radius_km):
        """
        reference_location: tuple of (lat, lon)
        radius_km: numeric radius in kilometers
        """
        self.reference_location = reference_location
        self.radius_km = radius_km

    def filter_events(self, events):

        filtered_events = []
        for event in events:
            if event['location']:
                lat = event['location'][0]
                lon = event['location'][1]

                if lat is not None and lon is not None:
                    distance = geodesic(self.reference_location, (lat, lon)).km
                    print(distance)
                    if distance <= self.radius_km:
                        filtered_events.append(event)
        return filtered_events