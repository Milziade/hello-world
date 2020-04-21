import os
import datetime
from prettytable import PrettyTable


# this function will convert bytes to MB.... GB... etc
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


a = 0           # Numero file
b = 0           # Numero cartelle
tot_size = 0    # Peso complessivo

table = PrettyTable(["Cartella", "File", "Peso", "Ultima modifica"])

USB_name = input("Inserire nome USB: ")
walk = input("Percorso directory (inserire percorso completo): ")
f = open('{}.csv'.format(USB_name), "w+", encoding="utf-8")
f.write("Directory,Nome_file,Peso,Ultima_modifica,Size_byte,Last_mod_num")

for dirname, dirnames, filenames in os.walk("{}".format(walk)):
    # print path to all subdirectories first and numbers of directory.
    x = 0
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))
        x += 1
    b += x
    # print path to all filenames, filenames, datetime and size and number of elements.
    k = 0
    for filename in filenames:
        name = os.path.join(dirname, filename)
        t = os.path.getmtime(name)
        last_edit = datetime.datetime.fromtimestamp(t)
        size = os.path.getsize(name)
        size_readble = convert_bytes(size)
        table.add_row([dirname, filename, size_readble, str(last_edit)])
        f.write("\n" + dirname + "," + filename + "," + str(size_readble) + ","
                + str(last_edit) + "," + str(size) + "," + str(t))
        k += 1
        tot_size += size
    a += k

print(table)
print("Cartelle totali: ", b)
print("File totali: ", a)
print("Peso totale: ", convert_bytes(tot_size))
f.close()
