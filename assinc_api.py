import asyncio
import aiohttp

# Função assíncrona que faz uma requisição para a API
async def buscar_usuario(usuario_id):
    url = f'https://jsonplaceholder.typicode.com/users/{usuario_id}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            dados = await response.json()
            print(f"Usuário {usuario_id}: {dados['name']} - {dados['email']}")

# Função principal que chama várias requisições ao mesmo tempo
async def main():
    ids = [1, 2, 3, 4, 5]  # IDs de usuários
    tarefas = [buscar_usuario(i) for i in ids]
    await asyncio.gather(*tarefas)

asyncio.run(main())
