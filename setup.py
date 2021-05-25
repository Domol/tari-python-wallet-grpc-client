import re

from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError

from setuptools import setup


class sdist(sdist_orig):
    def __init__(self):
        try:
            self.info("Generating proto files...")
            self.spawn(
                [
                    "python -m grpc_tools.protoc --proto_path=protos --python_out=$(pwd) --grpc_python_out=$(pwd) protos/*.proto"
                ]
            )
            script_names = [
                "tari_python/types_pb2.py",
                "tari_python/types_pb2_grpc.py",
                "tari_python/wallet_pb2.py",
                "tari_python/wallet_pb2_grpc.py",
            ]
            # Make pb2 imports in generated scripts relative
            for script in script_names:
                with open(script, "r+") as file:
                    code = file.read()
                    file.seek(0)
                    file.write(
                        re.sub(r"(import .+_pb2.*)", "from . \\1", code)
                    )
                    file.truncate()
            # self.spawn(["sed -i -r 's/^import (.+_pb2.*)/from . import \1/g' tari_python/*_pb2*.py"])
        except DistutilsExecError:
            self.warn("Generation of proto files failed.")


setup(
    name="tari-python",
    version="0.1.0",
    description="Tari gRPC Python Client",
    url="https://github.com/domol/tari-python-wallet-grpc-client",
    author="Dominik Olczyk",
    author_email="dominik.olczyk@gmail.com",
    license="BSD 2-clause",
    packages=["tari_python"],
    cmdclass={"sdist": sdist},
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
