# Test data for OctoFit Tracker (based on monafit tracker example)

test_users = [
    {"email": "alice@example.com", "name": "Alice", "password": "pass1", "team_id": "team1", "points": 120},
    {"email": "bob@example.com", "name": "Bob", "password": "pass2", "team_id": "team1", "points": 95},
    {"email": "carol@example.com", "name": "Carol", "password": "pass3", "team_id": "team2", "points": 110}
]

test_teams = [
    {"name": "Team 1", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team 2", "members": ["carol@example.com"]}
]

test_activities = [
    {"user_id": "alice@example.com", "activity_type": "running", "duration": 30, "date": "2025-06-01", "points": 30},
    {"user_id": "bob@example.com", "activity_type": "walking", "duration": 60, "date": "2025-06-01", "points": 20},
    {"user_id": "carol@example.com", "activity_type": "cycling", "duration": 45, "date": "2025-06-01", "points": 25}
]

test_leaderboard = [
    {"team_id": "Team 1", "total_points": 215},
    {"team_id": "Team 2", "total_points": 110}
]

test_workouts = [
    {"name": "Morning Run", "description": "Run 5km in the morning", "suggested_by": "Coach Paul", "difficulty": "Medium"},
    {"name": "Pushup Challenge", "description": "50 pushups in one go", "suggested_by": "Coach Paul", "difficulty": "Hard"}
]
