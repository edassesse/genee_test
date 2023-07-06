from flask import Blueprint, flash, render_template, request
from .models import Affaire, Commune, Departement
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def create_affaire():
    if request.method == 'POST':
        name = request.form.get('name')
        if len(name) > 0:
            departement = request.form.get('departement')
            preciser = request.form.get('preciser')
            departement_id = Departement.query.filter_by(name=departement).first().id
            new_affaire = Affaire(name=name, departement_id=departement_id, preciser=preciser)

            commune_names = request.form.getlist('commune')
            for commune_name in commune_names:
                commune = Commune.query.filter_by(name=commune_name).first()
                if (commune.departement_name == departement):
                    new_affaire.communes.append(commune)

            db.session.add(new_affaire)
            db.session.commit()
    return render_template("base.html", communes=Commune.query.all(), departements=Departement.query.all())


@views.route('/communes', methods=['GET'])
def get_communes():
    communes = Commune.query.all()
    print("on vient oui oui")
    return "oui"
