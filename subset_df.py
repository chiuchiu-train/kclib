def subset_df(df1, df2, col="ID", complement=False):
    # Set index
    df1 = df1.set_index(col)
    df2 = df2.set_index(col)
    # Find common IDs
    intersection = df1.join(df2, how="inner", rsuffix="1")
    intersection = intersection.reset_index()
    IDs = intersection[col].to_list()
    # Subset both dfs to only include common IDs
    df1 = df1.reset_index()
    df2 = df2.reset_index()
    if complement == True:
        df1 = df1[-df1[col].isin(IDs)]
        df2 = df2[-df2[col].isin(IDs)]
    else:
        df1 = df1[df1[col].isin(IDs)]
        df2 = df2[df2[col].isin(IDs)]
    # Sort
    df1 = df1.sort_values(by=col)
    df2 = df2.sort_values(by=col)
    return (df1, df2)
