from distutils.core import setup
from setuptools import find_packages
 
setup(name = 'TitleBar',     # 包名
      version = '2021.08.26.1',  # 版本号
      description = '',
      long_description = '配合pyqt可以生成一个标题栏\n仅支持3.7以上', 
      author = 'maplelost',
      author_email = '',
      url = '',
      license = '',
      install_requires = [],
      classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities'
      ],
      keywords = '',
      packages = find_packages('src'),  # 必填，就是包的代码主目录
      package_dir = {'':'src'},         # 必填
      include_package_data = True,
)
#!/usr/bin/env python
