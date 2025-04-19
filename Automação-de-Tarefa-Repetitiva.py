# O que esse projeto mostra:
# Manipulação de listas
#
# Automação de rotina
#
# Uso de bibliotecas padrão (webbrowser, time)
#
# Pode ser estendido com botões, interface ou agendamento
import webbrowser
import time

# Lista de sites que você quer abrir
sites_favoritos = [
    "https://mail.google.com",
    "https://www.linkedin.com",
    "https://www.youtube.com",
    "https://chat.openai.com",
]

print("🔁 Iniciando abertura dos seus sites favoritos...")

for site in sites_favoritos:
    print(f"🌐 Abrindo: {site}")
    webbrowser.open(site)
    time.sleep(2)  # Espera 2 segundos entre cada aba pra não travar tudo

print("✅ Todos os sites foram abertos com sucesso!")

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
