precoMerc = float(input('digite o preço da mercadoria: '))
desconto = float(input('digite o percentual do desconto: '))
descontoSomado = desconto * precoMerc

print (f'o valor do desconto é: R$ {descontoSomado:.2f}')
print (f'o preço que você ira pagar é: R$ {precoMerc - descontoSomado:.2f}')