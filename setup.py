import setuptools

setuptools.setup(
    name="chess-game",
    version="1.0.0",
    description="A chess game built with Arcade and playable in the browser",
    author="Mish Wilson",
    packages=setuptools.find_packages(),
    install_requires=[
        "arcade>=3.0.0",
        "numpy>=1.26.4",
    ],
    python_requires=">=3.9",
)
