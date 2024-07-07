units=['KB','MB','GB','TB','PB']
def sizeinbyte(size):
    if size < 0:
        raise ValueError('number < 0' )
    factor=1024
    for i in range(len(units)):
        if size < factor:
            
            if i == 0:
                 return '{0:.1f} {1[0]}'.format(size,units)
            elif i == 1:
                 return '{0:.1f} {1[1]}'.format(size,units)
            elif i == 2:
                 return '{0:.1f} {1[2]}'.format(size,units)
            elif i == 3:
                 return '{0:.1f} {1[3]}'.format(size,units)
            else:
                 return '{0:.1f} {1[4]}'.format(size,units)
        else:
             size /=factor


    
    
    raise ValueError('too big')

print(sizeinbyte(2561000))
