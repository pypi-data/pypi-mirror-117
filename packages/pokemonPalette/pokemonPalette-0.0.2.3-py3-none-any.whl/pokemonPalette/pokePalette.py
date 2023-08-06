#!/usr/bin/python3
import cv2
import numpy as np
import urllib.request
import pokebase as pb
from matplotlib import colors
from sklearn.cluster import KMeans

def get_pokemon(Pokemon):
    '''Returns pokedex ID'''
    if isinstance(Pokemon, int) is True:
        return Pokemon
    elif isinstance(Pokemon, str) is True:
        return pb.pokemon(Pokemon.lower()).id
    else:
        raise TypeError("Must be Pokedex ID or Pokemon name")

def get_pokemon_image(pokemon_id, shiny):
   #''Returns a numpy array with the pokemon '''
    url = pb.SpriteResource('pokemon', pokemon_id).url
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)

    return img

def get_color(image, numcolors):
    #'''Will clusterize the n_colors from pokemon'''
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = img.reshape((img.shape[0] * img.shape[1],3))

    clt = KMeans(n_clusters=numcolors+1) #+ 1 because one color is black
    clt.fit(img)

    #convert the array to rgb
    colors = [ i.astype("uint8").tolist() for i in clt.cluster_centers_ ]

    try:
        colors.remove([0,0,0]) #it'll remove the black
    except: 
        pass
    
    colors = [tuple(i) for i in colors]
    
    return colors

def rgb2hex(colors):
    '''return a list of hex colors'''
    return ["#"+'%02x%02X%02X'%color for color in colors]

def get_pokemon_palette(Pokemon, numcolors=4, shiny=False):
    poke_id = get_pokemon(Pokemon)
    colors = get_color(get_pokemon_image(poke_id, shiny), numcolors)
    return rgb2hex(colors)
