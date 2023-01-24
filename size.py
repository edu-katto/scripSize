# -*- coding: utf-8 -*-
from utils.email.mailConfig import sendMail
from utils.telegram.telegramConfig import sendTelegram
from decouple import config
import psutil, sys

parametro = sys.argv[1]
'''
* Paramentros
i) Envia informacion general del servidor
p) Envia informacion simpre y cuando el servidor se cuentre en riesgo por espacio
'''

ALERTA_LEVE = "🟩"
ALERTA_MODERADA = "🟨"
ALERTA_ELEVADA = "🟥"
alerta = ""

disk_usage = psutil.disk_usage("/")

def to_gb(bytes):
    #Convierte bytes a gigabytes.
    return bytes / 1024**3


espacioTotal = int(float(format(to_gb(disk_usage.total))))
espacioLibre = int(float(format(to_gb(disk_usage.free))))
espacioUsado = int(float(format(to_gb(disk_usage.used))))
porcentajeUso = format(disk_usage.percent)

if porcentajeUso < "85":
    alerta = ALERTA_LEVE

if porcentajeUso >= "85" and porcentajeUso <= "94":
    alerta = ALERTA_MODERADA

if porcentajeUso >= "95":
    alerta = ALERTA_ELEVADA


if parametro == 'i':
    sendMail("Almacenamiento " + config('SERVER_NAME') + " (Información)",
        "Servidor " + config('SERVER_NAME') + " (Información)\n" +
        "Espacio Total: " + str(espacioTotal) + " GB. \n" +
        "Espacio Utilizado: " + str(espacioUsado) + " GB. \n" +
        "Espacio Libre: " + str(espacioLibre)  + " GB. \n" +
        "Porcentaje Utilizado: " + str(porcentajeUso)  + " %. \n" +
        "Nivel de alerta: " + alerta
    )

if parametro == 'p' and alerta == ALERTA_ELEVADA:
    sendMail("Almacenamiento " + config('SERVER_NAME') + " (Peligro)\n",
        "Servidor " + config('SERVER_NAME') + " (Peligro)\n" +
        "Espacio Total: " + str(espacioTotal) + " GB. \n" +
        "Espacio Utilizado: " + str(espacioUsado) + " GB. \n" +
        "Espacio Libre: " + str(espacioLibre)  + " GB. \n" +
        "Porcentaje Utilizado: " + str(porcentajeUso)  + " %. \n" +
        "Nivel de alerta: " + alerta
    )
