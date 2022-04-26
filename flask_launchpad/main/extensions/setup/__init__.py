from importlib import import_module
from os import path

from flask import Blueprint
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from ...builtins.functions.database import find_model_location
from ...builtins.functions.import_mgr import import_routes
from ...builtins.functions.import_mgr import read_config
from ...builtins.functions.structure import StructureBuilder

"""
This is an example blueprint init file.
1. Config file is loaded into a dict and the arguments are passed direct to the blueprint object
2. Root path is set to allow the static url path to work
3. SQLAlchemy object is created
4. database session is set to sql_do to make it easier to read and use in sql action files
5. init a dict variable to get external model attributes
6. Pull blueprint models from the current app config, import and store in dict
. routes in the routes folder of the blueprint are imported
"""

config = read_config(filepath=path.dirname(path.realpath(__file__)))
bp = Blueprint(**config["settings"], root_path=path.dirname(path.realpath(__file__)))

db = SQLAlchemy()
sql_do = db.session

account_model = import_module(find_model_location("account"))
FlUser = getattr(account_model, "FlUser")

administrator_model = import_module(find_model_location("administrator"))
FlPermissions = getattr(account_model, "FlPermissions")
FlPermissionsMembership = getattr(account_model, "FlPermissionsMembership")
FlClan = getattr(account_model, "FlClan")
FlClanMembership = getattr(account_model, "FlClanMembership")
FlTeam = getattr(account_model, "FlTeam")
FlTeamMembership = getattr(account_model, "FlTeamMembership")

system_model = import_module(find_model_location("system"))
FlSystemSettings = getattr(system_model, "FlSystemSettings")

struc = StructureBuilder(current_app.config["STRUCTURE"])

for route in import_routes(module_folder="extensions", module=config["settings"]["name"]):
    import_module(f"{current_app.config['APP_NAME']}.extensions.{config['settings']['name']}.routes.{route}")
