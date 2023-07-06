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
            new_affaire = Affaire(name=name, departement_id=departement, preciser=preciser)

            commune_ids = request.form.getlist('commune')
            for commune_id in commune_ids:
                commune = Commune.query.filter_by(id=commune_id).first()
                if commune and commune.departement_id == int(departement):
                    new_affaire.communes.append(commune)

            db.session.add(new_affaire)
            db.session.commit()
    return render_template("base.html", communes=Commune.query.all(), departements=Departement.query.all())

