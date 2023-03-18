from pytube import YouTube, Playlist
from threading import Thread


def main():
    format = input('1 - file\n2 - playlist\n')

    if format == 1:
        with open('link.txt', 'r') as file:
            links = file.text
            print(links)
    else:
        link_playlist = input('Playlist link: ')
        playlist = Playlist(link_playlist)
        links = playlist.video_urls

    for index, link in enumerate(links):
        index += 1
        print(f'Total video --- {len(links)}\n')
        Thread(target=download_video, args=(link, index, )).start()


def download_video(link, number):
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download('video/')
    print('\t' + str(number) + ' --- finish')


if __name__ == '__main__':
    main()

