from Enums.QuestionEnum import QuestionEnum


class Question:
    def __init__(
        self,
        category: QuestionEnum,
        exclude: list[str],
    ):
        self.category = category
        self.exclude = exclude
