import operator
from operator import itemgetter


class HardDisk:
   

    def __init__(self, id, marka, price, pcc_id):
        self.id = id
        self.marka = marka
        self.price = price
        self.pcc_id = pcc_id


class PC:
   

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DiskPC:
   

    def __init__(self, pcc_id,disk_id ):
        self.pcc_id = pcc_id
        self.disk_id = disk_id



pcs= [
    PC(1, 'Apple'),
    PC(2, 'Asus'),
    PC(3, 'Lenovo'),

    PC(11, 'Honor'),
    PC(22, 'HP'),
    PC(33, 'Huawei'),
]


disks = [
    HardDisk(1, 'Apple inc', 55000, 1),
    HardDisk(2, 'Atasi', 81000, 2),
    HardDisk(3, 'Cogito Systems', 120000, 3),
    HardDisk(4, 'Fuji', 80000, 3),
    HardDisk(5, 'IBM', 40000, 3),
]

disks_pcs = [
    DiskPC(1, 1),
    DiskPC(2, 2),
    DiskPC(3, 3),
    DiskPC(3, 4),
    DiskPC(3, 5),

    DiskPC(11, 1),
    DiskPC(22, 2),
    DiskPC(33, 3),
    DiskPC(33, 4),
    DiskPC(33, 5),
]


def main():
   

    # Соединение данных один-ко-многим
    one_to_many = [(e.marka, e.price, d.name)
                   for d in pcs
                   for e in disks
                   if e.pcc_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.pcc_id, ed.disk_id)
                         for d in pcs
                         for ed in disks_pcs
                         if d.id == ed.pcc_id]

    many_to_many = [(e.marka, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in disks if e.id == emp_id]

    print('Задание А1')
    for d in pcs:
        if (d.name[0]!='А'):
            print(d.name, ':')
            for i in disks:
                if i.pcc_id==d.id:
                    print(i.marka)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in pcs:
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_emps) > 0:
            d_sals = [sal for _, sal, _ in d_emps]
           
            d_sals_max = max(d_sals)
            res_12_unsorted.append((d.name, d_sals_max))
    
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)



    print('\nЗадание А3')
    res_11 = sorted(many_to_many, key=itemgetter(1))
    print(res_11)



if __name__ == '__main__':
    main()
