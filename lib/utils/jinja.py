import jinja2
import os

base_path = os.path.join(os.path.dirname(__file__), "../../templates/")

jinja_engine = jinja2.Environment(
    loader=jinja2.FileSystemLoader([
        base_path
    ]),
)