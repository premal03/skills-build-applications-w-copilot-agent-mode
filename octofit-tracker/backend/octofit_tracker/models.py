
# MongoDB-based models (for structure/documentation only)
class User:
    def __init__(self, email, name, password, team_id=None, points=0):
        self.email = email
        self.name = name
        self.password = password
        self.team_id = team_id
        self.points = points

class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

class Activity:
    def __init__(self, user_id, activity_type, duration, date, points):
        self.user_id = user_id
        self.activity_type = activity_type
        self.duration = duration
        self.date = date
        self.points = points

class Leaderboard:
    def __init__(self, team_id, total_points):
        self.team_id = team_id
        self.total_points = total_points

class Workout:
    def __init__(self, name, description, suggested_by, difficulty):
        self.name = name
        self.description = description
        self.suggested_by = suggested_by
        self.difficulty = difficulty
