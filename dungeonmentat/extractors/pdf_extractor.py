from pathlib import Path
import pymupdf


def load_pdf(path: str|Path):
    doc = pymupdf.open(path)
    toc = ""
    pass
