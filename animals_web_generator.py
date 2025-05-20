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
            animal_type = animal['characteristics']['type']
            animal_object = (name, diet, location, animal_type)
            if all(animal_object):
                single_animal_info = serialize_animal(animal_object)
                output += single_animal_info
                print('output',output)
            else:
                continue
        except KeyError:
            continue
    return output


def serialize_animal(animal_obj):
    name, diet, location, animal_type = animal_obj
    tag_start = '<li class="cards__item">'
    tag_end = '</li>'
    text = f"\nName:{name}<br/>\nDiet:{diet}<br/>\nLocation:{location}<br/>\nType:{animal_type}<br/>\n"
    final_text = tag_start + text + tag_end
    return final_text


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