import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-carousel",
        version="1.0.1",
        description="Shoop Carousel",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_carousel=shoop_carousel"}
    )
