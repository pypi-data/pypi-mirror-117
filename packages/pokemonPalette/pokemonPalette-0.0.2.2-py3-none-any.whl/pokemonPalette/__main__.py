import sys
from .pokePalette import *

def main():
	pokemon = sys.argv[1]
	print(get_pokemon_palette(pokemon))

if __name__ == '__main__':
	main()



