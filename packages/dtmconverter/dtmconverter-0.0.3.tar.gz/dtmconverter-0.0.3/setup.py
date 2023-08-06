from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="dtmconverter",
    version="0.0.3",
    author="ThatRobin",
    author_email="ThatRobin3001@gmail.com",
    description="Tools for converting Datapacks to Mods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["context-menu","PyMsgBox"],
    entry_points={
        "console_scripts": [
            "dtm = converter.DatapackToMod:main",
            "dtc = converter.DatapackToCCPacks:main",
            "dto = converter.DatapackToOrigins:main",
            "dtb = converter.DatapackToBoth:main",
            "dtmc_install = converter.ContextMenu:install",
            "dtmc_uninstall = converter.ContextMenu:uninstall"
        ]
    },
)
