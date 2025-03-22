

class Company:
    def __init__(self):
        self.t_task = []
    
class University:
    def __init__(self):
        self.t_task = []
    
    
class TimeFlow:
    def __init__(self, date):
        self.date = date
        self.comapny = Company()
        self.university = University()
        
        
today_taks = TimeFlow(025-3-21)
today_taks.university.t_task = [
    " transformer acrhitecture explained"
]
