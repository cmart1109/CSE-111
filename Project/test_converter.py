# test_youtube_converter.py
import pytest
from unittest.mock import patch
from converter import video_downloader, get_video_url

def test_video_downloader():
    assert video_downloader("") == "Something Went Wrong :("
    assert video_downloader("12345") == "Something Went Wrong :("
class MockInput:
    def __init__(self, url):
        self._url = url

    def get(self):
        return self._url

def test_get_video_url():
    mock_input = MockInput("https://www.youtube.com/watch?v=3JBKp0YbSEc")
    assert get_video_url(mock_input) == "https://www.youtube.com/watch?v=3JBKp0YbSEc"
    mock_input = MockInput("https://www.youtube.com/watch?v=UZwi9SHgzGY")
    assert get_video_url(mock_input) == "https://www.youtube.com/watch?v=UZwi9SHgzGY"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
