from flask import render_template

from .. import bp
from .. import struc
from ....builtins.functions.security import login_required


@bp.route("/elements", methods=["GET"])
@login_required("auth", "account.login")
def elements():
    render = "renders/elements.html"
    structure = struc.name()
    extend = struc.extend("backend.html")
    footer = struc.include("footer.html")

    return render_template(render, structure=structure, extend=extend, footer=footer)