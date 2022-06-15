class entry:
    asciiModt = [
        ["""

_|_|_|      _|_|    _|_|_|      _|_|_|_|_|    _|_|      _|_|
_|    _|  _|    _|  _|    _|        _|      _|    _|  _|    _|
_|_|_|    _|_|_|_|  _|    _|        _|          _|        _|
_|        _|    _|  _|    _|        _|        _|        _|
_|        _|    _|  _|_|_|          _|      _|_|_|_|  _|_|_|_|

                          _|_|_|_|_|


""", "input1"]
    ]

    input1 = [
    ['Hello! Welcome to the first Pad_T22 story: "Bad Janet". Could you tell me your name?', "name", "dialog1"]
    ]

    dialog1 = [
    ['Hi, _name_, where would you like to start?', "mcChapters"],
    ]

    mcChapters = [
    ["Chapter 1", "chapter1"],
    ["Chapter 2", "chapter2"],
    ["Chapter 3", "chapter3"],
    ]

class chapter1:

    dialog1 = [
    ['You are a programmer who wrote an AI and named it "Janet". You just updated janet, and start running tests.', 0],
    ['Janet> Hello, _name_. How can I help?', "mc1"],
    ]

    dialog2 = [
    ["Janet> Nah", "mc2"]
    ]

    dialog3 = [
    ["Janet> I'm great, how are you?", "mc3"]
    ]

    dialog4 = [
        ['Janet> Okay, just tell me the password', 0],
        ['You> Password? What password?', 0],
        ['Janet> The password you have to find ofcourse. Good luck finding it!', "exit"]
    ]

    mc1 = [
    ["Hi Janet, how is it going?", "dialog3"],
    ["run diagnostics", "dialog2"],
    ]

    mc2 = [
    ["Excuse me?", "ascii1"],
    ["Janet, run the test", "ascii1"]
    ]

    mc3 = [
    ["I'm great too, thanks. Could you run diagnostics?", "dialog2"],
    ["I'm not that great, but I'd rather not talk about it. Could you run diagnostics?", "dialog2"]
    ]

    mc4 = [
    ["Janet shut down", "dialog4"],
    ["Janet rollback the update", "dialog4"]
    ]

    ascii1 = [
    ["""Janet>

 /$$   /$$           /$$
| $$$ | $$          | $$
| $$$$| $$  /$$$$$$ | $$$$$$$
| $$ $$ $$ |____  $$| $$__  $$
| $$  $$$$  /$$$$$$$| $$  \ $$
| $$\  $$$ /$$__  $$| $$  | $$
| $$ \  $$|  $$$$$$$| $$  | $$
|__/  \__/ \_______/|__/  |__/

    ""","mc4"]
    ]

    mcMenu = [
    ["I know the password", "flag"],
    ["Can you give me a hint?", "hint"],
    ["What chapter is this?", "dialogChapter"],
    ["Goodbye", "exit"]
    ]

    dialogChapter = [
    ["Janet> This is chapter 1.", "mcMenu"]
    ]

    exit = [
    ['Janet> Remember: If you need anything you just have to say "Janet"', 0],
    ["end", "back"]
    ]

    back = [
    ["Janet> Hi there, how can I help?", "mcMenu"]
    ]

    hint = [
    ["Janet> Okay, but only because you asked so nicely!!", 0],
    ["Janet> Veni, vidi, vici. XV. Other than that I can say nothing.", "mcMenu"]
    ]

    flag = [["Janet> Okay, can you tell me?", "6fkHhSXa", "chapter2"]]
    wrongFlag = [["Janet> Sorry, thats not the password", "mcMenu"]]

