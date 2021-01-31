import os
import pathlib

import setuptools

TARGET_NAME = os.environ["TARGET_NAME"]
TARGET_VERSION = os.environ["TARGET_VERSION"]

readme_path = pathlib.Path("README.md")
requirements_path = pathlib.Path("requirements.txt")

setuptools.setup(
    name=TARGET_NAME,
    version=TARGET_VERSION,
    description="Send text messages on TextNow with the Playwright API",
    long_description=readme_path.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/george-lim/textnow-bot-python",
    author="George Lim",
    author_email="lim.george@me.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications :: Chat",
        "Topic :: Communications :: Telephony",
        "Topic :: Education :: Testing",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="python playwright web automation headless textnow bot",
    py_modules=["textnow_bot"],
    install_requires=requirements_path.read_text().splitlines(),
    python_requires=">=3.7",
)
