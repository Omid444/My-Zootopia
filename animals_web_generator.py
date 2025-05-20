import json


from bs4 import BeautifulSoup
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_characteristics(animals_info):
    output =''
    for animal in animals_info:
        try:
            name = animal['name']
            diet = animal['characteristics']['diet']
            location = animal['locations'][0]
            type = animal['characteristics']['type']

            single_animal_info = f"\nName:{name}\nDiet:{diet}\nLocation:{location}\nType:{type}\n"
            output += single_animal_info
            #print(output)

        except KeyError:
            continue
    return output


def read_html(file_path, animals_info):
    with open(file_path, "r") as html_file:
        index = html_file.read()
        soup = BeautifulSoup(index, 'html.parser')
        target = soup.find('ul', class_="cards")
        print(target.text)
        print(type(animals_info))
        content_file = index.replace(target.text, animals_info)
        return content_file

def write_html(file_path, index):
    with open(file_path, "w") as html_file:
        html_file.write(index)


def main():
    animals_data = load_data('animals_data.json')
    animals = get_characteristics(animals_data)
    #print(animals)
    index = read_html('animals_template.html', animals)
    write_html('animals_template.html', index)

if __name__ == "__main__":
    main()