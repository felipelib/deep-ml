import math

PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
	base = []
	dias = list(range(1, 11))

	for i in range(len(consumption_data)):
		flutuacao = 10 * math.sin(2 * PI * (i+1)  / 10)
		base.append(consumption_data[i] - flutuacao)
	
	media_x = sum(dias) / 10
	media_y = sum(base) / 10

	numerador = sum((dias[i] - media_x) * (base[i] - media_y) for i in range(10))
	denominador = sum((dias[i] - media_x) ** 2 for i in range(10))

	inclinacao = numerador / denominador
	intercepto = media_y - inclinacao * media_x
	consumo_base = inclinacao * 15 + intercepto

	flutuacao_15 = 10 * math.sin(2 * math.pi * 15 / 10)
	consumo_previsto = consumo_base + flutuacao_15

	consumo_seguro = round(consumo_previsto) * 1.05
	consumo_seguro = math.ceil(consumo_seguro)

	return consumo_seguro