# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codepipeline_wrapper']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.18,<2.0',
 'compose-x-common[aws]>=0.1.1,<0.2.0',
 'ecs-files-composer>=0.4.4,<0.5.0']

setup_kwargs = {
    'name': 'codepipeline-wrapper',
    'version': '0.1.0',
    'description': 'Lambda Function that replaces AWS ECR images in AWS CodePipeline',
    'long_description': None,
    'author': 'John Preston',
    'author_email': 'john@ews-network.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
