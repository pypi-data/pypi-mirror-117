# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tempfolder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tempfolder',
    'version': '0.4.1',
    'description': "🗂 Easily create temporary folders, add files into them and don't worry about deleting them, tempfolder will take care",
    'long_description': "[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/tempfolder/badge.svg?branch=main)](https://coveralls.io/github/jalvaradosegura/tempfolder?branch=main)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![basic-quality-check](https://github.com/jalvaradosegura/tempfolder/actions/workflows/code_quality.yml/badge.svg)](https://github.com/jalvaradosegura/tempfolder/actions/workflows/code_quality.yml)\n[![GitHub license](https://img.shields.io/github/license/jalvaradosegura/tempfolder)](https://github.com/jalvaradosegura/tempfolder/blob/main/LICENSE)\n\n# tempfolder\n\n🗂 Easily create temporary folders, add files into them and don't worry about deleting them, tempfolder will take care\n\n---\n\nDocumentation: https://jalvaradosegura.github.io/tempfolder/\n\n## Installation\ntempfolder is published on [PyPI](https://pypi.org/project/tempfolder/) and can be installed from there:\n```\npip install tempfolder\n```\n\n## Quick example\nFor a deeper explanation, please check the [docs](https://jalvaradosegura.github.io/tempfolder/)...\n\nRun this and see if you spot the magic, if you don't, please check the [docs](https://jalvaradosegura.github.io/tempfolder/):\n\n``` python\nfrom pathlib import Path\n\nfrom tempfolder import use_temp_folder\n\n\ndef add_config_file_to_folder(folder: str):\n    with open(f'{folder}/config.cfg', 'w') as f:\n        f.write('I_love=tempfolder')\n\n\n@use_temp_folder('some_folder')\ndef test_add_config_file_to_folder():\n    add_config_file_to_folder('some_folder')\n    assert Path('some_folder').exists()\n    assert Path('some_folder/config.cfg').exists()\n\n\ndef test_look_for_the_folder_and_the_file():\n    assert not Path('some_folder').exists()\n    assert not Path('some_folder/config.cfg').exists()\n\n\ntest_add_config_file_to_folder()\ntest_look_for_the_folder_and_the_file()\n```\n",
    'author': 'Jorge Alvarado',
    'author_email': 'alvaradosegurajorge@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jalvaradosegura/tempfolder',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
