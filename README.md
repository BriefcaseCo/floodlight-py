# Floodlights CLI

Floodlights CLI is a command-line interface tool for controlling floodlight devices using the TinyTuya library. It provides an easy way to turn floodlights on and off, set brightness levels, and query the status of the device.

## Features

- Turn floodlights on and off with simple commands.
- Set brightness levels for the floodlights.
- Query the current status of the floodlights.
- Utilizes a configuration file for device configuration. If the `config.ini` file is missing, the script will prompt you to create one.

## Installation

You can install Floodlights CLI using pip:

```bash
pip install floodlights
```

## Configuration

Set up the required configuration in a \`config.ini\` file:

```ini
[Floodlight]
DEVICE_ID=your_device_id
DEVICE_IP=your_device_ip
DEVICE_KEY=your_device_key
DEVICE_VERSION=your_device_version
```

## Usage

### Turn On Floodlights

```bash
floodlights on --brightness 1000
```

### Turn Off Floodlights

```bash
floodlights off
```

### Get Floodlights Status

```bash
floodlights status
```

## Dependencies

- tinytuya
- click
- logging
- configparser
- json

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue.

## License

Please refer to the LICENSE file for information on the license governing this project.

## Contact

For any questions or support, please contact the maintainer at [dddanmar@gmail.com](mailto:dddanmar@gmail.com), CEO of [OnlyDans](https://onlydans.com.au).
