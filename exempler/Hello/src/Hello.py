'''
Created on 01/11/2012

@author: Anubis
'''
def BuyBread():
    print("BuyBread...")
    return("bread")
    
def BuyButter():

    print("BuyButter..")
    return("Butter")

def BuyJam():
    print("BuyJam...")
    return("Jam")

def spretbutter():
    print("spretbutter..")
    return("spretbutter")

def spretjam():
    print("spretjam..")
    return("spretjam")
    
def splat():
    print("splat..")
    return("splat")
    

Food = []

Food.append( BuyBread() )
Food.append( BuyButter() )
Food.append( BuyJam() )
Food.append( spretbutter() )
Food.append( spretjam() )
Food.append( splat() )


print(Food)