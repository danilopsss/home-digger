from pathlib import Path
from homedigger.core.scrapper import Scrapper


if __name__ == "__main__":
    files = Path(__file__).parent.joinpath("html").rglob("*.html")
    for file in files:
        scrapper = Scrapper(file)
        print(scrapper.run().model_dump_json())
