def validated_workflowhub_rocrate(url, label):
    import time

    from rocrate.rocrate import ROCrate
    from rocrate.model.person import Person

    crate = ROCrate()
    wfl = crate.add_workflow(url)
    
    vs_id = "https://orcid.org/0000-0001-6353-0808"    
    vs = crate.add(Person(crate, vs_id, properties={
        "name": "Volodymyr Savchenko",
        "affiliation": "EPFL, UNIGE"
    }))

    wfl["author"] = vs

    # TODO: upload somewhere
    # TODO: upload/publish functionality in rocrate?
    crate.write("exp_crate")

    return (
        f"\\href{{{url}}}{{{label}}}{{\\color{{green}} \\circledmarki}}"        
        "\\textit{\\footnotesize ("
        f"\\href{{https://workflowhub.eu/?myurl}}{{ROCrate}}, "
        f"validated at {time.strftime(r'%Y-%m-%d %H:%M')} "
        ")}"
    )
    