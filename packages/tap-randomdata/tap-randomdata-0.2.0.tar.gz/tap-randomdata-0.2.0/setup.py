# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_randomdata']

package_data = \
{'': ['*'], 'tap_randomdata': ['schemas/*']}

install_requires = \
['requests>=2.26.0,<3.0.0', 'singer-python>=5.12.1,<6.0.0']

entry_points = \
{'console_scripts': ['tap-randomdata = tap_randomdata:main']}

setup_kwargs = {
    'name': 'tap-randomdata',
    'version': '0.2.0',
    'description': 'Singer Tap to generate random data from https://random-data-api.com/',
    'long_description': '# Singer Demo\n\n## Intro\n\nThis Singer Tap implements a simple way to generate random data, using https://random-data-api.com/ as source.\n\n## Available Streams\n\nThis Tap supports the Streams listed below:\n\n- Company\n- Restaurant\n- Address\n- Vehicle\n- Food\n\nPlease, check https://random-data-api.com/documentation for more information.\n\n## Config\n\nTo execute the Tap in Sync Mode you have to provide a config.json file.\n\nThere is only one required key: record_count. It must be a integer and represents the number of record to be generated.\n\nPlease check [sample_file](tap-randomdata/sample_config.json) for an example.',
    'author': 'Wallace Prado',
    'author_email': 'wprado@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wallace-prado/singer-demo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
