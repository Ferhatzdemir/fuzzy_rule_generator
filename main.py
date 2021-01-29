import itertools

c = itertools.combinations(
    [b['A'], b['L'], b['P'], b['K'], e['CA'], e['A'], e['F'], e['CF'], m['CK'], m['K'], m['I'], m['CI'], s['CD'],
     s['D'], s['Y'], s['CY'], t['CK'], t['K'], t['U'], t['CU']], 4)
for i in list(c):
    print("rule = ctrl.Rule(" + str(i) + ")")
"""
Bulanık Mantıkta Sckit-fuzzy de otomatik kural oluşturma itertools kütüphanesin combinations fonksiyonu ile oluştdurduk 
eger hata alırsanız yukarıdaki degiştirmelisiniz ben burada 4 ana bulanık küme ve 4 üyelik derecesi üzerinde çalıştım 256 kurala ihtiyacım
vardı ben 4000 kural yazdım print fonksiyonundan sonrasında filtreleme yapılarak daha net alınabilir ben burada ayıklama işlemini 
excel tablosu yaparak ayıkladım.



"""