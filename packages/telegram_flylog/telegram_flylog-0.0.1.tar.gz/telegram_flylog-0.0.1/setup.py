#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='telegram_flylog',
    version='0.0.1',
    author='dean',
    author_email='deanzhou56@gmail.com',
    url='https://github.com/deanzhou69/telegram_log',
    description=u'基于flylog的telegram日志发送',
    packages=['telegramlog'],
    # urllib3 应该要依赖
    install_requires=['supervisor', 'flylog'],
)

