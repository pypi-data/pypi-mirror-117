import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acdpnet",
    version="0.1.1",
    author="Aiden",
    author_email="acdphc@qq.com",
    description="Intellen Network Core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/intellen/network",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)