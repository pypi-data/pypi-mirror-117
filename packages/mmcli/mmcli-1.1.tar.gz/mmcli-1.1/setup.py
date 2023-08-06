from setuptools import setup

setup(
    name='mmcli',
    version='1.1',    
    description='Cli client for mmdok',
    url='https://github.com/emagnca/mmcli',
    author='Magnus Carlhammar',
    author_email='mcarlhammar@gmail.com',
    license='BSD 2-clause',
    packages=['mmcli'],
    install_requires=['cmd2==1.5.0'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',       
        'Programming Language :: Python :: 3 :: Only'
    ],
)
