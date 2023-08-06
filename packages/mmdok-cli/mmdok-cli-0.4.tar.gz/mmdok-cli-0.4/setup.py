from setuptools import setup

setup(
    name='mmdok-cli',
    version='0.4',    
    description='Cli client for mmdok',
    url='https://github.com/emagnca/mmcli',
    author='Magnus Carlhammar',
    author_email='mcarlhammar@gmail.com',
    license='BSD 2-clause',
    packages=['mmcli'],
    install_requires=['cmd2==1.5.0',
                      'requests==2.25.0'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',       
        'Programming Language :: Python :: 3 :: Only'
    ],
)
