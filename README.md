# Repositório HarveAulaDocker

Execute o passo a passo deste repositório e pratique suas habilidades de Python, Git e Docker!

### **Passo 1:** Clone este repositório para seu ambiente local

Escolha um local para onde gostaria copiar este repositório e abra um terminal nessa pasta.  
Em seguida execute o comando abaixo para clonar o repositório:

```git clone https://github.com/Ralubrusto/HarveAulaDocker.git```

Note que agora deve existir uma pasta chamada `HarveAulaDocker` dentro da pasta onde você executou o comando.  
Para prosseguir, abra o Visual Studio Code, selecione a opção "Open Folder" e selecione essa pasta `HarveAulaDocker` recém criada.

### **Passo 2:** Desenvolva o código do jogo da velha convencional

Para aquecer, abra a pasta `python_jogodavelha` e, dentro dela, abra o arquivo `main.py`.  
Nele você já encontrará um esqueleto de como seu código deve funcionar, mas fique à vontade para alterá-lo como quiser.  
Edite e execute esse arquivo quantas vezes julgar necessário até que seu código funcione corretamente, o que implica:

  - Solicitar e armazenar o nome do jogador
  - Solicitar e armazenar uma opção de jogada do jogador
  - Atribuir uma jogada ao computador automaticamente (pode ser aleatória ou sempre igual, você decide)
  - Calcular corretamente o resultado do jogo com base nas jogadas do jogador e do computador

Uma vez que seu código esteja funcionando, passe para o próximo passo.

### **Passo 3:** Faça seu código do jogo da velha rodar dentro de um container Docker!

