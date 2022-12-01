import sys
import rrdtool
from  Notify import send_alert_attached
import time

from getSNMP import consultaSNMP
rrdpath = '/home/thelv/Documents/Redes 3/Practica3/PythonProject/rrd/'
imgpath = '/home/thelv/Documents/Redes 3/Practica3/PythonProject/img/'
check1 = 1
check2 = 1
check3 = 1

while 1:
    ultima_lectura = int(rrdtool.last(rrdpath+"trend.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 1800

    ret = rrdtool.graphv( imgpath+"deteccionCPU.png",
                        "--start",str(tiempo_inicial),
                        "--end",str(tiempo_final),
                        "--vertical-label=Cpu load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                        "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",#Abrir la base 'trend.rrd' en rrdpath
                        "VDEF:cargaMAX=cargaCPU,MAXIMUM",#Punto maximo
                        "VDEF:cargaMIN=cargaCPU,MINIMUM",#Punto minimo
                        "VDEF:cargaSTDEV=cargaCPU,STDEV",#Desviacion estandar
                        "VDEF:cargaLAST=cargaCPU,LAST",#Valor de la ultima lectura
                    #   "CDEF:cargaEscalada=cargaCPU,8,*",
                        "CDEF:umbral10=cargaCPU,10,LT,0,cargaCPU,IF",
                        "CDEF:umbral60=cargaCPU,60,LT,0,cargaCPU,IF",
                        "CDEF:umbral90=cargaCPU,90,LT,0,cargaCPU,IF",
                        "AREA:cargaCPU#00FF00:Carga del CPU",
                        "AREA:umbral10#FFF242:Carga CPU mayor que 10",
                        "AREA:umbral60#FF8714:Carga CPU mayor que 60",
                        "AREA:umbral90#FF0000:Carga CPU mayor que 90",
                        "HRULE:10#FF0000:Umbral 10%",#Umbral linea base
                        "HRULE:60#FF0000:Umbral 60%",#Umbral linea media
                        "HRULE:90#FF0000:Umbral 90%",#Umbral linea max
                        "PRINT:cargaLAST:%6.2lf",
                        "GPRINT:cargaMIN:%6.2lf %SMIN",
                        "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                        "GPRINT:cargaLAST:%6.2lf %SLAST" )

    ultimo_valor=float(ret['print[0]'])
    if ultimo_valor>10 and ultimo_valor<60 and check1:
        dev = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.5.0')
        sw = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.1.0')
        tme = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.3.0')
        date = time.localtime(time.time())
        send_alert_attached("Aviso: Primer umbral superado",dev,sw,tme,str(date),"comunidadASR")
        print("Aviso: Primer umbral superado")
        check1 = 0
    elif ultimo_valor>60 and ultimo_valor<90 and check2:
        dev = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.5.0')
        sw = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.1.0')
        tme = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.3.0')
        send_alert_attached("Aviso: Segundo umbral superado",dev,sw,tme,str(date),"comunidadASR")
        print("Aviso: Segundo umbral superado")
        check2 = 0
    elif ultimo_valor>90 and check3:
        dev = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.5.0')
        sw = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.1.0')
        tme = consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.1.3.0')
        send_alert_attached("AVISO: Tercer umbral superado",dev,sw,tme,str(date),"comunidadASR")
        print("AVISO: Tercer umbral superado")
        check3 = 0
    time.sleep(10)