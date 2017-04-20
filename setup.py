from setuptools import setup


def get_description():
    with open("README.rst") as file:
        return file.read()


setup(
    name="Mongo-Thingy",
    version="0.1.0",
    url="https://github.com/numberly/mongo_thingy",
    license="MIT",
    author="Guillaume Gelin",
    author_email="ramnes@1000mercis.com",
    description="The most Pythonic and friendly-yet-powerful way to use MongoDB",
    long_description=get_description(),
    py_modules=["mongo_thingy"],
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=["thingy>=0.3.0",
                      "pymongo>=3.0"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
