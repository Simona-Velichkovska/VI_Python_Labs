def suma_kolokviumi(rezultati):
    # your code here
    for r in rezultati:
        r['Vkupno od kolokviumi'] = r['Kolokvium1'] + r['Kolokvium2']
        del r['Kolokvium1']
        del r['Kolokvium2']

    return rezultati


if __name__ == "__main__":
    n = int(input())
    rezultati = []  # ova e listata od rechnici
    for i in range(0, n):
        r = {}  # rechnik koj kje chuva podatoci za eden student
        brojIndeks = int(input())
        brojPoeni1 = int(input())
        brojPoeni2 = int(input())
        # ovde dodadete gi podatocite vo rechnikot. Potoa dodadete go rechnikot vo listata rezultati!!

        r = {"indeks": brojIndeks, "Predmet": "Veshtachka inteligencija",
             "Kolokvium1": brojPoeni1, "Kolokvium2": brojPoeni2}
        rezultati.append(r)

    print(suma_kolokviumi(rezultati))