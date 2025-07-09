'''Exercício 4 – Controle de execução em ordem
Você tem 3 tarefas (t1, t2, t3) com tempos diferentes, mas precisa que terminem e imprimam na ordem certa, mesmo executando assíncronamente.

Desafio: usar await de forma controlada para garantir ordem.

'''

import asyncio

async def tarefa_1():
    await asyncio.sleep(4)
    print('tarefa 1')

async def tarefa_2():
    await asyncio.sleep(2)
    print('tarefa 2')

async def tarefa_3():
    await asyncio.sleep(3)
    print('tarefa 3')

async def main():
    await tarefa_1()
    await tarefa_2()
    await tarefa_3()

asyncio.run(main())