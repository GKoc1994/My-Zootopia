"""Generate an HTML page with a card for every animal in animals_data.json."""
import json

DATA_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Load and return the data of a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_file(file_path):
    """Return the content of a text file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_file(file_path, content):
    """Write the content to a text file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def get_animal_details(animal):
    """
    Return a list of (label, value) pairs for the card of one animal.
    Fields that are missing in the data are left out.
    """
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])
    details = [
        ("Diet", characteristics.get("diet")),
        ("Location", locations[0] if locations else None),
        ("Type", characteristics.get("type")),
    ]
    return [(label, value) for label, value in details if value]


def serialize_animal(animal):
    """Return the HTML list item (card) for one animal."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    for label, value in get_animal_details(animal):
        output += f"      <strong>{label}:</strong> {value}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n"
    return output


def serialize_animals(animals):
    """Return the HTML cards of all animals as one string."""
    return "".join(serialize_animal(animal) for animal in animals)


def main():
    """Read the animal data, build the cards and write the HTML page."""
    animals = load_data(DATA_FILE)
    template = read_file(TEMPLATE_FILE)
    html = template.replace(PLACEHOLDER, serialize_animals(animals))
    write_file(OUTPUT_FILE, html)
    print(f"Website was successfully generated to the file {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
