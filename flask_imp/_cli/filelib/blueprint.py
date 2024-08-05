def blueprint_init_py(url_prefix: str, name: str) -> str:
    return f"""\
from flask_imp import ImpBlueprint
from flask_imp.config import ImpBlueprintConfig

bp = Blueprint(__name__, ImpBlueprintConfig(
    enabled=True,
    url_prefix="/{url_prefix}",
    init_session={{ "{name}_session_loaded": True }},
))

bp.import_resources("routes")
"""


def blueprint_routes_index_py():
    return """\
from flask import render_template

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    return render_template(bp.tmpl("index.html"))
"""


def blueprint_templates_index_html(name: str, root: str) -> str:
    return f"""\
{{% extends '{name}/extends/main.html' %}}

{{% block content %}}
    <div style="display: flex; flex-direction: row; align-items: center; gap: 2rem; margin-bottom: 2rem;">
        <div>
            <h2 style="margin: 0;">Blueprint: {name}</h2>
            <h3>Here's your new blueprint.</h3>
            <p>Located here: <code>{root}</code></p>
            <p style="margin-bottom: 0;">Remember to double-check the config.toml file.</p>
        </div>
    </div>
{{% endblock %}}
"""


def blueprint_init_app_templates_index_html(
        name: str, index_html: str, extends_main_html: str, index_py: str, init_py: str
):
    return f"""\
{{% extends 'www/extends/main.html' %}}

{{% block content %}}
<div style="display: flex; flex-direction: row; align-items: center; gap: 2rem; margin-bottom: 2rem;">
    <div>
        <h2 style="margin: 0;">Blueprint: {name}</h2>
        <h3>This is the index route of the included example blueprint.</h3>
        <p style="margin-bottom: 0;">
            This template page is located in <code>{index_html}</code><br/>
            it extends from <code>{extends_main_html}</code><br/>
            with its route defined in <code>{index_py}</code><br/><br/>
            It's being imported by <code>bp.import_resources("routes")</code>
            in the <code>{init_py}</code> file.
        </p>
    </div>
</div>
{{% endblock %}}
"""


def blueprint_templates_extends_main_html(
        name: str, head_tag: str
):
    return f"""\
<!doctype html>

<html lang="en">
<head>
    {head_tag}
</head>

<body>
{{% include '{name}/includes/header.html' %}}
{{% block content %}}{{% endblock %}}
{{% include '{name}/includes/footer.html' %}}
</body>

</html>
"""


def blueprint_templates_includes_header_html(
        header_html: str, main_html: str, static_path: str
):
    return f"""\
<div style="display: flex; flex-direction: row; align-items: center;
            justify-content: start; gap: 2rem; margin-bottom: 2rem;">
    <img style="border-radius: 50%"
         src="{{{{ url_for('{static_path}', filename='img/flask-imp-logo.png') }}}}" alt="flask-imp logo">
    <h1 style="font-size: 4rem;">Flask-Imp</h1>
</div>
<div style="margin-bottom: 2rem;">
    <p>This is the header, located here: <code>{header_html}</code></p>
    <p>It's being imported in the <code>{main_html}</code> template.</p>
</div>
"""


# Format to: footer_html, main_html
def blueprint_templates_includes_footer_html(
        footer_html: str, main_html: str
):
    f"""\
<div style="display: flex; flex-direction: row; align-items: center; gap: 2rem; margin-bottom: 2rem;">
    <div>
        <p>This is the footer, located here: <code>{footer_html}</code></p>
        <p>It's being imported in the <code>{main_html}</code> template.</p>
    </div>
</div>
"""
