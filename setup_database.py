from main import db, Patient

db.create_all()

reuven = Patient(111111111, "Reuven", "cohen","rashi 10 jerusalem", "25/8/1989","025874965","0584878996")

db.session.add(reuven)

db.session.commit()
print(reuven.id)