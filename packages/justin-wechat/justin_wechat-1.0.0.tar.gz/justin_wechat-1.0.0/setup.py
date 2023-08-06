from setuptools import find_packages, setup

setup(
    name='justin_wechat',
    version='1.0.0',
    author='Justin Yoo',
    packages=find_packages(),
    include_package_data=True,
    author_email = 'xg.y@outlook.com',
    zip_safe=False,
    install_requires=[
        'json',
        'requests'
    ],
)