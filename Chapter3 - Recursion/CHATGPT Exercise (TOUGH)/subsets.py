def gets(s):
    if not s:
        return [""]
    rest=gets(s[1:])
    return rest+[s[0]+sub for sub in rest] # refet to [DRYRUN.jpg] for full explanation
print(gets("abc"))
