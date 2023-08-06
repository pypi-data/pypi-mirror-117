import setuptools

with open("README.md") as f:
    long_description = f.read()


setuptools.setup(
    name='bottem',  
    version='1',
    author="Erfan",
    author_email="parsyab1@gmail.com",
    description="A Python and Telegram utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErfanPY/bottem",
    packages=setuptools.find_packages(),
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="telegram chat messenger mtproto api client library python",
    project_urls={
        "Source": "https://github.com/ErfanPY/bottem",
    },
    py_modules=["bottem"],
    package_dir={'':'.'},
    install_requires=['Pyrogram==1.2.9'],
    python_requires="~=3.6",
)