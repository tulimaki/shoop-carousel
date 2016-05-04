import setuptools

try:
    import shoop_setup_utils
except ImportError:
    shoop_setup_utils = None


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-carousel",
        version="1.0.5",
        description="Shoop Carousel",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_carousel=shoop_carousel"},
        cmdclass=(shoop_setup_utils.COMMANDS if shoop_setup_utils else {}),
        install_requires=[
            'shoop>=3.0,<5',
        ],
    )
