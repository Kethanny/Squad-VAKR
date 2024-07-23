import requests
from faker import Faker
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image, ImageDraw  
import io

fake = Faker('pt_BR')

def salvar_json(logjson: str, conteudo: str):
    with open(logjson, 'w') as arquivo:
        arquivo.write(conteudo + '\n')
    print(f'Dados salvos em {logjson}.')

def criar_user_api() -> bool:
    endpoint_criaruser = "https://apipf.jogajuntoinstituto.org/register"

    user = {
        "email": fake.email(),
        "password": fake.password()
    }
    response = requests.post(endpoint_criaruser, json=user)

    if response.status_code == 200:
        print('Usuário criado com sucesso!')
        print(response.json())
        salvar_json('log_criacao.json', json.dumps(user, indent=4))
        return True
    else:
        print('Falha ao criar usuário.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('log_criacao.json', json.dumps(response.json(), indent=4))
        return False

def login_user_api() -> str:
    endpoint_login = 'https://apipf.jogajuntoinstituto.org/login'

    try:
        with open('log_criacao.json', 'r') as arquivo:
            user = json.load(arquivo)
    except Exception as e:
        print('Erro ao ler o arquivo JSON:', e)
        return None

    login_data = {
        'email': user["email"],
        'password': user["password"]
    }

    response = requests.post(endpoint_login, json=login_data)

    if response.status_code == 200:
        print('Login realizado com sucesso!')
        print(response.json())
        salvar_json('resposta_api.json', json.dumps(response.json(), indent=4))
        return response.json().get('token')
    else:
        print('Falha ao realizar login.')
        print('Status code:', response.status_code)
        try:
            print('Resposta:', response.json())
        except json.JSONDecodeError:
            print('Resposta: Não foi possível decodificar a resposta JSON.')
        salvar_json('resposta_api.json', json.dumps(response.json(), indent=4) if response.content else 'Resposta vazia')
        return None

def gerar_imagem():
    
    img = Image.new('RGB', (100, 100), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Fake Image", fill=(255, 255, 0))

    # Salvar imagem em um buffer
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    buf.seek(0)
    return buf

def cadastrar_produto_api(token: str):
    endpoint_cadastrarproduto = 'https://apipf.jogajuntoinstituto.org/'  
    headers = {
        'Authorization': f'Bearer {token}',
    }

    produto = {
        "name": fake.word(),
        "price": str(round(fake.random_number(digits=2), 2)),
        "description": fake.text(),
        "category": fake.word(),
        "shipment": str(round(fake.random_number(digits=2), 2)),
    }

   
    imagem_buffer = gerar_imagem()

    m = MultipartEncoder(
        fields={
            'name': produto['name'],
            'description': produto['description'],
            'price': produto['price'],
            'category': produto['category'],
            'shipment': produto['shipment'],
            'image': ('image.jpg', imagem_buffer, 'image/jpeg')
        }
    )

    headers['Content-Type'] = m.content_type

    print(f'Dados do produto: {produto}')
    print(f'Headers: {headers}')

    response = requests.post(endpoint_cadastrarproduto, data=m, headers=headers)

    if response.status_code == 200:
        print('Produto cadastrado com sucesso!')
        print(response.json())
        salvar_json('produto_cadastro.json', json.dumps(response.json(), indent=4))
    else:
        print('Falha ao cadastrar produto.')
        print('Status code:', response.status_code)
        try:
            print('Resposta:', response.json())
        except json.JSONDecodeError:
            print('Resposta: Não foi possível decodificar a resposta JSON.')
        salvar_json('produto_cadastro.json', json.dumps(response.json(), indent=4) if response.content else 'Resposta vazia')


if criar_user_api():
    token = login_user_api()
    if token:
        cadastrar_produto_api(token)