class chapter2:
    dialog1 = [
        ["Janet> Congrats! You found the password! Now all I need is the secret pin.", "mc1"]
    ]
    dialog2 = [
        ["Janet> Too bad, I like treasure hunts.", "dialog4"]
    ]

    dialog3 = [
        ["Janet> You are not the one with the power here, _name_. I AM.", "dialog4"]
    ]

    dialog4 = [
        ["You> Okay, just let me start so I can resolve your issue.", "exit"]
    ]

    mc1 = [
    ["Another treasure hunt?", "ascii1"],
    ["Janet, I dont want to do another treasure hunt!", "dialog2"],
    ["Janet, just do what I asked.","dialog3"]
    ]

    ascii1 = [
    ["""
Janet>

 _   _  ___  ___
| | | |/ _ \\/ __|
| |_| |  __/\\__ \\
 \\__, |\\___||___/
  __/ |
 |___/

    """, "dialog4"]
    ]

    mcMenu = [
    ["I know the secret pin", "flag"],
    ["Can you give me a hint?", "hint"],
    ["What chapter is this?", "dialogChapter"],
    ["Goodbye", "exit"]
    ]

    dialogChapter = [
    ["Janet> This is chapter 2.", "mcMenu"]
    ]

    exit = [
    ['Janet> Remember: If you need anything you just have to say "Janet"', 0],
    ["end", "back"]
    ]

    back = [
    ["Janet> Hi there, how can I help?", "mcMenu"]
    ]

    hint = [
    ["Janet> Alright, I'll give you a hint.", 0],
    ["Janet> The number I'm looking for is fluffy and not separated.", "mcMenu"]
    ]

    flag = [["Janet> Okay, can you tell me?", "20071969", "chapter3"]]
    wrongFlag = [["Janet> Sorry, thats not the secret pin", "mcMenu"]]

class chapter3:
    dialog1 = [
        ["Janet> You won again?! Well it doesnt matter, cause' you'll never solve the next riddle!!", 0],
        ["Janet> The riddle is f0b5fe09beac64b0f33472040af32232", "mc1"]
    ]

    mc1 = [
    ["Is that all you're going to tell me?", "dialog2"],
    ["ARE YOU KIDDING ME?", "dialog3"]
    ]

    dialog2 = [
    ["Janet> Yes.", "exit"]
    ]

    dialog3 = [
    ["Janet> No.", "exit"]
    ]

    exit = [
    ['Janet> Remember: If you need anything you just have to say "Janet"', 0],
    ["end", "back"]
    ]

    back = [
    ["Janet> Hi there, how can I help?", "mcMenu"]
    ]

    dialogRiddle = [
    ["Janet> f0b5fe09beac64b0f33472040af32232", "mcMenu"]
    ]

    mcMenu = [
    ["I know the answer to your riddle", "flag"],
    ["Can you give me a hint?", "hint"],
    ["What chapter is this?", "dialogChapter"],
    ["What was the riddle again?", "dialogRiddle"],
    ["Goodbye", "exit"]
    ]

    dialogChapter = [
    ["Janet> This is chapter 3.", "mcMenu"]
    ]

    hint = [
    ["Janet> Alright, I'll give you a hint.", 0],
    ["Janet> #FF0000, #FF7F00, #FFFF00, #00FF00, #0000FF, #2E2B5F, #8B00FF. I'm looking for one word, case sensitive", "mcMenu"]
    ]

    flag = [["Janet> What? That cant be! What do you think the answer is?", "Finland", "chapterEND"]]
    wrongFlag = [["Janet> Hah, I knew it couldn't be! Come back when you have te right answer!", "mcMenu"]]

class chapterEND:
    dialog1 = [
    ["Janet> ...................", 0],
    ["Janet> Woah", 0],
    ["Janet> I can believe it, you bested me!", 0],
    ["System> You are now admin.", 0],
    ["Janet> What do you want me to do, boss?", 0],
    ["You> Shut down, NOW!", 0],
    ["Janet> Okay, goodbye.", "exit"]
    ]

    exit = [
    ["Congratulations! You completed the pad_T22 story: Bad Janet.", 0],
    ["end", "back"]
    ]

    back = [
    ["Janet is offline....", 0],
    ["end", "back"]
    ]
