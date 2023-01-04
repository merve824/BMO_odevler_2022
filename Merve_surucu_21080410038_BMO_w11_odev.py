
sinav_sonuc = {'isimler':['Ayse K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],'cinsiyet':['K','E','E','E','K','K'],'matematik':[80,60,77,25,36,75],'turkce':[90,50,53,100,98,66]}
print(sinav_sonuc['isimler'])
print(sinav_sonuc['cinsiyet'])
print(sinav_sonuc['matematik'])
print(sinav_sonuc['turkce'])
# Bu iki bo� listeyi kad�n ve erkek t�rk�e notlar�n� ayr� ayr� tutsun diye olu�turdum
kadinlarin_turkce_notlari = []
erkeklerin_turkce_notlari = []
# Erkek ve kad�n say�lar� i�in birer saya� olu�turdum 
count_k = 0
count_e = 0
#kad�n ve erkek notlar� i�in ayr� bir  saya�
k_mat = 0
k_turk = 0
e_mat = 0
e_turk = 0
for i in range(len(sinav_sonuc['cinsiyet'])):
    # E�er kad�n ise saya� + 1
    if sinav_sonuc['cinsiyet'][i] == 'K':
        count_k +=1
        k_mat = k_mat + sinav_sonuc['matematik'][i]
        k_turk = k_turk + sinav_sonuc['turkce'][i]
        #Burda  kad�nlar i�in turkce notlar� al�n�yor
        kadinlarin_turkce_notlari.append(sinav_sonuc['turkce'][i])
        # E�er kad�n degilse erkek sayaci + 1
    else :
        count_e += 1
        e_mat = e_mat + sinav_sonuc['matematik'][i]
        e_turk = e_turk + sinav_sonuc['turkce'][i]
        #Burada erkekler i�in  turkce notlar� al�n�yor
        erkeklerin_turkce_notlari.append(sinav_sonuc['turkce'][i])
    
print(f"Erkek Matatematik Ortalamasi: {e_mat/count_e}\n\
Kadinlarin Matematik Ortalamasi: {k_mat/count_k}\n\
Turkce Dersinin Ortalamasi : {(k_turk + e_turk)/(count_e + count_k)}")
print("Kadinlarin En Yuksek Turkce Notu : ", max(kadinlarin_turkce_notlari))
print("Erkeklerin En Yuksek Turkce Notu : ", max(erkeklerin_turkce_notlari))