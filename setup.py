# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import versioneer

from setuptools import setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
