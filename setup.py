from setuptools import setup

setup(
    name="tari-python",
    version="0.1.0",
    description="Tari gRPC Python Client",
    url="https://github.com/domol/tari-python-wallet-grpc-client",
    author="Dominik Olczyk",
    author_email="dominik.olczyk@gmail.com",
    license="BSD 2-clause",
    packages=["tari_python"],
    install_requires=["grpcio>=1.37.1", "grpcio-tools>=1.37.1"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
