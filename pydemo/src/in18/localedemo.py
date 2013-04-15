import time
import locale

tm = time.localtime()

locale.setlocale(locale.LC_ALL, "")
print time.strftime("%x", tm)
print time.strftime("%X", tm)
print locale.currency(100000)

locale.setlocale(locale.LC_ALL, ('de_DE', 'UTF8'))
print time.strftime("%x", tm)
print time.strftime("%X", tm)
print locale.currency(100000)

locale.setlocale(locale.LC_ALL, ("zh_CN","UTF8"))
print time.strftime("%x", tm)
print time.strftime("%X", tm)
print locale.currency(100000)

locale.setlocale(locale.LC_ALL, ("sk_SK","UTF8"))
print time.strftime("%x", tm)
print time.strftime("%X", tm)
print locale.currency(100000)