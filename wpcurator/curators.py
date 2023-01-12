import re 
import logging
import pathlib

logger = logging.getLogger(__name__)

def curate_tex_dir(dir: pathlib.Path):
    for texfile in dir.glob("*.tex"): # todo: recursive
        logger.info('found file: %s', texfile)
        curate_tex_file(texfile)


    with open(dir / "ld.yaml", "w") as f:
        f.write("""
mmoda: |
       from wpcurator.normalize import validated_workflowhub_rocrate
        """)


def curate_tex(tex: str):    
    for ipynb_ref in re.findall("{(http.*?ipynb)}", tex):
        logger.info("found ipynb reference: %s", ipynb_ref)


    for ref, l in re.findall(r"(\\href\{.*?astro.unige.ch/(cdci/astrooda|mmoda).*?\}\{.*?\})", tex):
        r = re.match(r"\\href\{(?P<url>.*?)\}\{(?P<label>.*)\}", ref)
        mmoda_ref_url = r.group('url')
        mmoda_ref_label = r.group('label')

        logger.info("found mmoda_ref reference: %s as %s", mmoda_ref_url, mmoda_ref_label)

        patched_ref = re.sub(r"/cdci/astrooda(_|\\_)?", "/mmoda/", mmoda_ref_url)


        # TODO: two variations: call directly or put re-computable reference
        patched_ref = rf'\VAR{{mmoda.validated_workflowhub_rocrate("{patched_ref}", "{mmoda_ref_label}")}}'

        logger.info("patched mmoda_ref reference: %s", patched_ref)

        tex = tex.replace(ref, patched_ref)


    for zenodo_ref in re.findall("(http.*?zenodo.*?)}", tex):
        logger.info("found mmoda_ref reference: %s", zenodo_ref)

    tex = tex.replace(
        r"\begin{document}", """
\\include{ldmacros}
\\usepackage{fontawesome5}

\\usepackage{amssymb}
\\usepackage{tikz}



\\newcommand\\circledmark[1][green!20]{%
  \\tikz\\node[circle,fill=#1,inner sep=0pt]{$\\checkmark$};%
}

\\newcommand\\circledmarki[1][green!20]{%
  \\tikz[baseline=(A.south)]{
    \\node[circle,fill=#1,inner sep=0.75ex] (A) {};
    \\node at (A) {$\\checkmark$};
  }%  
}


\\LOAD{ld.yaml}

\\begin{document}
""")

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
