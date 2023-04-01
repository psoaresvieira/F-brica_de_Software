# F-brica_de_Software
OBS: se vocês clicarem para entrar no arquivo Desafio da Fábrica Verdadeiro encontrarão o arquivo certo!

1.Criei a pasta de arquivo
2.Entrei na Pasta
3.Criei uma VENV
4.Ativei a VENV
7.Instalei o DjangoRestFramework
8.Criei um projeto
9.Adicionei rest_framework no Installed_apps(Settings.py)
10.Crei um app
11.Adicionei o app em Installed_apps
12.Criei meu modelo com três classes
-1.A classe Champions League que irá receber a temporada dela e retornar a temporada
-2.A classe Time que irá receber nome do time, estádio e a temporada da classe Champions League e irá retornar a temporada
-3.A classe jogador que irá receber nome do jogador, a posição e o time da classe Time e irá retornar o time dele
13.Em Serializer eu importei as classes que estavam no models e fiz classses serializers que irão transformar python para json e vice-versa
-1.A classe Champions League irá receber um model e fields. 
-2.A classe Time irá receber um model e fields
-3.A classe Jogador irá receber um model e fields
14.Em views eu importei os models e serializers e criei classes que irão setar a vizualização
-1.Cada classe irá receber um queryset e um serializer_class, o queryset irá receber os objetos de cada classe
15.Em urls eu inclui o include e criei uma url para o site da API ROOTS
16.Depois criei um aarquivo urls no app e criei rotas nele importando os viewsets e o routers
17.Digitei o comando python manage.py makemigrations para criar minhas migrações com o banco de dados
18.E após isso o migrate para realmente acionar as migrações(empurrar)
19.Dei um runserver e corri pro abraço
