# Shorten names in fam and ped files
def edit_IDs(in_filename):
    # Prepare output file
    out_filename = in_filename[:-4] + "_edited" + in_filename[-4:]
    outfile = open(out_filename, "a")
    # Iterate through input file contents
    infile = open(in_filename, "r")
    for line in infile:
        if "_" not in line:
            outfile.write(line)
        else:
            line = line.split()
            (fid, iid) = (line[0], line[1])
            (fid, iid) = (fid.split("_"), iid.split("_"))
            idx = int(len(fid) / 2) # index to slice at
            (fid, iid) = ("_".join(fid[-idx:]), "_".join(iid[-idx:]))
            if len(fid) > 19:
                (fid, iid) = (fid.split("_"), iid.split("_"))
                (fid, iid) = (fid[-1], iid[-1])
            other_cols = " ".join(line[2:])
            outfile.write(fid + " " + iid + " " + other_cols + "\n")
    outfile.close()
