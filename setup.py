import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image-processing-package",
    version="1.0.0",
    author="silviodarko",
    description="Um pacote para processamento de imagens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silviodarko/image-processing-package",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "matplotlib",
        "scipy",
        # Adicione outras dependências necessárias aqui
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    setup_requires=["wheel"],
)