Inicie essa etapa copiando o arquivo do passo anterior para a pasta `docker_jogodavelha`.  
Dentro dessa pasta há também um arquivo `Dockerfile` a ser preenchido para prepararmos nossa **imagem Docker**!  
Se o seu código já funciona, agora é apenas questão de preencher a Dockerfile com os parâmetros necessários, que são:

  - A primeira linha deve indicar qual imagem python sua imagem irá utilizar. Fique à vontade para acessar o [Dockerhub](https://hub.docker.com/) e consultar as imagens python disponíveis
    - Exemplo: `FROM python:tag` - onde `tag` indicará a versão correspondente do Python (dica, utilize uma tag que termine com `-slim`, pois são imagens mais leves)
  - A segunda linha deve indicar ao Docker que é necessário copiar seu arquivo `main.py` para dentro da imagem. Se você mudou o nome do arquivo, apenas atente-se a isso na hora de preencher o comando
    - Exemplo: `COPY NOME_DO_SEU_ARQUIVO.py .` - não esqueça que há um caracter `.` depois do nome do seu arquivo. 
  - Por fim,  devemos incluir o comando que executa esse arquivo python dentro do container. A sintaxe é a seguinte:
    - `CMD ["python", "NOME_DO_SEU_ARQUIVO.py]`

E pronto! Sua Dockerfile já está preenchida, agora precisamos criar uma imagem a partir dela.   
Para fazer isso, faça o seguinte:

  - Pelo terminal entre dentro da pasta onde está a sua Dockerfile (deve se chamar `docker_jogodavelha`)
    - Caso não esteja dentro dela, utilize o comando `cd NOME_DA_PASTA` no terminal
  - Em seguida execute o comando `docker build . -t NOME_QUE_VC_QUISER`
    - Caso tenha algum erro que indique uma mensagem como `docker daemon is not running`, tente abrir o Docker Desktop e depois executar o comando novamente no terminal

Note que o que você colocar no lugar do `NOME_QUE_VC_QUISER` será o nome da sua imagem.  
Uma vez que o Docker termine de montar a sua imagem, é hora de executá-la!  
Para isso, basta executar o comando abaixo:

  - `docker run -it NOME_QUE_VC_QUISER`
    - Lembre de incluir os parâmetros `-it` para conseguir interagir com o código

Pronto! Seu código python já está funcionando dentro de um container!

### **Passo 4:** Suba uma instância de banco MySQL usando Docker

Esse passo é importante para prepararmos a etapa final, onde nosso código Python irá salvar os resultados dos jogos em uma tabela desse banco MySQL.  
Para subir um banco MySQL usando Docker entre na pasta `docker_mysql` e edite a Dockerfile que está lá.  
Num primeiro momento inclua apenas as seguintes linhas no arquivo:

  - Inclua o comando `FROM mysql`, podendo indicar uma versão específica utilizando tag ou não
  - Inclua o comando `ENV MYSQL_ROOT_PASSWORD=` e depois do sinal de `=` coloque qualquer senha que desejar
    - Exemplo: `ENV MYSQL_ROOT_PASSWORD=password`
    - Essa configuração é necessária para sabermos qual a senha do usuário `root` deste banco

Uma vez preparada a `Dockerfile`, agora é hora de montar a imagem. Lembra do passo a passo?

  - Entre na pasta onde essa Dockerfile está
  - Execute o comando `docker build . -t NOME_PARA_IMAGEM`

Depois de montada a imagem, inicialize o container com o seguinte comando:

  - ```docker run -d -p 3306:3306 NOME_PARA_IMAGEM```
    - O parâmetro `-p 3306:3306` mapeia a porta 3306 do container para a porta de mesmo número do seu computador, permitindo o acesso ao banco pela url `localhost` usando a porta 3306
    - O parâmetro `-d` faz com que a execução do container desacople do seu terminal. Em outras palavras, se você executar sem este parâmetro seu terminal ficará vinculado ao container e não será possível utilizar esse terminal para outros comandos.

Para testar se o banco subiu corretamente é possível acessá-lo via alguma interface de conexão, como o DBeaver, configurando uma conexão para a url `localhost`, porta `3306`, usuário `root` e a senha que você definiu.  
Outra alternativa é acessar o container diretamente pela linha de comando. Para isso executamos:

  - Execute primeiramente o comando `docker ps` para listar os seus containers em execução
  - Localize o container referente ao seu banco mysql procurando pelo nome de imagem que você lhe atribuiu
  - Copie o texto que consta na coluna `NAMES`, este é um nome único que foi atribuído automaticamente ao seu container. Vamos chamar esse parametro de `NOME` para facilitar
  - Execute o comando `docker exec -it NOME bash`
    - Esse comando fará com que acessemos um ambiente dentro do container utilizando linha de comando
  - Uma vez lá dentro execute o comando de login no banco:
    - `mysql -u root -p` - Depois de dar enter a senha será solicitada
    - Pronto! Você está logado dentro do banco! Para testar rode a query `SELECT VERSION();`
    - Para sair do banco digite `exit` e tecle enter. Mesma coisa para sair de dentro do container.


### **Passo 5:** Configure a instância MySQL para inicializar já criando uma tabela

Note que na mesma pasta `docker_mysql` há uma pasta chamada `db` com dois arquivos `.sql`.  
O primeiro arquivo deve criar uma tabela na inicialização do banco.  
Ele já contém um esqueleto dos comandos, apenas preencha o `CREATE TABLE` incluindo 4 colunas

 - Uma coluna `nome` para armazenar o nome do jogador
 - Uma coluna `jogada_jogador` para armazenar a jogada do player
 - Uma coluna `jogada_computador` para armazenar a jogada do computador
 - Uma coluna `resultado` para salvar o resultado da partida

Todas as colunas devem ter tipo `VARCHAR`, mas o comprimento delas fica a seu critério.  
O segundo arquivo cria apenas um usuário a ser utilizado pelo nosso aplicativo python (é sempre uma boa idea não deixar seu app rodando com permissões de administrador).  
Aqui sua missão apenas é escolher um nome e uma senha para seu usuário e ajustar o nome da database e da sua tabela no comando `GRANT` caso tenha mudado os nomes. Esse comando `GRANT` é utilizado para conceder permissões a usuários, como `SELECT`, `INSERT`, `DELETE` entre outros...

Uma vez configurados esses dois arquivos, inclua na sua Dockerfile o comando:
  - `COPY ./db/ /docker-entrypoint-initdb.d/`
    - Esse comando copia todo conteúdo da pasta `db` para uma pasta dentro do container chamada `docker-entrypoint-initdb.d`, que é utilizada por padrão para executar scripts no momento da inicialização do banco

Feito isso, agora é com você!
  - Execute o build novamente dessa imagem
  - Delete o container que ainda está em execução
    - Para isso acesse o Docker Desktop e delete o container manualmente ou execute o comando `docker kill NOME`, lembrando que o `NOME` foi obtido no passo anterior
  - Execute um novo container utilizando essa nova imagem que você criou
  - Acesse novamente o banco usando o terminal e tente rodar um SELECT na tabela que você criou.
    - Para isso execute `USE minhadatabase;` para selecionar a sua database
    - Depois execute `SELECT * FROM NOME_DA_TABELA;`. Se o comando não der erros é sinal que deu tudo certo!

### **Passo 6:** Inclua uma etapa no seu código python para salvar os resultados no banco

Agora que nosso banco está online, é a hora da verdade! Copie o seu script python que já estava funcionando para a derradeira pasta `docker_python_final`.  
Dentro dela há um script python pré-montado chamado `connector.py`. Ali há duas funções, uma para conectar no banco e outra para salvar o resultado.  
O que você precisa fazer aqui é:

  - Configure a função `get_mysql_connector` com os dados do seu usuário (nome e senha) e também altere o nome da database, se for necessário.
  - Instale localmente a biblioteca `mysql-connector-python`, pois ela é necessária para conexão com o banco
  - Insira no final do seu código (no arquivo `main.py`) essas duas linhas abaixo, trocando os nomes para as suas variáveis correspondentes ao nome do jogador, às jogadas do jogador e do computador, e ao resultado:

```
from connector import salva_resultado
conn = salva_resultado(VARIAVEL_NOME_JOGADOR, VARIAVEL_JOGADA_JOGADOR, VARIAVEL_JOGADA_COMPUTADOR, VARIAVEL_RESULTADO)
```

Então execute localmente o código `main.py` para verificar se a integração com o banco está funcionando.  
Se o seu código executar sem erros, parabéns!! Ele está pronto para a fase final


### **Passo FINAL:** Coloque seu código Python em um docker e execute uma vez o jogo da velha 100% em docker!

Como seu código está funcionando, vamos criar uma imagem com ele.  
Você pode aproveitar a sua Dockerfile anterior, mas será necessário incluir alguns comandos a mais:

  - Inclua também um comando `COPY` para copiar o arquivo `connector.py` para dentro da imagem
  - Esse código python utiliza uma biblioteca que precisa ser instalada. Para isso é necessário incluir o comando `RUN`, que executa uma instrução dentro da imagem quando ela está sendo criada:
    - `RUN pip install mysql-connector-python`

Pronto! Para criar a imagem utilize os passos que você já conhece ;)  
Por fim, execute-o! Mas cuidado, pois é necessário incluir um novo parãmetro:

  - Como os containers precisam se conectar entre si, é necessário incluir o parâmetro `--net=host` na execução do container com o código Python, assim ele consegue "enxergar" o outro container.
    - O comando deve ser o seguinte: `docker run -it --net=host NOME_IMAGEM`
