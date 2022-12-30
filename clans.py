mstr = "Batenga, Batanda, Kagere, Kittengo, Kyomubi, Lugyayo, Lulaba, Luwedde, Lwantale, Mazzi, Mpologoma, Muggale, Nabadda, Nabisaalu, Nabiwemba, Nabweteme, Naccwa, Nnaluwembe, Nakabiri, Nakalema, Nakamaanya, Nakampi, Nakayenga, Nakimbugwe, Nakuyita, Nakiggala, Namaalwa, Namikka, Nanjobe, Nassiwa, Nassolo, Ndagire (ab'enjaza balituuma), Ndege, Nkinzi, Tajuuba, Semalabe, Tuttekubano, Nnabaloga, Nattu, Ntaleyeebweera, Nazibanja, Nnamukaabya, Zalwango, Zansanze, Zzawedde."

lines = mstr.split(",")
for line in lines:
    print(f'"{line.strip()}",')