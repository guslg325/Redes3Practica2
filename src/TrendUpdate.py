import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/thelv/Documents/Redes 3/Practica3/PythonProject/rrd/'
carga_CPU = 0

while 1:
    carga_CPU = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))

    memoria_total = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.4.1.2021.4.5.0'))
    memoria_libre = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.4.1.2021.4.6.0'))

    red_1 = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.2.2.1.10.3'))
    time.sleep(1)
    red_2 = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.2.2.1.10.3'))

    uso_Memoria = (memoria_total - memoria_libre)/1000000
    uso_Red = red_2 - red_1

    valor = "N:" + str(carga_CPU) + ":" + str(uso_Memoria) + ":" + str(uso_Red)
    print (valor)
    rrdtool.update(rrdpath+'trend.rrd', valor)
   # rrdtool.dump(rrdpath+'trend.rrd','trend.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
