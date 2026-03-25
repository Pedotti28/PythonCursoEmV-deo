preco = float(input('Qual o preço do produto? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] Em até 2x no cartão.
[ 4 ] Em até 3x ou mais no cartão.''')
opcao = int(input('Qual das opções?'))

if opcao == 1:
    preco =  preco-(10 * preco )/ 100
    print('Você terá 10% de desconto. O valor total será de R${:.2f}'.format(preco))
elif opcao == 2:
    preco = preco - (5 * preco) / 100
    print('Você tera 5% de desconto. O valor total será de R${:.2f}'.format(preco))
elif opcao == 3:
    parcelas = preco / 2
    print('Você não terá nenhum ajuste de preço então ficará no total R${:.2f} com 2 parcelas de R${:.2f}'.format(preco,parcelas))
elif opcao == 4:
    preco = preco + (preco * 20)/100
    nparcela = int(input('Em quantas parcelas serão pagas? '))
    parcela = preco / nparcela
    print('Você terá 20% de juros no valor total. O valor total será de R${:.2f} e com {} parcelas de R${:.2f}'.format(preco,nparcela,parcela))