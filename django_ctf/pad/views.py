from django.shortcuts import render
from .forms import flagCheck

def index(request):
    javascript = ""
    challenges = [  # [naam, key,beschrijving, moeilijkheid, evt bestand]
        ["Acceptance", "pad_t22/namiddag kiezerslijst aardappeleter\\", "Are you ready to comply?", "&#11088", " "],
        ["Into the Cloud", "pad_t22/darkness\\", "The more there is of me the less you see. What am I?", "&#11088", "Cloud.png"],
        ["Metamorphosis", "pad_t22/Emily_Dickinson\\","Chaos theory", "&#11088", "Metamorphosis.txt"],
        ["The matrix", "pad_t22/Thematrix_Flag\\","What is real?", "&#11088&#11088", "Thematrix.png"],
        ["Mysterious Sound", "pad_t22/mp3\\", "Can you hear me?", "&#11088&#11088", "MysteriousSound.wav"],
        ["Nested Picture", "pad_t22/Stegano234\\"," ", "&#11088&#11088&#11088", "Pictures.zip"],
        ["Alan Turing", "pad_t22/germansecret\\", "Could you find the code of the Army Staff Machine on the 31th of October 1944?", "&#11088&#11088", "germanww2.txt"],
        ["Geography", "pad_t22/Albania\\","Two-faced wizard met a hag", "&#11088&#11088&#11088", "Geography.png"],
        ["Ziplocked", "pad_t22/AWizardCalledTim\\","<a href='/error'> Ziplocked </a>", "&#11088&#11088&#11088", ""],
        ["Hidden strings", "pad_t22/pudding\\","Remove the intruders! (The flag should be submitted in lowercase)", "&#11088&#11088&#11088", "Hiddenstrings.zip"],
        ["Treasures", "pad_t22/locksmith\\"," ", "&#11088&#11088&#11088", "Treasures_Challenge.rar"],
        ["Phone home", "pad_t22/extraterrestrial\\"," ", "&#11088&#11088&#11088&#11088", "encoded.txt"],
        ["It's all about Hashing", "pad_t22/BlueGen--WeNeedBetterSecurity\\"," ", "&#11088&#11088&#11088", "Its-All-About-Hashing.zip"],
	    ["Lost Dog", "pad_t22/the machine is here\\","Jannet has the cypher tool", "&#11088&#11088&#11088&#11088&#11088", "Lost_dog.png"],
        ["Morsmors!", "pad_t22/earrape\\","Better turn your volumes up!", "&#11088&#11088&#11088", "MOUS.zip"],
        ["French Classic", "pad_t22/pink\\", "Bonjour", "&#11088&#11088&#11088&#11088&#11088", "FrenchClassic.zip"],
        ["Back To School", "pad_t22/TheSoundOfSilence\\","Are you ready to go back", "&#11088&#11088", "Back_To_School.zip"]

    ]

    if request.method == 'POST':
        postdata = flagCheck(request.POST)
        name = request.POST['submit']

        if postdata.is_valid():
            for challenge in challenges:
                if challenge[0] == name:
                    if postdata.cleaned_data['flag'] == challenge[1]:
                        javascript = "<script>window.alert('Correct!')</script>"
                    else:
                        javascript = "<script>window.alert('Sorry, try again')</script>"
                    break



    context = {
        'javascript': javascript,
        'form': flagCheck(),
        'challenges': challenges
    }
    return render(request, 'challenges.html', context)


def ziplocked(request):
    context = {}
    return render(request, 'error.html', context)
