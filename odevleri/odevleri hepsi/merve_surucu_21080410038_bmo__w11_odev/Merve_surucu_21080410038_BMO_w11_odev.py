
sinav_sonuc = {'isimler':['Ayse K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],'cinsiyet':['K','E','E','E','K','K'],'matematik':[80,60,77,25,36,75],'turkce':[90,50,53,100,98,66]}
print(sinav_sonuc['isimler'])
print(sinav_sonuc['cinsiyet'])
print(sinav_sonuc['matematik'])
print(sinav_sonuc['turkce'])
# Bu iki boþ listeyi kadýn ve erkek türkçe notlarýný ayrý ayrý tutsun diye oluþturdum
kadinlarin_turkce_notlari = []
erkeklerin_turkce_notlari = []
# Erkek ve kadýn sayýlarý için birer sayaç oluþturdum 
count_k = 0
count_e = 0
#kadýn ve erkek notlarý için ayrý bir  sayaç
k_mat = 0
k_turk = 0
e_mat = 0
e_turk = 0
for i in range(len(sinav_sonuc['cinsiyet'])):
    # Eðer kadýn ise sayaç + 1
    if sinav_sonuc['cinsiyet'][i] == 'K':
        count_k +=1
        k_mat = k_mat + sinav_sonuc['matematik'][i]
        k_turk = k_turk + sinav_sonuc['turkce'][i]
        #Burda  kadýnlar için turkce notlarý alýnýyor
        kadinlarin_turkce_notlari.append(sinav_sonuc['turkce'][i])
        # Eðer kadýn degilse erkek sayaci + 1
    else :
        count_e += 1
        e_mat = e_mat + sinav_sonuc['matematik'][i]
        e_turk = e_turk + sinav_sonuc['turkce'][i]
        #Burada erkekler için  turkce notlarý alýnýyor
        erkeklerin_turkce_notlari.append(sinav_sonuc['turkce'][i])
    
print(f"Erkek Matatematik Ortalamasi: {e_mat/count_e}\n\
Kadinlarin Matematik Ortalamasi: {k_mat/count_k}\n\
Turkce Dersinin Ortalamasi : {(k_turk + e_turk)/(count_e + count_k)}")
print("Kadinlarin En Yuksek Turkce Notu : ", max(kadinlarin_turkce_notlari))
print("Erkeklerin En Yuksek Turkce Notu : ", max(erkeklerin_turkce_notlari))