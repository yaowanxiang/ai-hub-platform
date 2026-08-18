from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh.readlines() if line.strip() and not line.startswith("#")]

setup(
    name="aihub-platform",
    version="0.1.0",
    author="yaowanxiang",
    author_email="yaowanxiang@qut.edu.cn",
    description="让AI能力像水电一样触手可及 - 通用人工智能平台",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaowanxiang/ai-hub-platform",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "aihub=main:main",
            "aihub-gui=desktop_app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.html", "*.css", "*.js", "*.ico", "*.png"],
    },
)