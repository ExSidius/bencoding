from distutils.core import setup

setup(
    name='bencoding',
    version='0.1',
    packages=[
        'bencoding',
    ],
    license='MIT',
    description='Encode and Decode files using BitTorrent protocol.',
    long_description=open('README.md').read(),
    author='Mukul Ram',
    author_email='mukul.ram97@gmail.com',
    url='https://github.com/ExSidius/bencoding',
    keywords=['bittorrent', 'bencode', 'encode', 'decode'],
)
