from engine.time_flow import University
# "What I cannot create, I do not understand."
dl = University()
dl.syllabus = [
    {
        "name": "intro to neural network and backpropagation",
        "teacher": "Andrej Karpathy",
        "number": 1,
        "duration": 145
    },
    {
        "name": "neural network form scratch",
        "teacher": "sentdex",
        "number": 9,
        "duration": [16,15,25,33,40,34,16,17,14]
    },
]

today_task = dl.t_task = [
    {
        "date": "025-3-27",
        "name": [dl.syllabus[0]],
        "time": 20
    }
]

print(today_task[0]["name"][0]['name'])