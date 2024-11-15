import pymongo
import pymongo.errors
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def mongoDB():
    uri = "mongodb+srv://recycleadmin:garmKotmSHAwyGcg@cluster0.flsfq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        db=client.get_database('db_recycle')
        return db
    except Exception as e:
        print(e)
        
#usei esse bloco pra inserir os feitos
""" db = mongoDB()

dados = [
    {
      "nv_rec": 10,
      "titulo": "Economia de Água com Papel",
      "frase": "Reciclando 20 folhas de papel, você economiza aproximadamente 1 litro de água. Ótimo trabalho – cada folha conta!",
      "imagem": "assets/imgfeito1"
    },
    {
      "nv_rec": 30,
      "titulo": "Salvar Árvores com Papel Reciclado",
      "frase": "Cada 50 kg de papel reciclado salva uma árvore inteira. Parabéns por fazer parte dessa preservação!",
      "imagem": "assets/imgfeito2"
    },
    {
      "nv_rec": 50,
      "titulo": "Conservação de Água na Reciclagem de Papel",
      "frase": "Reciclar 1 tonelada de papel evita o uso de 26 mil litros de água. Você está ajudando a conservar nossos recursos!",
      "imagem": "assets/imgfeito3"
    },
    {
      "nv_rec": 70,
      "titulo": "Energia Economizada com Papel",
      "frase": "Ao reciclar 100 folhas de papel, você economiza energia suficiente para iluminar uma lâmpada por 3 horas. Continue assim – sua contribuição é essencial!",
      "imagem": "assets/imgfeito4"
    },
    {
      "nv_rec": 90,
      "titulo": "Redução de CO₂ com Papel",
      "frase": "Com a reciclagem de 100 kg de papel, você evita a emissão de 30 kg de CO₂. Excelente trabalho – você está ajudando a reduzir a poluição!",
      "imagem": "assets/imgfeito5"
    },
    {
      "nv_rec": 110,
      "titulo": "Energia com Garrafas PET",
      "frase": "Reciclar 10 garrafas PET economiza energia equivalente a ligar uma lâmpada por 5 horas. Muito bem – cada garrafa faz diferença!",
      "imagem": "assets/imgfeito6"
    },
    {
      "nv_rec": 130,
      "titulo": "Economia de Petróleo com Plástico",
      "frase": "Cada 1 kg de plástico reciclado economiza 2 litros de petróleo. Incrível, você está ajudando a poupar recursos preciosos!",
      "imagem": "assets/imgfeito7"
    },
    {
      "nv_rec": 150,
      "titulo": "Nova Vida ao Plástico",
      "frase": "Com 50 garrafas de plástico recicladas, é possível produzir uma camiseta nova. Parabéns – sua reciclagem está dando vida nova ao plástico!",
      "imagem": "assets/imgfeito8"
    },
    {
      "nv_rec": 170,
      "titulo": "Energia com Sacolas Plásticas",
      "frase": "A cada 500 sacolas plásticas recicladas, economiza-se energia suficiente para carregar um celular por um ano. Fantástico – sua ação ajuda a reduzir o desperdício!",
      "imagem": "assets/imgfeito9"
    },
    {
      "nv_rec": 190,
      "titulo": "Redução de CO₂ com Plástico",
      "frase": "Reciclando 1 tonelada de plástico, evita-se a emissão de até 1 tonelada de CO₂. Você está protegendo o planeta – continue assim!",
      "imagem": "assets/imgfeito10"
    },
    {
      "nv_rec": 210,
      "titulo": "Energia com Latas de Alumínio",
      "frase": "Reciclar uma lata de alumínio economiza energia suficiente para manter uma TV ligada por 3 horas. Parabéns – cada lata conta para um futuro mais limpo!",
      "imagem": "assets/imgfeito11"
    },
    {
      "nv_rec": 230,
      "titulo": "Preservação com Alumínio",
      "frase": "Cada 1 tonelada de alumínio reciclado evita a extração de 5 toneladas de bauxita. Incrível trabalho – você está ajudando a preservar nossos recursos naturais!",
      "imagem": "assets/imgfeito12"
    },
    {
      "nv_rec": 250,
      "titulo": "Energia com Latas de Alumínio",
      "frase": "Com 6 latas de alumínio recicladas, você economiza energia para fazer funcionar uma lâmpada LED por 24 horas. Excelente! Sua reciclagem tem um impacto enorme!",
      "imagem": "assets/imgfeito13"
    },
    {
      "nv_rec": 270,
      "titulo": "Economia de Minério com Aço",
      "frase": "Reciclando 1 kg de aço, economiza-se cerca de 1 kg de minério de ferro. Continue assim – sua ajuda é essencial para o meio ambiente!",
      "imagem": "assets/imgfeito14"
    },
    {
      "nv_rec": 290,
      "titulo": "Energia com Latas de Alumínio",
      "frase": "Ao reciclar 100 latas, você economiza energia para fazer funcionar um laptop por 30 horas. Parabéns – suas ações fazem a diferença!",
      "imagem": "assets/imgfeito15"
    },
    {
      "nv_rec": 310,
      "titulo": "Redução de CO₂ com Vidro",
      "frase": "Reciclar 1 kg de vidro evita a emissão de 300 g de CO₂ na atmosfera. Ótimo trabalho – o planeta agradece!",
      "imagem": "assets/imgfeito16"
    },
    {
      "nv_rec": 330,
      "titulo": "Energia com Vidro Reciclado",
      "frase": "Cada vidro reciclado economiza energia suficiente para manter uma lâmpada de LED acesa por 8 horas. Parabéns – cada reciclagem é uma vitória para o meio ambiente!",
      "imagem": "assets/imgfeito17"
    },
    {
      "nv_rec": 350,
      "titulo": "Economia de Areia com Vidro",
      "frase": "Com 1 tonelada de vidro reciclado, você economiza 700 kg de areia, preservando nossos recursos naturais. Excelente – continue sendo parte dessa mudança!",
      "imagem": "assets/imgfeito18"
    },
    {
      "nv_rec": 370,
      "titulo": "Energia com Garrafas de Vidro",
      "frase": "Reciclando 4 garrafas de vidro, economiza-se energia suficiente para ferver 10 xícaras de água. Muito bem – cada garrafa reciclada faz diferença!",
      "imagem": "assets/imgfeito19"
    },
    {
      "nv_rec": 390,
      "titulo": "Iluminação com Garrafas de Vidro",
      "frase": "Reciclar 100 garrafas de vidro pode iluminar uma casa pequena por até 10 dias. Impressionante! Sua ação é um passo para um futuro mais sustentável!",
      "imagem": "assets/imgfeito20"
    }
]

try:
   
    db.feitos.insert_many(dados)
    print("Dados inseridos com sucesso!")

except pymongo.errors.PyMongoError as e:
    print(f"Erro ao inserir dados: {e}") """