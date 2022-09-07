f = open('archivo.txt', 'w')
f.write('Primera entrada al archivo\n')
f.close()

f = open('archivo.txt', 'a')
f.write('Segunda entrada al archivo\n')
f.close()