from pathlib import Path


class Writer:

    def __init__(self):

        self.root = (
            Path(__file__).resolve().parents[1]
            / "data"
            / "raw"
        )

    def exists(
        self,
        symbol,
        year,
        month,
    ):

        return self._file_path(
            symbol,
            year,
            month,
        ).exists()

    def save(
        self,
        symbol,
        year,
        month,
        df,
    ):

        file = self._file_path(
            symbol,
            year,
            month,
        )

        file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_csv(
            file,
            index=False,
        )

        print(f"Saved : {file}")

    def _file_path(
        self,
        symbol,
        year,
        month,
    ):

        return (
            self.root
            / symbol
            / str(year)
            / f"{month:02d}.csv"
        )