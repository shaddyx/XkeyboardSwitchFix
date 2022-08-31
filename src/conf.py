import yaml

conf_file = './kb_switch.yml'


def load():
    with open(conf_file, 'r') as f:
        return yaml.safe_load(f)
