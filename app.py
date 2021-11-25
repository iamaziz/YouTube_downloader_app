import streamlit as st
from pytube import YouTube

# By Aziz Alto (https://github.com/iamaziz)
# Thanks to:
#   https://twitter.com/koladev32/status/1460200958353305601
#   https://github.com/pytube/pytube


class YouTubeDownloader:
    @staticmethod
    def run():
        st.header("YouTube Video Downloader")
        url = st.text_input("Enter YouTube URL to download:")
        if url:
            YouTubeDownloader.validate_url(url)
            with st.expander("preview video"):
                st.video(url)
            if st.button("Download"):
                YouTubeDownloader.cleanup()
                file_ = YouTubeDownloader.download_video(url)
                st.video(file_)
                YouTubeDownloader.helper_message()

    @staticmethod
    def download_video(url):
        with st.spinner("Downloading..."):
            local_file = (
                YouTube(url)
                .streams.filter(progressive=True, file_extension="mp4")
                .first()
                .download()
            )
            st.success("Downloaded")
        return local_file

    @staticmethod
    def validate_url(url):
        import validators

        if not validators.url(url):
            st.error("Hi there 👋 URL seems invalid 👽")
            st.stop()

    @classmethod
    def cleanup(cls):
        import pathlib
        import glob

        junks = glob.glob("*.mp4")
        for junk in junks:
            pathlib.Path(junk).unlink()

    @classmethod
    def helper_message(cls):
        st.write(
            "> To save the video to local computer, "
            "click the vertical ... icon (aka hamburger button) in the bottom-right corner (in the video above) and click download."
        )


if __name__ == "__main__":
    YouTubeDownloader.run()
