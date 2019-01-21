import asyncio

from translator import loop, run


class TestMain:
    words = ['love', 'I love you' ,'asasdfsda']
    def test_run(self):
        for words in self.words:
            future = asyncio.ensure_future(run(words, False))
            loop.run_until_complete(future)

        for words in self.words:
            future = asyncio.ensure_future(run(words, True))
            loop.run_until_complete(future)