from distutils.core import setup
setup(
  name = 'moblabpy',
  packages = ['moblabpy'],
  version = '0.1',
  license='MIT',
  description = 'A module that allow users to stimluate communcation system via their own device',
  author = 'Lewis Chan Chun Ming, Lawrence Tse Pui Yu',
  author_email = 'moblabpy@gmail.com',
  url = 'https://github.com/moblabpy/moblabpy',
  download_url = 'https://github.com/moblabpy/moblabpy/archive/refs/tags/v_01.tar.gz',
  keywords = ['BYOD', 'COMMUNICATION'],
  install_requires=[
          'numpy',
          'segno',
          'pyzbar',
          'PIL',
          'cv2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Topic :: Communications',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
