"""Generate an HTML page with a card for every animal in animals_data.json."""
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
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    if characteristics.get("diet"):
        output += f"      <strong>Diet:</strong> {characteristics['diet']}<br/>\n"
    if locations:
        output += f"      <strong>Location:</strong> {locations[0]}<br/>\n"
    if characteristics.get("type"):
        output += f"      <strong>Type:</strong> {characteristics['type']}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n"

with open("animals_template.html", "r", encoding="utf-8") as template_file:
    template = template_file.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as html_file:
    html_file.write(html)
