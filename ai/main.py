from ai.downloader.download_manager import DownloadManager
from ai.downloader.downloader import HistoricalDownloader
from ai.downloader.validator import Validator
from ai.downloader.writer import Writer

from auth.kite_session import get_kite
from ai.downloader.instrument_services import InstrumentService


def main():

    kite = get_kite()

    downloader = HistoricalDownloader(kite)
    validator = Validator()
    writer = Writer()
    instrument = InstrumentService(kite)

    manager = DownloadManager(
        downloader,
        validator,
        writer,
        instrument,
    )

    manager.run()


if __name__ == "__main__":
    main()