# Bir Packets adinda folder(Paket) yaradin. Icinde samitler adinda bir file (modul) olsun.
# Onunda icinde samitleri_al adinda bir funksiya olsun.

# Nece calisacaq ?:
# Bu folderden colde yerlesen main.py faylimizda bu methodu cagirmali ve icine bir deyer (cumle) gondermeliyik.

# Numune cagrilma:
# 'Salam necesen ... '

# netice:
# {'s', 'l', 'm', 'n', 'c'} >> heresinden bir dene olsa kifayetdir

# def samitleri_al(metin):
#     samitler = set()
#     for harf in metin:
#         if harf.lower() in "samit":
#             samitler.add(harf.lower())
#     return samitler


from Packets.samitler import samitleri_al

if __name__ == "__main__":
    cumle = input("cumleni daxil edin ")
    samitler = samitleri_al(cumle)
    print("Samitler:", samitler)

