import model.memory as memory
import datetime

class Company:
    def __init__(self):
        self.create = str
        self.roadmap = []
        self.features = []
        self.t_task = []
        self.report = {}
    
class University:
    def __init__(self):
        self.syllabus = []
        self.t_task = []
    
    
class TimeFlow:
    def __init__(self):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.company = Company()
        self.university = University()
        self.report = []
    
    def save(self):
        memory.store(
            {
                "date": self.date,
                "university": self.university.t_task,
                "company": self.company.t_task
            }
        )