from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv
import flask_sqlalchemy


db = SQLAlchemy()


from .models import Affaire, Departement, Commune


def create_departements_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        departements = []
        for row in reader:
            departement_name = row[0]
            departement = Departement.query.filter_by(name=departement_name).first()
            if not departement:
                departement = Departement(name=departement_name)
                departements.append(departement)
        db.session.add_all(departements)
        db.session.commit()


def create_communes_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        communes = []
        for row in reader:
            commune_name = row[1]
            departement_name = row[0]
            departement = Departement.query.filter_by(name=departement_name).first()
            commune = Commune.query.filter_by(name=commune_name).first()
            if departement and not commune:
                commune = Commune(name=commune_name, departement_id=departement.id)
                communes.append(commune)
        db.session.add_all(communes)
        db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')


    with app.app_context():
        db.drop_all()
        db.create_all()
        csv_departement_file = 'csv/departement.csv'
        csv_commune_file = 'csv/commune.csv'

        create_departements_from_csv(csv_departement_file)
        create_communes_from_csv(csv_commune_file)
        print('Database created!')

    return app




