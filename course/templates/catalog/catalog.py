from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    after_this_request,
    flash,
)
from sqlalchemy.sql.expression import func
from flask_login import login_required, current_user
import flask_login
from sqlalchemy.orm import session
from course.models import *
from course.templates.base.base_process import *
from course import db, photos
from course.forms import *
from course.utilities import *
import datetime, os

catalog = Blueprint("catalog", __name__)


@catalog.route("/", methods=["GET", "POST"])
@login_required
def main():
    
    catalogs = db.session.query(Catalog).filter(Catalog.userid == current_user.id).order_by(Catalog.course_code).all()
    context = {"user": User, "catalogs":catalogs}
    return render_template("/catalog/catalog_main.html", **context)


@catalog.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def filament_edit(id):

    db_fil = db.session.query(Filament).filter_by(id=id).first()
    form = Filament_form(obj=db_fil)
    if form.validate_on_submit():
        if form.picture.data:
            filename = photos.save(form.picture.data)
            ext = os.path.splitext(filename)
            newfile = str(form.name.data).replace(" ", "_").lower()
            db_fil.picture = newfile + ext[1]
            os.rename(
                "printing/static/images/" + filename,
                "printing/static/images/" + newfile + ext[1],
            )
        db_fil.name = form.name.data
        db_fil.color = form.color.data
        db_fil.colorhex = convert_color_to_hex(form.color.data)
        db_fil.priceperroll = form.priceperroll.data
        db_fil.length_spool = form.length_spool.data
        db_fil.diameter = form.diameter.data
        db_fil.url = form.url.data
        db_fil.purchasedate = form.purchasedate.data
        db_fil.vendorfk = form.vendorfk.data
        db_fil.typefk = form.typefk.data
        db_fil.userid = current_user.id
        db.session.commit()
        return redirect(form.referer.data)

    form.process(obj=db_fil)
    form.referer.data = request.referrer

    types = Type.query.all()
    context = {"user": User, "types": types, "form": form, "filament": db_fil}
    return render_template("/filament/filament_edit.html", **context)


@catalog.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def filament_delete(id):
    db.session.query(Filament).filter(Filament.id == id).delete()
    db.session.commit()
    return redirect(url_for("filament.filament_main"))
