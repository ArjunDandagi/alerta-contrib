from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-dynatrace",
    version=version,
    description='Alerta webhook for splunk',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_dynatrace'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'splunk = alerta_dynatrace:DynatraceWebhook'
        ]
    }
)
