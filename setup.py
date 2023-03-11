from google_images_search import GoogleImagesSearch

from setuptools import setup, find_packages

install_requires = [
    'Google-Images-Search',
    'opencv-python',
    'scikit-image',
    'matplotlib',
    'numpy']

setup(name='artbot',
      version='0.0.1',
      description='art bot',
      url='',
      author='Douglas Franz',
      author_email='nah@nah.com',
      install_requires=install_requires,
      zip_safe=False,  # Use of __file__ and __path__ in some code makes it unusable from zip
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ],
      platforms=['any'],
      license='',
)