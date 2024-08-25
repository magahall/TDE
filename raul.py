# Raul Magalhães

arquivo = 'obrigado.txt'

def linhaParaLista(linha):
    return [x.strip() for x in linha.strip().split(',')]

def interseccao(lt1, lt2):
    resultado = []
    for item in lt1:
        if item in lt2 and item not in resultado:
            resultado.append(item)
    return f'Interseção: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

def diferenca(lt1, lt2):
    resultado = []
    for item in lt1:
        if item not in lt2 and item not in resultado:
            resultado.append(item)
    return f'Diferença: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

def uniao(lt1, lt2):
    resultado = []
    for item in lt1:
        if item not in resultado:
            resultado.append(item)
    for item in lt2:
        if item not in resultado:
            resultado.append(item)
    return f'União: conjunto 1 {{{", ".join(lt1)}}}, conjunto 2 {{{", ".join(lt2)}}}. Resultado: {{{", ".join(resultado)}}}'

def pc(lt1, lt2):
    resultado = []
    repetidos = set()
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
            qtd_operacoes = int(lin[0].strip())
            i = 1

            for _ in range(qtd_operacoes):
                operacao = lin[i].strip()
                c1 = linhaParaLista(lin[i + 1])
                c2 = linhaParaLista(lin[i + 2])

                if operacao == 'U':
                    lista.append(uniao(c1, c2))
                elif operacao == 'I':
                    lista.append(interseccao(c1, c2))
                elif operacao == 'D':
                    lista.append(diferenca(c1, c2))
                elif operacao == 'C':
                    lista.append(pc(c1, c2))

                i += 3

            for resposta in lista:
                print(resposta)
    except FileNotFoundError:
        print(f'O arquivo {arq} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def main():
    usarA(arquivo)

if __name__ == '__main__':
    main()
