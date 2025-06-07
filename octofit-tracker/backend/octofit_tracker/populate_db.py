# Standalone script to populate octofit_db with test data
import pymongo
from test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB_NAME = "octofit_db"

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Clear existing data
print("Clearing existing data...")
db.users.delete_many({})
db.teams.delete_many({})
db.activity.delete_many({})
db.leaderboard.delete_many({})
db.workouts.delete_many({})

# Insert test data
print("Inserting test data...")
db.users.insert_many(test_users)
db.teams.insert_many(test_teams)
db.activity.insert_many(test_activities)
db.leaderboard.insert_many(test_leaderboard)
db.workouts.insert_many(test_workouts)

print("Test data populated successfully.")
