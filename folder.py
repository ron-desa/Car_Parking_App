import os

# Define the folder and file structure
structure = {
    "parking_app_22f1000876": {
        "app.py": "",
        "controllers": {
            "__init__.py": "",
            "routes.py": "# app routes here"
        },
        "models": {
            "__init__.py": "",
            "models.py": "# SQLAlchemy models here"
        },
        "static": {
            "css": {},
            "js": {}
        },
        "templates": {
            "base.html": "<!-- common layout -->",
            "login.html": "",
            "register.html": "",
            "dashboard_user.html": "",
            "dashboard_admin.html": "",
            "book_parking.html": "",
            "release_parking.html": ""
        }
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Run the script from current directory
create_structure('.', structure)
