'''Exercício 1 – Simulando tarefas com tempo
Crie três funções assíncronas que simulem tarefas demoradas com asyncio.sleep():

tarefa_a() → espera 3 segundos

tarefa_b() → espera 2 segundos

tarefa_c() → espera 1 segundo

Execute todas ao mesmo tempo e imprima o tempo total gasto (deve ser no máximo 3 segundos).'''

import asyncio

async def tarefa_a():
    print('Iniciando a tarefa A')
    await asyncio.sleep(3)
    print('Finalizando a tarefa A')

async def tarefa_b():
    print('Iniciando a tarefa B')
    await asyncio.sleep(2)
    print('Finalizando a tarefa B')

async def tarefa_c():
    print('Inicaindo a tarefa C')
    await asyncio.sleep(1)
    print('Finalizando a tarefa C')

async def main():
    await asyncio.gather(tarefa_a(), tarefa_b(), tarefa_c())

asyncio.run(main())

# a b c c b a