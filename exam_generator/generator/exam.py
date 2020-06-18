class Exam():

    def __init__(self, questions: list, students: list = [],
                 exam_block_id: int = 0, target_score: int = 100) -> None:
        self.questions = questions
        self.students = students
        self.exam_block_id = exam_block_id
        self.target_score = target_score
