import os

pedidos = []
total = 0
troco = 0


def finalizador():
    opcoes = int(input('1 - Pagar \n2 - adicionar pedido \n3 - deletar item\n'))
    if opcoes == 1:
        print(f'O pedido deu {total}.')


while True:
    numeroPedidos = int(input('Quantos itens serão adicionados? '))
    for i in range(numeroPedidos):
        pedido = {}
        pedido['pedido'] = str(input(f'Digite o {i + 1}º pedido: ')).lower()
        pedido['valor'] = float(input('Digite o valor do item acima: '))
        pedidos.append(pedido.copy())
        total += pedido['valor']

    print('Resumo do pedido:')
    for i, item in enumerate(pedidos, start=1):
        print(f'{i}: {item["pedido"]} - R${item["valor"]}')
        os.system("clear" if os.name == "posix" else "cls")

    opcoes = int(input('1 - Pagar \n2 - adicionar pedido \n3 - deletar item\n'))
    if opcoes == 1:
        print(f'O pedido deu: {total}.')
        break

    elif opcoes == 2:
        pedido = {}
        pedido['pedido'] = str(input(f'Digite o {len(pedidos) + 1}º pedido a ser adicionado: ')).lower()
        pedido['valor'] = float(input('Digite o valor do item acima: '))
        pedidos.append(pedido.copy())
        total += pedido['valor']
        os.system("clear" if os.name == "posix" else "cls")

    elif opcoes == 3:
        excluir_pedido = input('Qual item deseja deletar? ').lower()
        for item in pedidos:
            if item['pedido'] == excluir_pedido:
                total -= item['valor']
                pedidos.remove(item)
                print(f'O produto {excluir_pedido} foi removido.')
                break
        else:
            print('Produto não encontrado.')
