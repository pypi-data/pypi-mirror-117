"""Base class of all Spiders.

Typical usage:
    url = 'https://www.bilibili.com/video/BV15L411p7M8'
    spider = Spider.create_spider(url)  # will return a BilibiliSpider object
    asycio.run(spider.run())  # try to fetch resource information and download
"""
from urllib.parse import urlparse
import aiohttp
import asyncio

from video_dl.args import Arguments
from video_dl.toolbox import UserAgent, info


class Spider(object):
    """crawl data from web and download video.

    subclass of Spider should provide two public attributes:
        site: this class will use this field to create a specific Spider for
            target url. for example, BilibiliSpider's site is 'bilibili.com',
            will auto match to a url like 'https://www.bilibili.com/video/*'.
        home_url: target website's home page. this field will be inserted into
            headers of session to avoid some `no referer, no download` policy.

    subclass of Spider should implement some public methods:
        before_download: do something before download, just like: parse html.
        after_download: merge picture and sound to a completed video, delete
            tamporary files, and et al..
    """
    arg = Arguments()

    cookie = arg.cookie
    diretory = arg.directory
    proxy = arg.proxy
    url = arg.url
    lists = arg.lists

    @classmethod
    def create_spider(cls, url: str):
        """create a specific subclass depends on url."""
        netloc = urlparse(url).netloc
        for subclass in cls.__subclasses__():
            if subclass.site in netloc:
                return subclass()
        raise NotImplementedError

    def __init__(self):
        self.session = None
        self.headers = {
            'accept': '*/*',
            'user-agent': UserAgent().random,
            'cookie': self.cookie,
            'referer': self.home_url,
            'origin': self.home_url,
        }

        # list that contains Videos
        self.video_list = []

    async def create_session(self) -> None:
        """create client seesion if not exist."""
        if self.session is None:
            self.session = aiohttp.ClientSession(headers=self.headers)

    async def close_session(self) -> None:
        """close client session if possible."""
        if self.session:
            await self.session.close()

    async def fetch_html(self, url: str) -> str:
        """get url's html source code from internet."""
        async with self.session.get(url=url, proxy=self.proxy) as r:
            return await r.text()

    async def before_download(self) -> None:
        """do something before download"""
        raise NotImplementedError

    async def downloading(self) -> None:
        """download video from web."""
        await asyncio.wait([
            asyncio.create_task(video.download()) for video in self.video_list
        ])

    def after_downloaded(self) -> None:
        """do something after downloaded video."""
        pass

    async def run(self) -> None:
        """start crawl."""
        info('site', self.site)
        await self.create_session()

        await self.before_download()
        await self.downloading()
        self.after_downloaded()

        await self.close_session()


# import subclasses of Spider.
# You should import XxxSpider in sites/__init__.py
# then Spider.__subclasses__() could be workable.
import video_dl.sites  # pylint: disable=import-error
