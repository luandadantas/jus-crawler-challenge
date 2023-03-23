# Web Crawler Challenge

### OBJETIVOS

1. Desenvolver um web crawler em Python que extrai das páginas-alvo e salva em disco os dados especificados;
2. Manter em sistema git hospedado de sua preferência (github, gitlab, etc.) o progresso do seu código de acordo com as melhores práticas que regem o uso de tal sistema.
3. Refletir sobre o código conforme ele cresce e propor abstrações. Tais abstrações só devem ser usadas caso ajudem a manter esta pequena aplicação mais coesa (https://en.wikipedia.org/wiki/Cohesion_(computer_science)), concisa (https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) e com baixo nível de acoplamento (https://en.wikipedia.org/wiki/Coupling_(computer_programming)) entre seus componentes internos.

### ESPECIFICAÇÃO

Dadas as opções de máquinas nas páginas-alvo, o crawler deve extrair os seguintes atributos de cada opção de máquina:
- CPU / VCPU
- MEMORY
- STORAGE / SSD DISK
- BANDWIDTH / TRANSFER
- PRICE [ $/mo ]

Páginas-alvo
1. https://www.vultr.com/products/bare-metal/#pricing (apenas Bare Metal)
2. https://www.hostgator.com/vps-hosting (apenas tabela We Recommend)

Ao executar um crawler, devem ser disponíveis as seguintes opções independentes entre si:
- Imprime resultados na tela
- Salva dados em arquivo json
- Salva dados em arquivo csv

Não deve ser usado o framework Scrapy, Selenium ou semelhante alto-nível, mas sinta-se livre para usar alguns conceitos como inspiração, bem como bibliotecas menores utilizadas pelo mesmo (requests, xpath, regex, parsel, etc.)

### ETAPAS
1. Página-alvo 1 - Imprime na tela: A primeira etapa exige que o seu crawler funcione para a página alvo 1, capturando as informações e sendo capaz de imprimi-las na linha de comando em formato arbitrário.
2. Página-alvo 1 - Imprime na tela e salva em json: A segunda etapa exige que o seu crawler funcione para a mesma página-alvo da etapa anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de salvar os dados em um arquivo em formato json
3. Página-alvo 1 - Imprime na tela, salva em json e salva em csv: A terceira etapa exige que o seu crawler funcione para a mesma página-alvo da etapa anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de salvar os dados em um arquivo em formato csv.
4. Páginas-alvo 2 - A quarta etapa exige que você extraia as informações também da página-alvo 2, tendo as mesmas funcionalidades da etapa anterior
