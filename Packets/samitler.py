def samitleri_al(metn):
    saitler = ("aioueöüəı")
    samitler = set()
    for harf in metn:
        if harf.isalpha()and harf not in saitler:
            samitler.add(harf.lower())
    return samitler
