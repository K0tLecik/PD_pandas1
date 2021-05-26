from pandas import *
import xlrd
import openpyxl
import matplotlib.pyplot as plt

print("Zadanie 1:")

xlsx = ExcelFile('imiona.xlsx')
a = read_excel(xlsx, header=0)
print(a)

print("Zadanie 2:")

print(a[a['Liczba'] < 1000])

print(a[a['Imie'] == 'MICHAŁ'])

print(a.agg({'Liczba' : ['sum']}))

print(a[(a.Rok >= 2005) & (a.Rok <= 2010)].agg({'Liczba' : ['sum']}))

# print(a.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# b = a.sort_values('Liczba', ascending=False).gruopby(['Rok', 'Plec'])
# for x, y in enumerate(b, start=1):
#     print(f"{x} {y[0]}")
#     print(f" {y[1].ilosc[0]['Imie']}", end='')
#     print(f" {y[1].ilosc[0]['Liczba']}")
#
# print(a[a['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba' : ['sum']}).sort_values(('Liczba','sum'), ascending=False).ilosc[0])
#
# print(a[a['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba' : ['sum']}).sort_values(('Liczba','sum'), ascending=False).ilosc[0])

print("Zadanie 3:")

a = read_csv("zamowienia.csv", header=0, sep=';', decimal='.')
print(a)

print(a['Sprzedawca'].unique())

print(a.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])

print(a.groupby(['Sprzedawca']).size())

print(a.groupby(['Kraj']).agg({'Utarg' : ['sum']}))

print(a[((a['Kraj'] == 'Polska') & (a['Data zamowienia'] >= '2005-01-01') & (a['Data zamowienia'] <= '2005-12-31'))].agg({'Utarg' : ['sum']}))

print(a[((a['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())

r2004 = a[((a['Data zamowienia'].str[:4] == '2004'))]
r2005 = a[((a[ 'Data zamowienia'].str[:4] == '2005'))]
r2004.to_csv("zamowienia_2004.csv", sep=';', index=False)
r2005.to_csv("zamowienia_2005.csv", sep=';', index=False)
