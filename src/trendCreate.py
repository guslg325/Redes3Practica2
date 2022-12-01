import rrdtool
ret = rrdtool.create("/home/thelv/Documents/Redes 3/Practica3/PythonProject/rrd/trend.rrd",
                     "--start",'N',#N obtiene el tiempo del sistema en epoch
                     "--step",'60',#Enviar muestras cada 60 seg
                     "DS:CPUload:GAUGE:60:0:100",#Datos de 0 a 100
                     "DS:MemUsage:GAUGE:60:0:NaN",
                     "DS:NetUsage:GAUGE:60:0:NaN",
                     "RRA:AVERAGE:0.5:1:24")#- cada 1 step - de 24 filas
if ret:
    print (rrdtool.error())
