from setuptools import setup, find_packages

version = '5.0.0'

setup(
    name="alerta-splunk",
    version=version,
    description='Alerta webhook for splunk',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_splunk'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'splunk = alerta_splunk:SplunkWebhook'
        ]
    }
)
