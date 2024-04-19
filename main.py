from pytube import YouTube


def print_available_streams(yt: YouTube):
    """Run this function to see all available streams for the video."""
    for i in yt.streams:
        print(i)


def download_best_stream(yt: YouTube):
    """Download the best available stream."""
    yt.streams.get_highest_resolution().download()


if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=LXb3EKWsInQ&t=171s"
    yt = YouTube(url)
    # video_stream = yt.streams.filter(res='720p', file_extension='mp4').first()
    download_best_stream(yt)

    # if video_stream:
    #     video_stream.download()
    # else:
    #     print('No video stream found')
