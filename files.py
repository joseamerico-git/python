import os 

sistema_operacional = os.name
username = os.environ.get("USERNAME")

print(f'Usuário atual logando no sistema operacional {username}, o sistema operacional é : {sistema_operacional}')
print(f'Diretório atual: {os.getcwd()}')
print(f'Verificar diretório: {os.chdir("C:\\")}')
