import yaml 


def load_dictionary(path):
    with open(path) as file:
        dictionary = yaml.load(file)

    return dictionary











    
