# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "0.0.9"
PACKAGE_NAME = "blp.dsbuild.kubernetes"
DEVELOPMENT_STATUS = "4 - Beta"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

#with open('requirements.txt') as f:
#    REQUIRES = f.readlines()
REQUIRES = """
certifi>=14.05.14 # MPL
six>=1.9.0  # MIT
python-dateutil>=2.5.3  # BSD
setuptools>=21.0.0  # PSF/ZPL
urllib3>=1.19.1,!=1.21  # MIT
pyyaml>=3.12  # MIT
google-auth>=1.0.1  # Apache-2.0
ipaddress>=1.0.17  # PSF
websocket-client>=0.32.0,<=0.40.0 # LGPLv2+

"""

#with open('test-requirements.txt') as f:
#    TESTS_REQUIRES = f.readlines()
TESTS_REQUIRES = """
coverage>=4.0.3
nose>=1.3.7
pytest
pluggy>=0.3.1
py>=1.4.31
randomize>=0.13
mock>=2.0.0
sphinx>=1.2.1,!=1.3b1,<1.4 # BSD
recommonmark
codecov>=1.4.0
pep8
autopep8
isort
"""

setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="Kubernetes python client - https://github.com/kubernetes-incubator/client-python/commit/bca588fbb3d40c56726d1ea1388b47b84b997538",
    author_email="",
    author="Kubernetes",
    license="Apache License Version 2.0",
    url="https://github.com/kubernetes-incubator/client-python",
    keywords=["Swagger", "OpenAPI", "Kubernetes"],
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    #packages=find_packages(),
    packages=['blp', 'blp.dsbuild', 'blp.dsbuild.kubernetes', 'blp.dsbuild.kubernetes.client', 'blp.dsbuild.kubernetes.config',
              'blp.dsbuild.kubernetes.watch', 'blp.dsbuild.kubernetes.client.apis',
              'blp.dsbuild.kubernetes.client.models'],
    include_package_data=True,
    #data_files=['requirements.txt', 'test-requirements.txt'],
    long_description="""\
    Python client for kubernetes http://kubernetes.io/
    """,
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)