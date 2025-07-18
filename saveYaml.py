import yaml
import os
from pathlib import Path
import yaml
from pyaml import dump

def get_config_path():
    # Get the user home directory
    home = Path.home()

    
    config_dir = home / '.shippingForms'
    config_dir.mkdir(exist_ok=True)  # create if doesn't exist

    # YAML config file path
    config_file = config_dir / 'config.yaml'

    return config_file

def load_config():
    config_file = get_config_path()
    if config_file.exists():
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    else:
        # Return default config if file doesn't exist
        return {}

def save_config(data):
    config_file = get_config_path()
    with open(config_file, 'w') as f:
        f.write(dump(data))

