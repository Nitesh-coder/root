
class Ideas:
    def __init__(self):
        self.create = str
        self.plan = []
        
class Problem:
    def __init__(self):
        self.describe = str
        self.plan = []
        
class BrainStrom:
    def __init__(self):
       self.idea = Ideas()
       self.problem = Problem()

UIDesign = BrainStrom()
UIDesign.problem.describe = "It's hard to Get which kind of design is suit for app. From sketching to desigining"
UIDesign.problem.plan = [
    "First we must feagure out what kind of app we will builiding",
    "Research about similar genre app and what kind of they design",
    "Extract top design and pick some of them from site like dribble",
    "Now we use ai tool like v0 and claude to ask for create design with that reference in html",
    "Now extract that to figma"
]


businessAgent = BrainStrom()
businessAgent.idea.create = "Shift towards business based market from job based market with Business Agent"
businessAgent.idea.plan = [
    "You can create any business with any ideas simple, easier than before",
    "Ideas is yours, control is yours and everything rest will agent do",
    "You have agent to work for you",
    "Example: i have a plan to open pickle maker industry",
    "You have site agent for make you great site for your needs",
    "You have market research agent for you to do market research for you",
    "You have counslatant agent for counslatating",
    "You have fianancial agent for do and manage your capital",
    "You have legal agent for you to do all the legal things and paper work",
    "You have accounting agent for you to do accounitng",
    "What you need: just command and control with Prime Agent",
    "Prime Agent: which control all other agent and manage your business overall"
]

large_scale_project = BrainStrom()
large_scale_project.problem.describe = "It require tremendous amount of capital and men force to build project like businessAgent"
large_scale_project.problem.describe = [
    "Instead i better build in chunks",
    "Figure out right project idea which fit current resources capabilities",
    "Example:",
    "Build agent for develop website for your business which handed over you production file(html)",
    "Build agent for deplolier which will deploy that site on your recommended web service(aws, ngnix, vercel etc)",
    "Build agent for market research which will give you idea about what kind of prodcut in demand righ now",
    "Build agent for your budget manager which will give you best possible way to mange your budget accoriding to your project"
]
