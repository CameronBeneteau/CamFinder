from Enums.Region import Region

# User Information
USER_ID: str = ""
REGION: Region = Region.US_EAST_1

# Login Info
EMAIL: str = ""
PASSWORD: str = ""

# Configuration
PROPOSAL_REFRESH_TIME: int = 10  # Minutes
FREE_CONSULTATION: bool = True
ALLOWED_SERVICE_TYPES: list = []  # List of strings (empty for all)

# types:
# multiselect
# select
# text

# Filter
# filter = {
#     "resume writing": {
#         "What type of resume?": {
#             "type": "multiselect",
#             # "options": ["LinkedIn profile", "Traditional resume", "Other"],
#             # "value": ["LinkedIn profile"]
#             # "filter": {
#             # "operator": "", # and, or
#             # }
#         },
#         # "What type of resume?": ["LinkedIn profile", "Traditional resume", "Other"],
#         # "What stage of resume writing are you in?": "",
#         # "Where are you in your career?": "",
#         # "Which industries are you focused on?": "",
#         # "How would you like to work with the resume writer?": "",
#     },
#     "application development": {
#         "What kind of application development services?": {
#             "type": "multiselect",
#             "value": [],
#             "operator": "",
#         },
#         "What type of project?": {"type": "select", "value": "Social application"},
#     },
# }
