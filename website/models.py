from . import db


affaire_commune = db.Table('affaire_commune',
                           db.Column('affaire_id', db.Integer, db.ForeignKey('affaire.id')),
                           db.Column('commune_id', db.Integer, db.ForeignKey('commune.id')))


class Affaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    departement_id = db.Column(db.Integer, db.ForeignKey('departement.id'))
    communes = db.relationship('Commune', secondary=affaire_commune, backref='affaires')
    preciser = db.Column(db.String(1000))


class Departement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    affaires = db.relationship('Affaire')
    communes = db.relationship('Commune')


class Commune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    departement_id = db.Column(db.Integer, db.ForeignKey('departement.id'))

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "departement_id": self.departement_id}
