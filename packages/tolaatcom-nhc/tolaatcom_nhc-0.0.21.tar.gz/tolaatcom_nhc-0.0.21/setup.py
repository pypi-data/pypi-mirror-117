from distutils.core import setup


setup(
    name='tolaatcom_nhc',
    version='0.0.21',
    description='tolatcom module for scraping backend of net hamishpat app',
    url='https://github.com/tolaat-com/tolaatcom_nhc',
    download_url='https://github.com/tolaat-com/tolaatcom_nhc/archive/refs/tags/0.0.21.tar.gz',
    author='Andy Worms',
    author_email='andyworms@gmail.com',
    license='mit',
    packages=['tolaatcom_nhc'],
    install_requires=['PyPDF2==1.26.0', 'Pillow==8.3.1'],
    zip_safe=False
)