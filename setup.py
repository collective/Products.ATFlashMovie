import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('Products', 'ATFlashMovie', 'version.txt').strip()

setup(name='Products.ATFlashMovie',
      version=version,
      description='A Flash content-type and extra views for Plone.',
      long_description=read('Products', 'ATFlashMovie', 'README.txt') + "\n\n" +
                       read('Products', 'ATFlashMovie', 'CHANGES.txt'),
      classifiers=[
          'Programming Language :: Python',
          'Framework :: Plone',
          'License :: OSI Approved :: GNU General Public License (GPL)',
      ],
      keywords='plone flash',
      author='Jean-Charles Rogez',
      author_email='jeancharles.rogez@free.fr',
      url='http://plone.org/products/atflashmovie',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
