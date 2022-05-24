# Flask-Launchpad

Flask-Launchpad is a small auto importer to import multiple blueprints and their routes. Can also handle multiple 
imports of flask_restx apis.

This extension allows you to make multiple route files and not have to worry about manually importing each of them.

!BEWARE! - This is an auto importer! - This can be a security concern!
Don't get lazy and ensure you know what code you are potentially going to run. 
(don't auto import files you've not looked at)

I've removed the example from here as I'm going through a little restructuring...

Check out the github for updates :)

[//]: # ()
[//]: # (Here's an example of how your project should look)

[//]: # (```)

[//]: # (Example folder structure :)

[//]: # (```)

[//]: # (```)

[//]: # (project/)

[//]: # (    - main/)

[//]: # (        - blueprints/)

[//]: # (            - example/)

[//]: # (                - templates/)

[//]: # (                - static/)

[//]: # (                - models/)

[//]: # (                    - models.py)

[//]: # (                    - models2.py)

[//]: # (                - routes/)

[//]: # (                    - route1.py)

[//]: # (                    - route2.py)

[//]: # (                - __init__.py)

[//]: # (                - config.toml)

[//]: # (            - example2/)

[//]: # (            - example3/)

[//]: # (        - api/)

[//]: # (            - v1/)

[//]: # (                - routes/)

[//]: # (                    api_route1.py)

[//]: # (                    api_route2.py)

[//]: # (                - __init__.py)

[//]: # (                - config.toml)

[//]: # (                - models.py)

[//]: # (                )
[//]: # (        - __init__.py)

[//]: # (        - app_config.toml)

[//]: # (        - templates/)

[//]: # (        - static/)

[//]: # (    - venv/)

[//]: # (    - run.py)

[//]: # (```)

[//]: # (```)

[//]: # (main/__init__.py :)

[//]: # (```)

[//]: # (```python)

[//]: # (from flask import Flask)

[//]: # (from flask_launchpad import FlaskLaunchpad)

[//]: # ()
[//]: # (# ~~ other imports)

[//]: # ()
[//]: # (fl = FlaskLaunchpad&#40;&#41;)

[//]: # ()
[//]: # (def create_app&#40;&#41;:)

[//]: # (    main = Flask&#40;__name__&#41;)

[//]: # (    fl.init_app&#40;main&#41;)

[//]: # (    )
[//]: # (    fl.app_config&#40;"app_config.toml"&#41;)

[//]: # (    fl.register_structure_folder&#40;"structures"&#41;)

[//]: # (    )
[//]: # (    fl.import_builtins&#40;"routes"&#41;)

[//]: # (    fl.import_builtins&#40;"another/folder/template_filters"&#41;)

[//]: # (    )
[//]: # (    fl.import_blueprints&#40;"blueprints"&#41;)

[//]: # (    fl.import_apis&#40;"api"&#41;)

[//]: # (    )
[//]: # (    # optional: you can specify a global model folder below, or add a model folder to each Blueprint or Api...)

[//]: # (    # ...or both, I suppose.)

[//]: # (    fl.models_folder&#40;"models"&#41;)

[//]: # ()
[//]: # (# ~~~ other create app things)

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # (.models_folder&#40;&#41; loads model files and classes into the apps config under current_app.config["models"] setting this)

[//]: # (in the app __init__.py is optional, and can be set in Blueprint config files if you would rather keep your models)

[//]: # (attached to your Blueprints.)

[//]: # ()
[//]: # (.app_config&#40;&#41; loads Flask env vars, database settings and email settings from a )

[//]: # (specified toml file that sits in the app root folder.)

[//]: # ()
[//]: # (.register_structure_folder&#40;&#41; registers a cut down Blueprint that will be added to the template folder lookups.)

[//]: # ()
[//]: # (.import_builtins&#40;&#41; imports basically app level routes that use @current_app.whatever, this)

[//]: # (can be used to import routes and template_filters for jinja as shown.)

[//]: # ()
[//]: # (.import_blueprints&#40;&#41; and .import_apis&#40;&#41; look in the folder passed in for Blueprint modules and registers them in)

[//]: # (Flask. This also includes model files by adding models_folder to the Blueprint config.)

[//]: # (```)

[//]: # (main/blueprints/example/app_config.toml :)

[//]: # (```)

[//]: # (```toml)

[//]: # (# Updates the Flask app config with the variables below.)

[//]: # (# If any variable below does not exist in the standard Flask env vars it is created and will be accessible using)

[//]: # (# current_app.config["YOUR_VAR_NAME"] or of course, app.config["YOUR_VAR_NAME"] if you are not using app factory.)

[//]: # ()
[//]: # ([flask])

[//]: # (name = "main")

[//]: # (secret_key = "sdflskjdflksjdflksjdflkjsdf")

[//]: # (debug = true)

[//]: # (testing = true)

[//]: # (session_time = 480)

[//]: # (static_folder = "static")

[//]: # (template_folder = "templates")

[//]: # (error_404_help = true)

[//]: # (SQLALCHEMY_TRACK_MODIFICATIONS = false)

[//]: # ()
[//]: # (# [database.main] is loaded as SQLALCHEMY_DATABASE_URI)

[//]: # (# type = mysql / postgresql / sqlite)

[//]: # (# if type = sqlite, config parser will ignore username and password)

[//]: # ([database])

[//]: # ()
[//]: # (    [database.main])

[//]: # (    enabled = true)

[//]: # (    type = "sqlite")

[//]: # (    server = "local")

[//]: # (    database_name = "database")

[//]: # (    username = "user")

[//]: # (    password = "password")

[//]: # ()
[//]: # (    # Anything below will be imported using SQLALCHEMY_BINDS, with the [SECTION] name being the __bind_key__)

[//]: # ()
[//]: # (    [database.example1])

[//]: # (    enabled = false)

[//]: # (    type = "mysql")

[//]: # (    server = "0.0.0.0")

[//]: # (    database_name = "example1")

[//]: # (    username = "user")

[//]: # (    password = "password")

[//]: # ()
[//]: # (    [database.example2])

[//]: # (    enabled = false)

[//]: # (    type = "mysql")

[//]: # (    server = "localhost")

[//]: # (    database_name = "example2")

[//]: # (    username = "user")

[//]: # (    password = "password")

[//]: # ()
[//]: # (# works well with Microsoft Exchange Kiosk License)

[//]: # (# for Exchange Kiosk to work you must enable Authenticated-SMTP in the accounts features)

[//]: # (# this feature takes a while to activate, so don't expect instant results)

[//]: # ()
[//]: # (# The name of the key is used as the username to login to the server defined below.)

[//]: # (# If your username is different uncomment alt_username and set it there)

[//]: # ([smtp])

[//]: # ()
[//]: # (    [smtp."email@email.com"])

[//]: # (    enabled = false)

[//]: # (    password = "password")

[//]: # (    server = "smtp-mail.outlook.com")

[//]: # (    port = 587)

[//]: # (    send_from = "email@emial.com")

[//]: # (    reply_to = "email@emial.com")

[//]: # (    #alt_username = "username")

[//]: # ()
[//]: # (    [smtp."email2@email.com"])

[//]: # (    enabled = false)

[//]: # (    password = "password")

[//]: # (    server = "smtp-mail.outlook.com")

[//]: # (    port = 587)

[//]: # (    send_from = "email@emial.com")

[//]: # (    reply_to = "email@emial.com")

[//]: # (    #alt_username = "username")

[//]: # ()
[//]: # (```)

[//]: # (```)

[//]: # (main/blueprints/example/__init__.py :)

[//]: # (```)

[//]: # (```python)

[//]: # (from flask_launchpad import FLBlueprint)

[//]: # (from flask import session)

[//]: # ()
[//]: # (fl_bp = FLBlueprint&#40;&#41;)

[//]: # (bp = fl_bp.register&#40;&#41;)

[//]: # (fl_bp.import_routes&#40;"routes"&#41;)

[//]: # ()
[//]: # (@bp.before_app_first_request)

[//]: # (def before_app_first_request&#40;&#41;:)

[//]: # (    session.update&#40;fl_bp.session&#41;)

[//]: # ()
[//]: # ()
[//]: # (@bp.before_app_request)

[//]: # (def before_app_request&#40;&#41;:)

[//]: # (    pass)

[//]: # ()
[//]: # ()
[//]: # (@bp.after_app_request)

[//]: # (def after_app_request&#40;response&#41;:)

[//]: # (    return response)

[//]: # ()
[//]: # (```)

[//]: # (```)

[//]: # (main/blueprints/example/config.toml :)

[//]: # (```)

[//]: # (```toml)

[//]: # ([init])

[//]: # (enabled = true)

[//]: # (version = 0.1)

[//]: # ()
[//]: # ([settings])

[//]: # (type = "blueprint")

[//]: # (models_folder = "models")

[//]: # (# models_folder is optional, see app __init__.py above for more info)

[//]: # ()
[//]: # ([blueprint])

[//]: # (url_prefix = "/example")

[//]: # (template_folder = "templates")

[//]: # (static_folder = "static")

[//]: # (static_url_path = "/static")

[//]: # ()
[//]: # ([session])

[//]: # (var_in_session = "this can be loaded using fl_bp.session")

[//]: # ()
[//]: # (```)

[//]: # (```)

[//]: # (main/blueprints/example/routes/route1.py :)

[//]: # (```)

[//]: # (```python)

[//]: # (from .. import bp)

[//]: # ()
[//]: # ()
[//]: # (@bp.route&#40;"/", methods=["GET"]&#41;)

[//]: # (def index&#40;&#41;:)

[//]: # (    """Example of route url redirect""")

[//]: # (    return """Working...""")

[//]: # (```)

[//]: # (```)

[//]: # (main/blueprints/example/models/models.py :)

[//]: # (```)

[//]: # (```python)

[//]: # (from sqlalchemy.orm import relationship)

[//]: # (from .. import db)

[//]: # ()
[//]: # ()
[//]: # (class Example1&#40;db.Model&#41;:)

[//]: # (    __tablename__ = "example1")

[//]: # (    example1_id = db.Column&#40;db.Integer, primary_key=True&#41;)

[//]: # (    username = db.Column&#40;db.String&#40;256&#41;, nullable=False&#41;)

[//]: # (    password = db.Column&#40;db.String&#40;512&#41;, nullable=False&#41;)

[//]: # (    fk_details = relationship&#40;"Example2"&#41;)

[//]: # (```)

[//]: # ()
[//]: # (import_apis&#40;&#41; from the main / init file, works much the same as the blueprint imports, although it prepends the blueprint holding folder into the URL registration.)

[//]: # ()
[//]: # (In this example the v1 API folder with be registered against /api/v1)

[//]: # ()
[//]: # (Here's an example of how the files should look to register APIs)

[//]: # ()
[//]: # (```)

[//]: # (main/api/v1/__init__.py :)

[//]: # (```)

[//]: # (```python)

[//]: # (from flask_restx import Api)

[//]: # (from flask_launchpad import FLBlueprint)

[//]: # ()
[//]: # (fl_bl = FLBlueprint&#40;&#41;)

[//]: # (api_bp = fl_bl.register&#40;&#41;)

[//]: # (api = Api&#40;api_bp, doc=f"/docs"&#41;)

[//]: # (fl_bl.import_routes&#40;&#41;)

[//]: # (# import_routes&#40;&#41; defaults to a folder called routes)

[//]: # (```)

[//]: # (```)

[//]: # (main/api/v1/config.toml :)

[//]: # (```)

[//]: # (```toml)

[//]: # ([init])

[//]: # (enabled = true)

[//]: # (version = 1.0)

[//]: # ()
[//]: # ([settings])

[//]: # (type = "api")

[//]: # (models_folder = "folder")

[//]: # ()
[//]: # ([blueprint])

[//]: # (url_prefix = "/v1")

[//]: # ()
[//]: # ([http_auth])

[//]: # (enabled = false)

[//]: # (http_user = "httpuser")

[//]: # (http_pass = "httppass")

[//]: # ()
[//]: # ([public_key])

[//]: # (enabled = false)

[//]: # (public_key = "a3oe3qhY8knm")

[//]: # (```)

[//]: # (```)

[//]: # (main/api/v1/routes/api_route1.py :)

[//]: # (```)

[//]: # (```python)

[//]: # (from flask_restx import Resource)

[//]: # ()
[//]: # (from .. import api)

[//]: # ()
[//]: # ()
[//]: # (@api.route&#40;'/test'&#41;)

[//]: # (class Test&#40;Resource&#41;:)

[//]: # (    def get&#40;self&#41;:)

[//]: # (        return "waiting")

[//]: # (```)

[//]: # ()
[//]: # (Sticking to this method of blueprints and APIs will allow you to mass import route files.)