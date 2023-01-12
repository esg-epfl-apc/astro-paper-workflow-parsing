import re 
import logging
import pathlib

logger = logging.getLogger(__name__)

def curate_tex_dir(dir: pathlib.Path):
    for texfile in dir.glob("*.tex"): # todo: recursive
        logger.info('found file: %s', texfile)
        curate_tex_file(texfile)


def curate_tex(tex: str):    
    for ipynb_ref in re.findall("{(http.*?ipynb)}", tex):
        logger.info("found ipynb reference: %s", ipynb_ref)


    for mmoda_ref in re.findall(r"(http.*?astro.unige.ch/cdci/astrooda.*?)\}", tex):
        logger.info("found mmoda_ref reference: %s", mmoda_ref)
        patched_ref = re.sub("/cdci/astrooda_?", "/mmoda/", mmoda_ref)
        logger.info("patched mmoda_ref reference: %s", patched_ref)

        tex = re.sub(mmoda_ref, patched_ref, tex)


    for mmoda_ref in re.findall(r"(http.*?astro.unige.ch/mmoda.*?)\}", tex):
        logger.info("found mmoda_ref reference: %s", mmoda_ref)

    for zenodo_ref in re.findall("(http.*?zenodo.*?)}", tex):
        logger.info("found mmoda_ref reference: %s", zenodo_ref)

    # TODO: for each reference, replace with a workalbe ld-latex call
    return tex
    

def curate_tex_file(texfile: pathlib.Path):
    logger.info('found file: %s', texfile)

    with open(texfile) as f:
        tex = curate_tex(f.read())
    
    with open(texfile, "w") as f:
        f.write(tex)


def curate(dir: pathlib.Path):
    curate_tex_dir(dir)
