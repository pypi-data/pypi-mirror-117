# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['target_localjson']

package_data = \
{'': ['*']}

install_requires = \
['singer-python>=5.12.1,<6.0.0']

entry_points = \
{'console_scripts': ['target-localjson = target_localjson:main']}

setup_kwargs = {
    'name': 'target-localjson',
    'version': '0.1.1',
    'description': 'A Singer Target for save data to local json files',
    'long_description': '# target-localjson\n\n## Intro\n\nThis Singer Target implements a simple way persist data as local json files.\n\n## Install\n\npip install target-localjson\n\n## Config\n\nTo execute the Tap in Sync Mode you have to provide a config.json file.\n\nThere is only one required key: dest_dir. It must be a string and represents the destination directory where json files will be persisted. \n\nFor each stream received, the Target creates a subdirectory and puts the json files there.\n\n**Requires write permission on dest_dir.**\n\n## Run Target\n\ne.g.\n\n    tap-<your-choice> -c tap_sample_config.json | target-localjson -c sample_config.json',
    'author': 'Wallace Prado',
    'author_email': 'wprado@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
