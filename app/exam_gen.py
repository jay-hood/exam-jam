#!/usr/bin/python

import json


class ExamGenerator():

    """take a dictionary representation of an exam bank and generate
    exams from it. Values that should be passed: dictionary of 
    exam questions and their possible answers. Requirements:

    Dictionary can have nested values that identify which questions are correct
    as well as point values. 

    If the dictionary has point values, it 
    should check to see if a special field exists that says what the
    total points for an exam should be. 

    This method should return
    ...something. I am not actually sure how to serve the resulting
    archive back to the client. That might be tricky. 

    The dictionary should also specify how many exam blocks there should be

    Later, add an optional list of student names as strings that can be randomly
    applied to all exams.

    Add an option for the above student roster list to automatically fill the "Name"
    space on exams.

    Concerns: Need to escape double quotes in input data somehow.

    Need to be aware of the possibility of users breaking json with special characters. Need to make
    a special character list and either handle those special character or forbid their
    entry.


    Need a way to guarantee that each question has exactly one correct answer.
    """

    """ This entire process can likely be done asynchronously and would see some significant time
    saving benefits. Not sure if I know enough about asynchronous programming to pull it off, but
    it might be worth a try, if nothing else, given the sequential I/O operations involved. """

    def entry_point(self, bank: dict) -> None:
        new_exam = Exam(bank)
        new_exam.export_bank_to_db()
        new_exam.build_sets()
        new_exam.export_sets_to_db()
        new_exam.build_pdfs()
        new_exam.export_pdfs_to_db()
        new_exam.build_archive()
        return new_exam.get_archive()


class Exam():

    def __init__():
        pass


if __name__ == '__main__':
    test_data = {}
    with open('/home/jay/code/projects/python/exam-jam/test_data.json') as td:
        test_data = json.load(td)
        td.close()
    ex_gen = ExamGenerator()
    ex_gen.entry_point(test_data)
