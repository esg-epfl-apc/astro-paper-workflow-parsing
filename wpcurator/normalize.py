def validated_workflowhub_rocrate(url, label):
    import time

    return (
        f"\\href{{{url}}}{{{label}}}{{\\color{{green}} \\circledmarki}}"        
        "\\textit{\\footnotesize ("
        f"\\href{{https://workflowhub.eu/?myurl}}{{ROCrate}}, "
        f"validated at {time.strftime(r'%Y-%m-%d %H:%M')} "
        ")}"
    )
    