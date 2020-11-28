import pytube

''' Inspired by NeuralNine '''
'''WARNING: DOWNLOADING COPYRIGHTED MATERIAL IS HIGHLY ILLEGAL!
I DO NOT TAKE ANY RESPONSIBILITY FROM THE USAGE OF THIS TOOL!
THIS IS FOR EDUCATIONAL PURPOSES ONLY!'''

url = input("Paste Playlist URL")

playlist = pytube.Playlist(url)
for url in playlist:
    video = pytube.Youtube(url)
    stream = video.streams.get_by_itag(22)
    print("Downloading playlist...")
    stream.download
    print("Done!")
