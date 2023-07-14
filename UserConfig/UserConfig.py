from Enums.RegionEnum import RegionEnum
from Enums.QuestionEnum import QuestionEnum

from Models.Question import Question


# User Information
USER_ID: str = ""
REGION: RegionEnum = RegionEnum.US_EAST_2

# Login Info
EMAIL: str = ""
PASSWORD: str = ""

# Configuration
PROPOSAL_REFRESH_TIME: int = 10  # Minutes
FREE_CONSULTATION: bool = True

FILTERS: dict[str, dict[str, Question]] = {}
