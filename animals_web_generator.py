"""Generate an HTML page with the data of every animal in animals_data.json."""
import json


def load_data(file_path):
    """Load and return the data of a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")
output = ""
for animal in animals_data:
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])
    if animal.get("name"):
        output += f"Name: {animal['name']}\n"
    if characteristics.get("diet"):
        output += f"Diet: {characteristics['diet']}\n"
    if locations:
        output += f"Location: {locations[0]}\n"
    if characteristics.get("type"):
        output += f"Type: {characteristics['type']}\n"
    output += "\n"

with open("animals_template.html", "r", encoding="utf-8") as template_file:
    template = template_file.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as html_file:
    html_file.write(html)
