# gdrive-api

## Run
Para executar o script é necessário instalar os pacotes:
> pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2 PyPDF2

Em Seguida execute no terminal:
> python3 main.py --noauth_local_webserver

O script vai pedir para acessar um link na web e fazer o login com sua conta do google, e logo em seguida você receberá um código para ser inserido na execução do programa. Logo após inserir essas suas credenciais ficaram salvas em uma pasta dentro do projeto e será liberado o acesso ao seu drive.

