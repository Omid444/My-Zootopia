import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)



def print_characteristics(animals_info):
    for animal in animals_info:
        try:
            name = animal['name']
            diet = animal['characteristics']['diet']
            location = animal['locations'][0]
            type = animal['characteristics']['type']

            print(f"Name:{name}")
            print(f"Diet:{diet}")
            print(f"Location:{location}")
            print(f"Type:{type}")
        except KeyError:
            continue





def main():
    animals_data = load_data('animals_data.json')
    print_characteristics(animals_data)


if __name__ == "__main__":
    main()