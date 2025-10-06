from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="wclub",
    version="1.0.0",
    description="wClub — Multi-tenant fighting club management for Frappe v15+",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Taqrieb Information Technology Company",
    author_email="support@taqrieb.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe>=15,<17"],
)
