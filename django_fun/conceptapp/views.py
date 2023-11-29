from django.shortcuts import render

# Create your views here.


def home(request):
    d = {"name": "django", "list": ["rakib", "sakib", "akib", "nakib"]}
    return render(request, "home.html", d)


def context(request):
    d = {
        "letters": ["a", "b", "c", "d"],
        "num": 22,
        "quotes": "Turu Love",
        "greetings": "she's shanti",
        "name": "bodnam",
        "status": "",
        "guys": [
            {"name": "zed", "age": 19},
            {"name": "amy", "age": 22},
            {"name": "joe", "age": 31},
        ],
        "file": 123456789,
    }
    return render(request, "context.html", d)
