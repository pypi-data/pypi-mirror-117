from setuptools import setup, find_packages
setup(
    name = 'aigpytest',
    version = "2021.8.26.1",
    license = "Apache2",
    description = "",

    author = 'YaronH',
    author_email = "yaronhuang@foxmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires=["aigpy", "requests"],
    entry_points={'console_scripts': [ 'aigpytest = aigpytest:main', ]}
)
