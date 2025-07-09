# Exercício 2 – Baixando dados simulados

import asyncio

async def baixando_dados(site):

    print(f'Baixando dados do site {site}')
    await asyncio.sleep(2)
    print(f'Dados do site {site} concluído')

async def main():
    sites = ['site1.com', 'site2.com', 'site3.com', 'site4.com']
    tarefas = [baixando_dados(site) for site in sites]
    await asyncio.gather(*tarefas)

asyncio.run(main())