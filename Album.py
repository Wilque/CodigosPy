def dicioAlbum (artista, titulo, faixas = ''):
    while True:
        album = {'artista' : artista, 'Titulo': titulo}
        if faixas:
            album ['faixas'] =  faixas
        '''else:
            album = {'artista' : artista, 'Titulo': titulo}'''
        return(album)
