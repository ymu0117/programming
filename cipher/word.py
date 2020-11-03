import yaml
import json 


def load_dictionary(path):
    with open(path) as file:
        dictionary = yaml.load(file)
    return dictionary


def load_Webster(path):
    """Load Webster dictionary in json format."""
    dictionary = json.load(open(path))
    return dictionary 











    
