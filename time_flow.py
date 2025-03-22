import memory
import datetime

class Company:
    def __init__(self):
        self.t_task = []
    
class University:
    def __init__(self):
        self.t_task = []
    
    
class TimeFlow:
    def __init__(self):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.company = Company()
        self.university = University()
    
    def save(self):
        memory.store(
            {
                "date": self.date,
                "university": self.university.t_task,
                "company": self.company.t_task
            }
        )
        
        
today_taks = TimeFlow()
today_taks.university.t_task = [
    
    " firebase auth"
]
today_taks.save()
