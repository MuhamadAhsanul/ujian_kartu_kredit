# import json
# with open('ccNasabah.json', 'r') as x:
#     out = json.load(x)
# print(out)

[
    {"nama": "Andi", "noCreditCard": 4253625879615781},
    {"nama": "Budi", "noCreditCard": 5123-4567-8912-3455},
    {"nama": "Caca", "noCreditCard": 525362587961578},
    {"nama": "Deni", "noCreditCard": 42536258796157867},
    {"nama": "Euis", "noCreditCard": 4424424424442442},
    {"nama": "Fani", "noCreditCard": 4424424424442444},
    {"nama": "Gaga", "noCreditCard": 5122236879543214},
    {"nama": "Hari", "noCreditCard": 4424444424442444},
    {"nama": "Inne", "noCreditCard": 5122-2368-7954-3213},
    {"nama": "Janu", "noCreditCard": 61234-123-8912-3456},
    {"nama": "Kiki", "noCreditCard": 5199-9967-7912-3457},
    {"nama": "Luis", "noCreditCard": 1111222233334444},
    {"nama": "Mira", "noCreditCard": 5123 - 4567 - 8912 - 3456},
    {"nama": "Nuri", "noCreditCard": 4123356789123456},
    {"nama": "Opik", "noCreditCard": 4123456789123454}
]

class Klasifikasi:
    nama: "nama"
    nomor: "noCreditCard"
    valid: [
        {4253625879615781,
        4424424424442442,
        5122-2368-7954-3213,
        4123456789123454,
        5123-4567-8912-3455,
        4123356789123456}
        ]

class Nasabah():
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor
    def valid(self, nomor):
        if self.nomor == 4253625879615781:
            return True
        elif self.nomor == 4424424424442442:
            return True
        elif self.nomor == 5122-2368-7954-3213:
            return True
        elif self.nomor == 4123456789123454:
            return True
        elif self.nomor == 5123-4567-8912-3455:
            return True
        elif self.nomor == 4123356789123456:
            return True
        else:
            return False
    

Nasabah1 = Nasabah("Andi", "4253625879615781")
Nasabah2 = Nasabah("Budi", "5123-4567-8912-3455")
Nasabah3 = Nasabah("Caca", "0525362587961578")
Nasabah4 = Nasabah("Deni", "42536258796157867")
Nasabah5 = Nasabah("Euis", "4424424424442442")
Nasabah6 = Nasabah
Nasabah7 = Nasabah
Nasabah8 = Nasabah
Nasabah9 = Nasabah
Nasabah10 = Nasabah
Nasabah11 = Nasabah
Nasabah12 = Nasabah
Nasabah13 = Nasabah
Nasabah14 = Nasabah
Nasabah15 = Nasabah