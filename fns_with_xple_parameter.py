# Define shout with parameters word1 and word2
def shout(word1,word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1=word1+"!!!"
    
    # Concatenate word2 with '!!!': shout2
    
    shout2=word2+"!!!"
    # Concatenate shout1 with shout2: new_shout
    new_shout=shout1+shout2

    
    return new_shout


yell=shout("congratulations","you")


print(yell)
