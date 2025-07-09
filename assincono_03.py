'''Exercício 3 - Corrida de tarefas
Crie uma "corrida" entre 5 tarefas com tempos de espera aleatórios entre 1 e 5 segundos. Exemplo:'''

import asyncio
import random

async def entrega(nome):
    tempo = random.randint(1, 10)
    await asyncio.sleep(tempo)
    print(f'O {nome} terminou a entrega em {tempo} segundos ')

async def main():
    nomes = ['João', 'Maria', 'Pereira', 'Funck']
    entregas = [entrega(nome) for nome in nomes]
    await asyncio.gather(*entregas) # desempacotamento

asyncio.run(main())