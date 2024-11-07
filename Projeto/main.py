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
            
    

def solicitar_dados_ap() -> PontoDeAcesso:
        while True:
            ssid = input("Digite o nome (SSID) do AP: ").strip()
            if not ssid:
                print("O SSID não pode estar vazio. Tente novamente.")
                continue
            
            senha = input("Digite a senha do AP (mínimo 8 caracteres): ").strip()
            if len(senha) < 8:
                print("A senha deve ter pelo menos 8 caracteres. Tente novamente.")
                continue
            
            return PontoDeAcesso(ssid, senha)

def main():
        try:
            quantidade_aps = int(input("Digite a quantidade de pontos de acesso que deseja criar: "))
            if quantidade_aps <= 0:
                print("A quantidade deve ser um número positivo.")
                return

            aps = [solicitar_dados_ap() for _ in range(quantidade_aps)]

            for ap in aps:
                ap.criar()

        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número para a quantidade de APs.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    
if __name__ == "__main__":
        main()