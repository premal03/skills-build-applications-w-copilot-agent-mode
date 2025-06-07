from django.core.management.base import BaseCommand
import pymongo
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Test data (replace with actual data from docs/mona-high-school-fitness-tracker.md)
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "pass1", "team_id": "team1", "points": 120},
            {"email": "bob@example.com", "name": "Bob", "password": "pass2", "team_id": "team1", "points": 95},
            {"email": "carol@example.com", "name": "Carol", "password": "pass3", "team_id": "team2", "points": 110}
        ]
        teams = [
            {"name": "Team 1", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team 2", "members": ["carol@example.com"]}
        ]
        activities = [
            {"user_id": "alice@example.com", "activity_type": "running", "duration": 30, "date": "2025-06-01", "points": 30},
            {"user_id": "bob@example.com", "activity_type": "walking", "duration": 60, "date": "2025-06-01", "points": 20},
            {"user_id": "carol@example.com", "activity_type": "cycling", "duration": 45, "date": "2025-06-01", "points": 25}
        ]
        leaderboard = [
            {"team_id": "Team 1", "total_points": 215},
            {"team_id": "Team 2", "total_points": 110}
        ]
        workouts = [
            {"name": "Morning Run", "description": "Run 5km in the morning", "suggested_by": "Coach Paul", "difficulty": "Medium"},
            {"name": "Pushup Challenge", "description": "50 pushups in one go", "suggested_by": "Coach Paul", "difficulty": "Hard"}
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
