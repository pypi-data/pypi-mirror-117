from pathlib import Path
from setuptools.command.install import install
from setuptools import setup


class ReservationCommand(install):
    def run(self, *args, **kwargs):
        raise Exception("This package cannot yet be installed with pip.")


setup(
    name="morphodict",
    version="0.dev1",
    description="Intelligent dictionary application",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/UAlbertaALTLab/cree-intelligent-dictionary",
    author="Alberta Language Technology Lab",
    author_email="altlab@ualberta.ca",
    license="Apache-2.0",
    cmdclass={"install": ReservationCommand},
)
