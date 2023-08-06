import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='CHRequester',
    version='0.0.1',
    author='Maxime Peim',
    author_email='maxime.peim@gmail.com',
    description='Cryptohack URL/NetCat request maker.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/maxime-peim/cryptohack-requester',
    project_urls={
        'Bug Tracker': 'https://github.com/maxime-peim/cryptohack-requester/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
       'requests >= 2.26',
       'pwntools >= 4.6.0'
   ],
)