import setuptools

from utils import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tawqeetex", # Replace with your own username
    version=VERSION,
    author="Ayoub Sabri",
    author_email="sabriayoub96@gmail.com",
    description="tawqeeTeX package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayoubsabri/tawqeetex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "tawqeetex = tawqeetex.__main__:main",
        ],
        "gui_scripts": [
            "baz = my_package_gui:start_func",
        ]
    }
)
