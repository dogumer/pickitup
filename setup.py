from setuptools import setup

setup(name='pickitup',
      version='1.0',
      description='Organize files with one simple command',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      keywords='organize linux windows folder extension modification file size manager',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.8',
          'Topic :: Desktop Environment :: File Managers',
          'Topic :: Utilities',
          ],
      url='http://github.com/dogonso/pickitup',
      author='Dogukan Meral',
      author_email='dogukan.meral@yahoo.com',
      license='MIT',
      include_package_data=True,
      packages=['pickitup'],
      entry_points = {
          'console_scripts': ['pickitup=pickitup.command_line:main'],
          },
      zip_safe=False)
