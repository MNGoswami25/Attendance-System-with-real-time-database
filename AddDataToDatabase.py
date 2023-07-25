
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-933ce-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={

    "210111126":
        {
            "name":"Manoj Nath Goswami",
            "major":"CSE",
            "starting_year":2021,
            "total_attendance":6,
            "standing":"G",
            "year":3,
            "Last_attendance_time":"2023-05-21 00:54:34"
        },
    "210121622":
        {
            "name":"Pooja Joshi",
            "major":"CSE",
            "starting_year":2021,
            "total_attendance":10,
            "standing":"V.G",
            "year":3,
            "Last_attendance_time":"2023-05-21 00:55:34"
        },
    "210112233":
        {
            "name":"Mahak Saxena",
            "major":"CSE",
            "starting_year":2021,
            "total_attendance":8,
            "standing":"G",
            "year":3,
            "Last_attendance_time":"2023-05-21 00:53:34"
        },
    "210111145":
        {
            "name": "Sangeeta Chawla",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "Last_attendance_time": "2023-05-21 00:53:34"
        }



}

for key,value in data.items():
    ref.child(key).set(value)
