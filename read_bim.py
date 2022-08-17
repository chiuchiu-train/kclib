def read_bim(infile):
    bim = open(infile, "r")
    snp_dict = dict()
    for line in bim:
        line = line.split()
        rsid = line[1]
        if rsid.startswith("rs") == False:
            continue
        varid = [line[0], line[3], line[5], line[4]]
        varid = ":".join(varid)
        snp_dict[rsid] = varid
    return snp_dict
