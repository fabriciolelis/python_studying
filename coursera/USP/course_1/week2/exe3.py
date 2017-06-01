segundosStr = input("Por favor, entre com o número de segundos que deseja converter:")
segundosInt = int(segundosStr)

dias = segundosInt // (3600 * 24)
segundosRestantes = segundosInt % (3600 * 24)
horas = segundosRestantes // 3600
segundosRestHoras = segundosRestantes % 3600
minutos = segundosRestHoras // 60
segundos = segundosRestHoras % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
