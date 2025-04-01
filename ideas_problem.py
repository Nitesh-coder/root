from engine.brain_strom import BrainStrom

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
large_scale_project.problem.plan = [
    "Instead i better build in chunks",
    "Figure out right project idea which fit current resources capabilities",
    "Example:",
    "Build agent for develop website for your business which handed over you production file(html)",
    "Build agent for deplolier which will deploy that site on your recommended web service(aws, ngnix, vercel etc)",
    "Build agent for market research which will give you idea about what kind of product in demand righ now",
    "Build agent for your budget manager which will give you best possible way to mange your budget accoriding to your project"
]


introspection = BrainStrom()
introspection.problem.describe = "what's going on"
introspection.problem.think = [
    "do not lost in the way, balance out",
    "it's wired to be reaction machine: your reaction describe you to the puble: practice reactionless",
    "overwhelmed by oppertunities, tools, complexity and doubtness"
]

map = BrainStrom()
map.problem.describe = "It's hard to figure out where we are standing at when exploring big area like AI"
map.problem.plan = [
    "Research about map of areas",
    "Create ai agent about it",
    "Now integrate with react app",
    "Deploy it in NGNIX server"
]

own_the_style = BrainStrom()
own_the_style.problem.describe = "There are millions of design and style and it's hard to mix all the design to the product."
own_the_style.problem.think = [
    "So chose one theme for rest of the prodcut like apple",
    "Chose one style and own the style",
    "Theme, color and design should align"
]
