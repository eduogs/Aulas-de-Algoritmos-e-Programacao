# Eduardo - Matéria de Algoritmos e Programação
#Aluno Eduardo Oliveira Gomes

#Instanciando o sistema
app = WebmotorsCRUD()

#Vendedor cadastrando veículos com Fotos e Vídeos
v1 = app.cadastrar_veiculo(
    tipo="Carro",
    marca="Toyota",
    modelo="Corolla XEi 2.0",
    ano_fab=2021,
    ano_mod=2022,
    preco=115000.00,
    km=35000,
    cidade="São Luís",
    estado="MA",
    lista_fotos=["/uploads/foto1.jpg", "/uploads/foto2.jpg"],
    lista_videos=["/uploads/tour_carro.mp4"]
)

v2 = app.cadastrar_veiculo(
    tipo="Carro",
    marca="Honda",
    modelo="Civic Touring",
    ano_fab=2020,
    ano_mod=2020,
    preco=128000.00,
    km=48000,
    cidade="São Paulo",
    estado="SP",
    lista_fotos=["/uploads/civic1.png"]
)

v3 = app.cadastrar_veiculo(
    tipo="Moto",
    marca="Honda",
    modelo="CB 500F",
    ano_fab=2023,
    ano_mod=2023,
    preco=39000.00,
    km=5000,
    cidade="São Luís",
    estado="MA",
    lista_fotos=["/uploads/moto1.jpg"]
)

#Comprador fazendo buscas avançadas

print("--- Busca 1: Todos os carros Toyota ---")
busca_toyota = app.buscar_veiculos(tipo="Carro", marca="Toyota")
for car in busca_toyota:
    print(car, "| Fotos:", len(car.fotos), "| Vídeos:", len(car.videos))

print("\n--- Busca 2: Veículos até R$ 120.000 no MA ---")
busca_regiao = app.buscar_veiculos(preco_max=120000.00, estado="MA")
for item in busca_regiao:
    print(item)

print("\n--- Busca 3: Apenas anúncios que possuem VÍDEO ---")
busca_video = app.buscar_veiculos(apenas_com_video=True)
for item in busca_video:
    print(item, "| Vídeo:", item.videos[0])
