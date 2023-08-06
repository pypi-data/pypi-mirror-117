import setuptools

import site
site.ENABLE_USER_SITE = True

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slurmx",
    version="0.0.1",
    author="D. Khuê Lê-Huu",
    author_email="huudienkhue.le@gmail.com",
    description="slurmx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/netw0rkf10w/slurmx.git",
    project_urls={
        "Bug Tracker": "https://github.com/netw0rkf10w/slurmx/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "slurmx"},
    packages=setuptools.find_packages(where="slurmx"),
    python_requires=">=3.6",
)