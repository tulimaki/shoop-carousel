import setuptools

try:
    import shuup_setup_utils
except ImportError:
    shuup_setup_utils = None


if __name__ == '__main__':
    setuptools.setup(
        name="shuup-carousel",
        version="1.5.4",
        description="Shuup Carousel",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shuup.addon": "shuup_carousel=shuup_carousel"},
        cmdclass=(shuup_setup_utils.COMMANDS if shuup_setup_utils else {}),
        install_requires=[
            'shuup>=0.4',
        ],
    )
