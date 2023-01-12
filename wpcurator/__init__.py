import os
import re
import pathlib
import subprocess
import tempfile
import logging
import requests


from .curators import curate

logger = logging.getLogger(__name__)


def fetch(uri: str): # only arxiv for now
    # r = requests.get(uri, headers={'Accept': 'application/rdf+xml'})
    # logger.info("%s %s", r, r.text)

    r = re.match("https://doi.org/10.48550/arXiv.(?P<arxivid>.*)", uri)
    if r is None:
        raise RuntimeError

    arxivid = r.group('arxivid')
    
    eprint_url = "https://arxiv.org/e-print/" + arxivid

    cached_path = pathlib.Path(os.getenv('HOME')) / ".cache/arxiv" / arxivid


    if cached_path.exists():
        logger.info("already exists: %s", cached_path)
    else:        
        logger.info("does not exist: %s will download", cached_path)
        cached_path.parent.mkdir(parents=True, exist_ok=True)
        with cached_path.open("wb") as f:
            f.write(requests.get(eprint_url).content)

    basedir = pathlib.Path.cwd() / "paper-build"
    basedir.mkdir(parents=True, exist_ok=True)
    # with tempfile.TemporaryDirectory(dir=basedir) as tmpdir:

    tmpdir = basedir / "paper"
    tmpdir.mkdir(parents=True, exist_ok=True)

    if True:
        logger.info("in tempdir %s", tmpdir)
        subprocess.check_call(['tar', 'xvzf', cached_path], cwd=tmpdir)

        curate(pathlib.Path(tmpdir))
    
        