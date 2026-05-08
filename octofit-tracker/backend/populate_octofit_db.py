from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Cancella dati esistenti
db.users.delete_many({})
db.teams.delete_many({})
db.activities.delete_many({})
db.leaderboards.delete_many({})
db.workouts.delete_many({})

# Crea team
marvel_id = db.teams.insert_one({'name': 'Marvel'}).inserted_id
dc_id = db.teams.insert_one({'name': 'DC'}).inserted_id

# Crea utenti
users = [
    {'email': 'tony@stark.com', 'username': 'IronMan', 'team_id': marvel_id},
    {'email': 'steve@rogers.com', 'username': 'CaptainAmerica', 'team_id': marvel_id},
    {'email': 'bruce@wayne.com', 'username': 'Batman', 'team_id': dc_id},
    {'email': 'clark@kent.com', 'username': 'Superman', 'team_id': dc_id},
]
user_ids = db.users.insert_many(users).inserted_ids

# Crea attività
activities = [
    {'user_id': user_ids[0], 'type': 'run', 'duration': 30, 'distance': 5},
    {'user_id': user_ids[1], 'type': 'cycle', 'duration': 45, 'distance': 20},
    {'user_id': user_ids[2], 'type': 'swim', 'duration': 60, 'distance': 2},
    {'user_id': user_ids[3], 'type': 'run', 'duration': 25, 'distance': 4},
]
db.activities.insert_many(activities)

# Crea workout
workouts = [
    {'name': 'Morning Cardio', 'description': 'Cardio session'},
    {'name': 'Strength Training', 'description': 'Weights and resistance'},
]
db.workouts.insert_many(workouts)

# Crea leaderboard
leaderboards = [
    {'user_id': uid, 'points': 100} for uid in user_ids
]
db.leaderboards.insert_many(leaderboards)

# Indice unico su email
try:
    db.users.create_index('email', unique=True)
except Exception as e:
    print('Indice già esistente o errore:', e)

print('Database octofit_db popolato con dati di test.')
