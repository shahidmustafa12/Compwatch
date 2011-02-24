from setuptools import setup, find_packages
 
setup(
    name='django-Compwatch',
    version='0.0.1',
    description='A basic compwatch application use to add and view company.',
    author='team@kenthill.in',
    author_email='team@kenthill.in',
    url='http://www.kenthill.in/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
