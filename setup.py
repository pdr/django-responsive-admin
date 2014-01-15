from setuptools import setup, find_packages

setup(
    name='django-responsive-admin',
    version='0.2.4',
    description='A responsive admin for Django using Kube CSS',
    author='Pierre Drescher',
    author_email='pierre.drescher@gmail.com',
    url='https://github.com/pdr/django-responsive-admin',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
