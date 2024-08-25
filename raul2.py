arquivo = 'obrigado.txt'

#Conversão de linha de texto para lista de elementos.
def linhaParaLista(linha):
    return [x.strip() for x in linha.strip().split(',')]

#Definir interseção
def intersecao(lt1, lt2):
    resultado = []
    for item in lt1:
        #Adicionar o item no resultado se não estiver em lt2 e se não estiver no próprio resultado
        if item in lt2 and item not in resultado:
            resultado.append(item)
    return f'Interseção: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

#Definir diferença
def diferenca(lt1, lt2):
    resultado = []
    for item in lt1:
        #Adicionar o item no resultado se não estiver em lt2 e se não estiver no próprio resultado
        if item not in lt2 and item not in resultado:
            resultado.append(item)
    return f'Diferença: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

#Definir união
def uniao(lt1, lt2):
    resultado = []
    for item in lt1:
        #Adicionar o item no resultado se não estiver nele
        if item not in resultado:
            resultado.append(item)
    for item in lt2:
        #Adicionar o item no resultado se não estiver nele
        if item not in resultado:
            resultado.append(item)
    return f'União: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

#Definir Produto cartesiano
def pc(lt1, lt2):
    resultado = []
    repetidos = set()  #Evitar repetições
    for x in lt1:
        for y in lt2:
            if (x, y) not in repetidos:
                resultado.append(f'({x}, {y})')
                repetidos.add((x, y))
    return f'Produto Cartesiano: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

def usarA(arq):

    try:
        with open(arq, 'r') as arq:
            lin = arq.readlines()
            lista = []
            qtd_operacoes = int(lin[0].strip())  #Ler a quantdade de operações
            i = 1  #Primeira linha para ler operações

            for _ in range(qtd_operacoes):
                operacao = lin[i].strip()  #Tipo de operação
                c1 = linhaParaLista(lin[i + 1])  #Conjunto 1
                c2 = linhaParaLista(lin[i + 2])  #Conjunto 2

                #Executar a operação e adicionar o resultado na lista
                if operacao == 'U':
                    lista.append(uniao(c1, c2))
                elif operacao == 'I':
                    lista.append(intersecao(c1, c2))
                elif operacao == 'D':
                    lista.append(diferenca(c1, c2))
                elif operacao == 'C':
                    lista.append(pc(c1, c2))

                i += 3  #Vai para a próxima operação

            #Imprimir os resultados das operações
            for resposta in lista:
                print(resposta)
    except FileNotFoundError:
        print(f'O arquivo {arq} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

#Chamar a função principal
def main():
    usarA(arquivo)

if __name__ == '__main__':
    main()
