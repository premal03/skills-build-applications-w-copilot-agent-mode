from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
#\-8000.app.github.dev
#\-8000.app.github.dev

def api_root(request):
    return JsonResponse({
        "users": "https:/laughing-umbrella-rq767w6p9wpcx66r.github.dev/-8000.app.github.dev/users/",
        "teams": "https://laughing-umbrella-rq767w6p9wpcx66r.github.dev-8000.app.github.dev/teams/",
        "activity": "https://laughing-umbrella-rq767w6p9wpcx66r.github.dev-8000.app.github.dev/activity/",
        "leaderboard": "https://laughing-umbrella-rq767w6p9wpcx66r.github.dev-8000.app.github.dev/leaderboard/",
        "workouts": "https://laughing-umbrella-rq767w6p9wpcx66r.github.dev-8000.app.github.dev/workouts/"
    })