def get_stats_by_pop(df1, df2, SAS=True):
    groupList = [AFRlist, AMRlist, EURlist, EASlist, SASlist]
    popList = ["AFR","AMR","EUR","EAS","SAS"]
    if SAS == False: # no SAS estimates in one of the dfs
        groupList = [AFRlist, AMRlist, EURlist, EASlist]
        popList = ["AFR","AMR","EUR","EAS"]
    for group in groupList:
        subset1 = df1[df1["ID"].isin(group)]
        subset2 = df2[df2["ID"].isin(group)]
        print("--------------------")
        print("n =", len(subset1))
        for pop in popList:
            subset3 = subset1[pop]
            subset4 = subset2[pop]
            lst1 = subset3.to_list()
            lst2 = subset4.to_list()
            distances = []
            for x,y in zip(lst1,lst2):
                d = abs(x-y)
                distances.append(d)
            mean = statistics.mean(distances)
            stdev = statistics.stdev(distances)
            print(pop, "Average:", mean, "Std Dev:", stdev)
