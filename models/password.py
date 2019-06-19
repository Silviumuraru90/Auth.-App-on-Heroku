# from db import db


# class PassModel(db.Model):
#     __tablename__ = 'pass'

#     id = db.Column(db.Integer, primary_key=True)
#     password = db.Column(db.String(80))

#     def __init__(self, password):
#         self.password = password

#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def find_by_id(cls, _id):
#         return cls.query.filter_by(id=_id).first()