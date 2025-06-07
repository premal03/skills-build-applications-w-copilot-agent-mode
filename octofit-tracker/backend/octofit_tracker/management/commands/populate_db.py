from django.core.management.base import BaseCommand
import pymongo
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activity, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Test data based on monafit example
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": "team1", "points": 120},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": "team1", "points": 100},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass", "team_id": "team2", "points": 150}
        ]
        teams = [
            {"name": "Team 1", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team 2", "members": ["carol@example.com"]}
        ]
        activity = [
            {"user_id": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2024-06-01", "points": 30},
            {"user_id": "bob@example.com", "activity_type": "walk", "duration": 60, "date": "2024-06-01", "points": 20},
            {"user_id": "carol@example.com", "activity_type": "cycle", "duration": 45, "date": "2024-06-01", "points": 40}
        ]
        leaderboard = [
            {"team_id": "team1", "total_points": 220},
            {"team_id": "team2", "total_points": 150}
        ]
        workouts = [
            {"name": "Morning Run", "description": "A quick 5k run.", "suggested_by": "Alice", "difficulty": "Medium"},
            {"name": "Yoga", "description": "30 minutes of yoga.", "suggested_by": "Carol", "difficulty": "Easy"}
        ]

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activity)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
