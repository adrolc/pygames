import json

MAX_WIDTH = 1920
MAX_HEIGHT = 1080
MIN_FIELD_SIZE = 2


def load_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {
            "field_size": 7,
            "fields_in_row": 108,
            "fields_in_col": 192,
            "draw_visited_fields_speed": 10,
            "draw_found_path_speed": 10,
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

    validate_config(config)
    return config


def validate_config(config):
    if config["field_size"] < MIN_FIELD_SIZE:
        raise ValueError("Field size must be greater than 1")
    if (config["field_size"] * config["fields_in_row"]) > MAX_HEIGHT:
        raise ValueError("Width of maze is too large")
    if (config["field_size"] * config["fields_in_col"]) > MAX_WIDTH:
        raise ValueError("Height of maze is too large")
