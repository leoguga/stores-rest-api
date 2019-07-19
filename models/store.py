from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    # when lazy = 'dynamic' is used, then we must use self.items.all()
    items = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return { 'name': self.name, 'items': [ item.json() for item in self.items.all() ] }

    @classmethod
    def find_by_name(cls, name):
        # SELECT * FROM __tablename__ WHERE name = <name> LIMIT 1
        return cls.query.filter_by(name = name).first()

    # insert and update
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
