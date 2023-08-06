# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['techmo_client', 'techmo_client.service', 'techmo_client.utils']

package_data = \
{'': ['*'], 'techmo_client': ['docker/*', 'docker/tls/*', 'docker/wav/*']}

install_requires = \
['PyAudio==0.2.11',
 'gapic-google-cloud-speech-v1==0.15.3',
 'google-api-core==1.27.0',
 'google-auth-httplib2==0.0.3',
 'google-auth==1.21.1',
 'google-cloud-core==1.0.2',
 'google-cloud-speech==1.0.0',
 'googleapis-common-protos==1.6.0',
 'grpc-google-cloud-speech-v1==0.8.1',
 'grpcio-tools==1.38.1',
 'grpcio==1.38.1',
 'httplib2==0.14.0',
 'oauth2client==2.0.0',
 'proto-google-cloud-speech-v1==0.15.3',
 'protobuf==3.12.2',
 'pydub==0.23.1',
 'setuptools==50.3.2']

setup_kwargs = {
    'name': 'techmo-client',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Marek Radecki',
    'author_email': 'marek.radecki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
