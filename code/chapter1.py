import nsfg

df = nsfg.ReadFemPreg()
# print(df.outcome.value_counts().sort_index())


case_id = 10229
preg_map = nsfg.MakePregMap(df)
indices = preg_map[case_id]
for index, caseid in df.caseid.iteritems():
    print(index,caseid)