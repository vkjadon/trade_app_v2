from tasks.kite_client import get_kite

from downloader.download_manager import DownloadManager
from downloader.downloader import HistoricalDownloader
from downloader.instrument_services import InstrumentService
from downloader.validator import Validator
from downloader.writer import Writer

class TaskManager:

    def __init__(self):

        kite = get_kite()
        downloader = HistoricalDownloader(kite)
        validator = Validator()
        writer = Writer()
        instrument = InstrumentService(kite)

        self.download_manager = DownloadManager(downloader=downloader, validator=validator, writer=writer, instrument=instrument,)

    def download(self, symbols, interval, start_date,end_date,
        download_master=False,):

        self.download_manager.run(symbols=symbols, interval=interval,
            start_date=start_date, end_date=end_date,
            download_master=download_master,)