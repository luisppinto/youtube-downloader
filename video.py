import pytube

''' Inspired by NeuralNine '''
'''WARNING: DOWNLOADING COPYRIGHTED MATERIAL IS HIGHLY ILLEGAL!
I DO NOT TAKE ANY RESPONSIBILITY FROM THE USAGE OF THIS TOOL!
THIS IS FOR EDUCATIONAL PURPOSES ONLY!'''

video_list = []

print("Enter URLs (Terminate by 'STOP')")
while True:
	url = input("")
	if url == 'STOP':
		break
	video_list.append(url)

for x, video in enumerate(video_list):
	v = pytube.YouTube(video)
	stream = v.streams.get_by_itag(133)
	print(f"Downloading video {x}...")
	stream.download()
	print("Done")
