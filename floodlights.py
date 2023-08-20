import tinytuya
import click
import logging
import configparser
import json
import os

# Define the configuration file path in the user's home directory
config_file_path = os.path.expanduser('~/.floodlights/config.ini')
config = configparser.ConfigParser()

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(config_file_path), exist_ok=True)

# Read the configuration file
config.read(config_file_path)

def configure():
    """Configure the floodlight settings."""
    device_id = click.prompt('Enter Device ID')
    device_ip = click.prompt('Enter Device IP')
    device_key = click.prompt('Enter Device Key')
    device_version = click.prompt('Enter Device Version')

    config['Floodlight'] = {
        'DEVICE_ID': device_id,
        'DEVICE_IP': device_ip,
        'DEVICE_KEY': device_key,
        'DEVICE_VERSION': device_version,
    }

    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

    click.echo('Configuration saved successfully!')

# Check if the configuration file exists and has the required section
if not os.path.exists(config_file_path) or not config.has_section('Floodlight'):
    configure()

# Set up logging with colorful output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addFilter(lambda record: setattr(record, 'color', 'green') or record)

class ConfigError(Exception):
    pass

def check_config():
    if not os.path.exists(config_file_path) or not config.has_section('Floodlight'):
        raise ConfigError('Configuration file is missing or malformed.')

class FloodlightController:
    def __init__(self):
        check_config()
        self.device_id = config.get('Floodlight', 'DEVICE_ID')
        self.device_ip = config.get('Floodlight', 'DEVICE_IP') or "Auto"
        self.device_key = config.get('Floodlight', 'DEVICE_KEY')
        self.device_version = config.get('Floodlight', 'DEVICE_VERSION')
        self.device = tinytuya.OutletDevice(self.device_id, self.device_ip, self.device_key)
        self.device.set_version(float(self.device_version))

    def on(self, brightness=None):
        if brightness:
            self.device.set_value(20, True)
            self.device.set_value(22, brightness)
            logger.info(f"Floodlights turned on with brightness {brightness}")
        else:
            self.device.set_value(20, True)
            logger.info("Floodlights turned on")

    def map_dps_values(self, dps):
        mapping = {
            "20": "Power State",
            "21": "Mode",
            "22": "Brightness",
            "25": "Unknown",
            "26": "Unknown"
        }
        output = {}
        for key, value in dps.items():
            mapped_key = mapping.get(key, f"Unknown Key {key}")
            output[mapped_key] = value
        return output

    def status(self):
        data = self.device.status()
        dps_data = self.map_dps_values(data['dps'])
        status_str = json.dumps({"devId": data['devId'], "dps": dps_data}, indent=4)
        logger.info(f"\nCurrent status of the device: \n{status_str}\n")
        return data

    def off(self):
        self.device.set_value(20, False)
        logger.info("Floodlights turned off")

@click.group()
def cli():
    pass

@click.command()
@click.option('--brightness', default=1000, type=int)
def on(brightness):
    controller = FloodlightController()
    controller.on(brightness)

@click.command()
def status():
    controller = FloodlightController()
    controller.status()

@click.command()
def off():
    controller = FloodlightController()
    controller.off()

@click.command()
@click.option('--device-id', prompt='Enter Device ID')
@click.option('--device-ip', prompt='Enter Device IP')
@click.option('--device-key', prompt='Enter Device Key')
@click.option('--device-version', prompt='Enter Device Version')
def configure(device_id, device_ip, device_key, device_version):
    """Configure the floodlight settings."""
    config['Floodlight'] = {
        'DEVICE_ID': device_id,
        'DEVICE_IP': device_ip,
        'DEVICE_KEY': device_key,
        'DEVICE_VERSION': device_version,
    }
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)
    click.echo('Configuration saved successfully!')

cli.add_command(configure)
cli.add_command(status)
cli.add_command(on)
cli.add_command(off)

if __name__ == '__main__':
    config.read(config_file_path)
    try:
        cli()
    except ConfigError:
        click.echo('Configuration file is missing or malformed. Please reconfigure the app.')
        configure()
        click.echo('Please rerun the original command.')