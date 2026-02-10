def albumList(art, alb, tracks = None):
    """Makes a dictionary of albums and artists."""
    albList = {'Album': art, 'Artist': alb};
    if tracks:
        albList[tracks] = tracks;
    return albList;

album1 = albumList('Pink Floyd', 'The Wall', tracks = 26);
album2 = albumList('Megan Thee Stallion', 'Good News');
album3 = albumList('Cardi B', 'Am I The Drama', tracks = 15);

print(album1);
print(album2);
print(album3);

def makeAlbum(artist, album, tracks = None):
    """Makes album"""
    album = {'artist': artist, 'album': album}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease enter the name of an album information: ")
    print("(enter 'q' at any time to quit)")
    
    art = input("Artist Name: ")
    if art == 'q':
        break;
    alb = input("Album Name: ")
    if alb == 'q':
        break;
    trk = input("Number of Tracks: ")
    if trk == 'q':
        break;
    albInfo = makeAlbum(art, alb, trk)
    print(albInfo)