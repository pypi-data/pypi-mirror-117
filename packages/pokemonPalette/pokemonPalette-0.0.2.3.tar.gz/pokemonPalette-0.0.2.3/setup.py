import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pokemonPalette",
	version="0.0.2.3",
	author="Rodrigo M Calegari",
	author_email="rodrigomcalegari@gmail.com",
	description="The pokemonPalette is a python library generate a color palette based on the colors of a chosen pokemon.",
	packages=['pokemonPalette'],
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/MilanCalegari/pokemonPalette",
	classifiers=[
		"Programming Language :: Python :: 3"
	],
	license="MIT",
	install_requeres=[
		"opencv-python",
		"pokebase",
		"sklearn",
		"matplotlib",
		"numpy"]
)
