#!/usr/bin/python


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
    """

    def entry_point(bank: dict,
                    roster: bool = False,
                    namefill: bool = False) -> None:
        pass






if __name__ == '__main__':
    pass
