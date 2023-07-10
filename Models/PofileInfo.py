class ProfileInfo:
    name: str
    service_type: str
    location: str
    profile_description: str
    profile_link: str

    def __init__(self, name, service_type, location, profile_description, profile_link):
        self.name = name
        self.service_type = service_type
        self.location = location
        self.profile_description = profile_description
        self.profile_link = profile_link
