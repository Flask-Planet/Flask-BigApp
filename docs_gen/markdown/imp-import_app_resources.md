```
Menu = Imp./import_app_resources
Title = Imp.import_app_resources
```

```python
import_app_resources(
    folder: str = "global",
    app_factories: Optional[List] = None,
    static_folder: str = "static",
    templates_folder: str = "templates",
    scope_root_folders_to: Optional[List] = None,
    scope_root_files_to: Optional[List] = None,
) -> None
```

Import standard app resources from the specified folder.

This will import any resources that have been set to the Flask app.

Routes, context processors, cli, etc.

**Can only be called once.**

If no static and or template folder is found, the static and or template folder will be set to None in the Flask app
config.

---

**Small example of usage:**

```python
imp.import_app_resources(folder="global")
```

**`global` folder structure**

```text
app
├── global
│   ├── routes.py
│   ├── app_fac.py
│   ├── static
│   │   └── css
│   │       └── style.css
│   └── templates
│       └── index.html
└── ...
...
```

**`routes.py` file**

```python
from flask import current_app as app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")
```

### app_factories

`app_factories` are functions that are called when importing the app resources. Here's an example:

```python
imp.import_app_resources(
    folder="global",
    app_factories=["development_cli"]
)
```

`["development_cli"]` => `development_cli(app)` function will be called, and the current app will be passed in.

**`app_fac.py` file**

```python
def development_cli(app):
    @app.cli.command("dev")
    def dev():
        print("dev cli command")
```

### scope_root_folders_to & scope_root_files_to

`scope_root_folders_to=["cli", "routes"]` => will only import files from `<folder>/cli/*.py`
and `<folder>/routes/*.py`

`scope_root_files_to=["cli.py", "routes.py"]` => will only import the files `<folder>/cli.py`
and `<folder>/routes.py`