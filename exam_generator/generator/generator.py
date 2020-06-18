#!/usr/bin/python


from exam import Exam


class Generator():

    def __init__(self, data) -> None:
        try:
            self.data: str = data
        except KeyError:
            print("Error: Must pass json string to Generator class.")
            exit(1)
        try:
            self.target_score = data["target_score"]
        except KeyError:
            self.target_score = 100
        try:
            self.exam_blocks: int = data["exam_blocks"]
        except KeyError:
            self.exam_blocks: int = 1
        try:
            self.questions_per_block: int = data["questions_per_block"]
        except KeyError:
            num_questions = 0
            for key, value in self.data:
                if key.split("_")[0] == "question":
                    num_questions += 1
            self.questions_per_block: int = int(num_questions/self.exam_blocks)
        self.questions = []
        for key, value in self.data:
            if key.split("_")[0] == "question":
                self.questions.append({key: value})
        self.exams = []

    def generate_exam_sets(self) -> None:
        self.exams = []
        for block in self.exam_blocks:
            exams.append(self.make_exam_from_questions())


    def generate
