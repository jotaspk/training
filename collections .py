idade = int(input("Digite sua idade: "))


if 18 <= idade <= 35:
  autorizacao = int(input("Você tem autorização médica? Tecle 1 para Sim ou Tecle 0 para Não: "))
  porte_fisico = int(input("Seu porte físico é bom? Tecle 1 para sim ou Tecle 0 para Não:"))
  if autorizacao == 1 or porte_fisico == 1:
    print("Você pode participar das olimpíadas")
  if autorizacao == 0 and porte_fisico == 0:
    print("Sua entrada foi negada por falta de autorização médica e não ter um porte físico.")
  if (autorizacao != 0 and autorizacao != 1) or (porte_fisico != 0 and porte_fisico != 1):
    print("Valor inválido, digite apenas valores 1 para Sim ou 0 para Não.")
elif 0 <= idade <= 18:
   print("Você é muito novo para participar!")
else:
   print("Você está muito velho para participar!")
