def subset_df(df1, df2):
    # Set index
    df1 = df1.set_index("ID")
    df2 = df2.set_index("ID")
    # Find common IDs
    intersection = df1.join(df2, how="inner", rsuffix="1")
    intersection = intersection.reset_index()
    IDs = intersection["ID"].to_list()
    # Subset both dfs to only include common IDs
    df1 = df1.reset_index()
    df1 = df1[df1['ID'].isin(IDs)]
    df2 = df2.reset_index()
    df2 = df2[df2['ID'].isin(IDs)]
    # Sort
    df1 = df1.sort_values(by="ID")
    df2 = df2.sort_values(by="ID")
    return (df1, df2)
