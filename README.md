# Ponto_de_Acesso_Wifi
Projeto Python para configurar pontos de acesso Wi-Fi no Windows.

🚩 Detalhes sobre o código

🔴 Explicação:

subprocess.run() é usado para executar comandos do sistema.
O comando netsh wlan set hostednetwork configura o ponto de acesso com o SSID e a chave especificada.
netsh wlan start hostednetwork inicia o ponto de acesso.

🔴 Notas:

Esse script pode ser executado em Python 3 no Windows.
Para que funcione, o adaptador Wi-Fi do seu computador precisa suportar a criação de pontos de acesso.
O script requer privilégios de administrador para criar pontos de acesso. Portanto, deve ser executado como administrador.

🔴 Verificação:

Para verificar se os APs aparecem na aba Wi-Fi de outro dispositivo, conecte o dispositivo à rede sem fio e veja se os SSIDs configurados são exibidos.

Aviso: Criação de múltiplos pontos de acesso simultâneos pode ser limitada pelo hardware do seu computador e pelo sistema operacional. Normalmente, apenas um ponto de acesso pode estar ativo por vez.

🔴 Características do projeto

🔴 Classe PontoDeAcesso:
Abstrai a lógica de configuração do ponto de acesso, tornando o código mais organizado e orientado a objetos.

🔴 Validações de entrada:
Verifica se o SSID não está vazio e se a senha tem pelo menos 8 caracteres.
Verifica se a quantidade de APs é um número positivo.

🔴 Tratamento de erros aprimorado:
Inclui tratamento de exceções detalhado para capturar erros durante a execução dos comandos do sistema.
Mensagens de erro informativas para o usuário.

🔴 Feedback ao usuário:
Mensagens que informam sobre o progresso e sucesso ou falha da criação dos pontos de acesso.

🔴 Notas importantes:

▶ Privilégios de administrador: Esse script precisa ser executado com privilégios de administrador para funcionar corretamente.
▶ Compatibilidade de hardware: O computador precisa ter um adaptador Wi-Fi que suporte a criação de pontos de acesso.
▶ Limitação de múltiplos APs: O sistema Windows geralmente só permite um ponto de acesso ativo por vez. O script é configurado para solicitar e configurar múltiplos, mas apenas um pode estar ativo simultaneamente, dependendo das capacidades do hardware.

💥 Utilidades do Projeto

1. Compartilhamento de Internet
Utilidade: Transformar um computador em um ponto de acesso para compartilhar a conexão de internet com outros dispositivos. Isso pode ser útil em locais onde apenas um dispositivo pode se conectar à rede principal, mas você deseja que outros dispositivos acessem a internet através desse computador.
Cenário de uso: Em um escritório temporário ou evento onde a conexão à internet é limitada a um dispositivo, mas outros precisam de acesso.

2. Testes e Desenvolvimento de Aplicações de Rede
Utilidade: Desenvolvedores que trabalham em aplicações que requerem redes locais podem usar esse projeto para criar redes de teste de maneira rápida e personalizável.
Cenário de uso: Testar o comportamento de dispositivos IoT, aplicativos móveis ou serviços que dependem de conexão de rede em diferentes SSIDs.

3. Treinamento e Ensino
Utilidade: Usar o projeto para demonstrar conceitos relacionados à criação de redes, segurança de Wi-Fi e gerenciamento de redes em aulas ou treinamentos de TI.
Cenário de uso: Um professor de tecnologia da informação que precisa ensinar a configuração e o funcionamento de pontos de acesso sem fio.

4. Gerenciamento de Redes Temporárias
Utilidade: Criar redes temporárias em eventos, hackathons ou pequenas conferências para que os participantes se conectem rapidamente.
Cenário de uso: Um organizador de eventos que quer oferecer um ponto de acesso específico para cada grupo de participantes.

5. Automação de Tarefas de Rede
Utilidade: Automação de tarefas de rede, como a criação de redes seguras em horários específicos ou para propósitos temporários.
Cenário de uso: Empresas que querem facilitar o acesso à internet para convidados ou clientes sem precisar acessar diretamente o painel de controle do roteador.

6. Redundância e Backup de Conexão
Utilidade: Configurar pontos de acesso como backup, garantindo que, se a rede principal falhar, dispositivos possam se conectar a um AP criado no computador.
Cenário de uso: Manutenção de operações críticas onde uma conexão contínua à internet é necessária.

7. Testes de Segurança
Utilidade: Criar redes falsas para testar como dispositivos se comportam em um ambiente simulado e avaliar medidas de segurança.
Cenário de uso: Profissionais de cibersegurança que precisam entender o comportamento de dispositivos em redes desconhecidas para identificar vulnerabilidades.

Restrições e Considerações:
Limitações do Windows: A capacidade de criar múltiplos pontos de acesso simultâneos é limitada pelo sistema e pelo hardware.
Privilégios de Administrador: O script requer execução com privilégios de administrador.
Segurança: Padrões de segurança devem ser considerados ao criar pontos de acesso para garantir que dados sensíveis não sejam expostos.
Em resumo, este projeto é uma ferramenta útil para quem trabalha com redes e precisa de soluções rápidas para criar e gerenciar pontos de acesso sem fio em diferentes contextos.

Em resumo, este projeto é uma ferramenta útil para quem trabalha com redes e precisa de soluções rápidas para criar e gerenciar pontos de acesso sem fio em diferentes contextos. 
