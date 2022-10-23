from main import db, Patient


# create_all
shimon = Patient(2222222222, "Shimon", "cohen","rashi 10 jerusalem", "25/8/1989","025874965","0584878996")
levi =  Patient(333333333, "Levi", "lev","rashi 10 jerusalem", "25/8/1989","025874965","0584878996")
israe =  Patient(444444444, "Israel", "chen","rashi 10 jerusalem", "25/8/1989","025874965","0584878996")
david =  Patient(555555555, "David", "mori","rashi 10 jerusalem", "25/8/1989","025874965","0584878996")
db.session.add_all([shimon, levi, israe, david])
db.session.commit()

# by filter


# update
def update_patient(id):
    update = Patient.query.get(id)
    #TODO: add another option to update.
    db.session.add(update)
    db.session.commit()

# delete
delete = Patient.query.get(2)
db.session.delete(delete)
db.session.commit()

# read

# by # ID
id = Patient.query.get(1)
print(id)
print('\n')

# all
all = Patient.query.all()
print(all)
print('\n')