import subprocess


class PontoDeAcesso:
    def __init__(self, ssid, senha) -> None:
        self.ssid = ssid
        self.senha = senha
    
    def criar(self):
        try:
            print(f'Configurando o ponto de acesso "{self.ssid}"...')
            # Configura o ponto de acesso com o SSID e a senha fornecida
            subprocess.run(f'netsh wlan set hostednetwork mode=allow ssid={self.ssid} key={self.senha}',
                           check=True, shell=True)
            # Inicia o ponto de acesso
            subprocess.run('netsh wlan start hostednetwork', check=True, shell=True)
            print(f'Ponto de acesso "{self.ssid}" ativado com sucesso.\n')

        except subprocess.CalledProcessError as e:
            print(f'Erro ao criar o ponto de acesso "{self.ssid}": {e}')