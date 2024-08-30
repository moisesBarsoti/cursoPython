# Datetime - Ele quem controla as datas, horas e segundos
import datetime

data = datetime.date(2024,8,30)
print(data)

# date.today - Ele pega a data de hoje
dataHoje = datetime.date.today()
print(dataHoje)

# datetime.datetime() - Ele utiliza (year,month,day,hour,minute,seconds,microseconds)
dataHora = datetime.datetime(2024,8,30,10,50,43)
print(dataHora)