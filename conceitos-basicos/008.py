exercicio_hr = float(input('Quantas horas você se exercitou esse mês? '))
converte_horas = float(exercicio_hr * 60)
cal_qmd_total = float(converte_horas * 5)

print(f'Sua quantidade de calorias queimadas no mês é: {cal_qmd_total:.2f}')