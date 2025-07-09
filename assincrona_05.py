# Exercício 5 – Fila de execução

import asyncio

semaforo = asyncio.Semaphore(2)
async def atendimento(nome):
    print(f'{nome} está esperando para ser atendido(a)')
    async with semaforo:
        print(f'{nome} iniciou o atendimento')
        await asyncio.sleep(2)
        print(f'{nome} terminou o atendimento')

async def main():
    nomes = ['Souza', 'Romarinho', 'Yuri', 'Alberto']
    atendimentos = [atendimento(ordem) for ordem in nomes]
    await asyncio.gather(*atendimentos)

asyncio.run(main())