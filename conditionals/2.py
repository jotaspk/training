entrada = input("Que horas são no formato HH:MM?")

try:
  horas, minutos = map(int, entrada.split(":"))


  if 0 <= horas <= 23 and 0 <= minutos <= 59:
      horario = horas + minutos / 60

      if 12 > horario >= 5:
        print("Bom dia!")
      elif 18 > horario >= 12:
        print("Boa tarde!")
      elif 18 <= horario <= 23 + 59/60:
        print("Boa noite!")
      elif 0 <= horario < 5:
       print("Boa madruga!")
  else:
    print("Horário inválido! Use valores entre 00:00 e 23:59.")

except ValueError:
    print("Formato inválido! Digite no formato HH:MM (ex: 14:30).")