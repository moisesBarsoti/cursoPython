from datetime import timedelta, datetime, date

tipoDeCarro = "G"
dataAtual = datetime.now()
dataAtualFormatada = dataAtual.strftime('"%d/%m/%Y, %H:%M:%S"')
tempoDoPequeno = 30
tempoDoMedio = 45
tempoDoGrande = 60

if tipoDeCarro == 'P':
    dataEstimada = dataAtual + timedelta(minutes=tempoDoPequeno)
    print(f"O carro chegou: {dataAtualFormatada} e ficara pronto às {dataEstimada}")
elif tipoDeCarro == 'M':
    dataEstimada = dataAtual + timedelta(minutes=tempoDoMedio)
    print(f"O carro chegou às: {dataAtualFormatada} e ficara pronto às: {dataEstimada}" )
else:
    dataEstimada = dataAtual + timedelta(minutes=tempoDoGrande)
    print(f"O carro chegou às: {dataAtualFormatada} e ficara pronto às: {dataEstimada}")