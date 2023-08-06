import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JD_SDK_CUSTOM", # Replace with your own username
    version="0.0.4",
    author="Rponnt",
    author_email="rponnt@gmail.com",
    description="JD SDK version 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires= ['numpy','rsa','psutil','apscheduler','wincertstore'],
    python_requires='>=3',
)