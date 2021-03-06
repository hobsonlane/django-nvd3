from setuptools import setup, find_packages
import django_nvd3
import os
from pip.req import parse_requirements

def read(*parts):
    return open(os.path.join(os.path.dirname(__file__), *parts)).read()

requirements = list(parse_requirements('requirements.txt'))
install_requires=[req.name for req in requirements if req.req and not req.url]  # `and not line.url` will cause it not to download and install, pehaps doing `lin.req + '>=' + lin.ver` would to the trick
dependency_links=[line.url for line in requirements if line.url]

# print 'locals'
# print locals()
# print 'globals'
# print globals()
# globals and locals -^ above give no clue about verbosity level (-v command-line option for pip) so don't know when to print the debug info below 
print 'install_requires:', install_requires
print 'dependency_links:', dependency_links

setup(
    name='hl-django-nvd3',
    version=django_nvd3.__version__,
    description="Hobson Lane's Django NVD3 -- Django template tags (hooks) for python-nvd3 -- python bindings for nvd3.js which wraps d3.j3 into reusable charts",
    long_description=read('README.rst'),
    keywords='django, nvd3, chart, graph, d3',
    url='http://github.com/hobsonlane/hl-django-nvd3',
    author='Belaid Arezqui, portions by Hobson Lane',
    author_email='hobsonlane@gmail.com',
    license='MIT License',
    zip_safe=False,
    packages=find_packages(exclude=["tests", "demoproject", "docs"]),
    include_package_data=True,
    package_data={},
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
