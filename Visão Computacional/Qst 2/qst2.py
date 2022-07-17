import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1ª PARTE: Calcular a média, o desvio padrão e a variância, para 20 amostragens (3 bandas e média das 3);

# Carregar imagem. Criar uma lista para cada banda de cor, e uma para escala de cinza
imgs = []
for n in range(1, 21):
    imgs.append("./imagens/"+str(n)+".png")


lista_imagem = []
lista_cinza = []

for n in range(len(imgs)):
    lista_imagem.append(cv2.imread(imgs[n]))
    lista_cinza.append(cv2.imread(imgs[n], cv2.IMREAD_GRAYSCALE))
lista_imagem = np.array(lista_imagem)
lista_cinza = np.array(lista_cinza)

img_verm = lista_imagem[:, :, :, 2]
img_verde = lista_imagem[:, :, :, 1]
img_azul = lista_imagem[:, :, :, 0]

# Vizulaização de uma das imagens
# plt.title("Exemplo de uma das imagens")
# plt.imshow(cv.cvtColor(lista_imagem[0], cv.COLOR_BGR2RGB))
# plt.show()


# Calculo da Imagem média, imagem média em escala de cinza e imagem média para cada canal
media_img = np.mean(lista_imagem, axis=0, dtype=float)
media_img = np.array(media_img, dtype=np.uint8)

media_cinza = np.mean(lista_cinza, axis=0, dtype=float)
media_cinza = np.array(media_cinza, dtype=np.uint8)

media_verm = np.mean(lista_imagem[:, :, :, 0], axis=0, dtype=int)
media_verm = np.array(media_verm, dtype=np.uint8)

media_verde = np.mean(lista_imagem[:, :, :, 1], axis=0, dtype=int)
media_verde = np.array(media_verde, dtype=np.uint8)

media_azul = np.mean(lista_imagem[:, :, :, 2], axis=0, dtype=int)
media_azul = np.array(media_azul, dtype=np.uint8)

# Vizualização imagem média e imagem média de cinza
#plt.title("Imagem média")
#plt.imshow(cv.cvtColor(media_img, cv.COLOR_BGR2RGB))
# plt.show()

#plt.title("Imagem média:Escala de cinza")
#plt.imshow(cv.cvtColor(media_cinza, cv.COLOR_BGR2RGB))
# plt.show()

# Cálculo do desvio padrão em cada canal e na escala de cinza
std_cinza = np.std(lista_cinza, axis=0)
std_verm = np.std(img_verm, axis=0)
std_verde = np.std(img_verde, axis=0)
std_azul = np.std(img_azul, axis=0)
# plt.title("Desvio Padrão:Escala de cinza")
# plt.imshow(std_cinza)
# plt.colorbar()
# plt.show()
# plt.title("Desvio Padrão:Vermelho")
# plt.imshow(std_verm)
# plt.colorbar()
# plt.show()
# plt.title("Desvio Padrão:Verde")
# plt.imshow(std_verde)
# plt.colorbar()
# plt.show()
# plt.title("Desvio Padrão:Azul")
# plt.imshow(std_azul)
# plt.colorbar()
# plt.show()

# Mesmo procedimento para a variância
var_cinza = np.std(img_azul, axis=0)
var_verm = np.std(lista_cinza, axis=0)
var_green = np.std(img_verm, axis=0)
var_azul = np.std(img_verde, axis=0)

# plt.title("Variância:Escala de cinza")
# plt.imshow(var_cinza)
# plt.colorbar()
# plt.show()
# plt.title("Variância:Canal Vermelho")
# plt.imshow(var_verm)
# plt.colorbar()
# plt.show()
# plt.title("Variância:Canal Verde")
# plt.imshow(var_green)
# plt.colorbar()
# plt.show()
# plt.title("Variância:Canal Azul")
# plt.imshow(var_azul)
# plt.colorbar()
# plt.show()

# 2ª PARTE: Escolher uma determinada linha da imagem e plotar um gráfico mostrando, para cada pixel, duas curvas: média mais desvio padrão; média menos desvio padrão (3 bandas e média das 3).

linha_md_cin = media_cinza[int(len(media_img)/2), :]
linha_std_cinza = std_cinza[int(len(media_img)/2), :]
linha_md_cza_max = linha_md_cin + linha_std_cinza
linha_md_cza_neg = linha_md_cin - linha_std_cinza

linha_md_verm = media_verm[int(len(media_img)/2), :]
linha_std_verm = std_verm[int(len(media_img)/2), :]
linha_md_verm_max = linha_md_verm + linha_std_verm
linha_md_verm_min = linha_md_verm - linha_std_verm

linha_mds_verd = media_verde[int(len(media_img)/2), :]
linha_std_verd = std_verde[int(len(media_img)/2), :]
linha_md_vrd_max = linha_mds_verd + linha_std_verd
linha_md_vrd_min = linha_mds_verd - linha_std_verd

linha_md_azl = media_azul[int(len(media_img)/2), :]
linha_std_azul = std_azul[int(len(media_img)/2), :]
linha_md_azl_max = linha_md_azl + linha_std_azul
linha_md_azl_min = linha_md_azl - linha_std_azul


# plt.title("Line Red")
# plt.plot(linha_md_verm)
# plt.plot(linha_md_verm_max)
# plt.plot(linha_md_verm_min)
# plt.show()

# plt.title("Line Green")
# plt.plot(linha_mds_verd)
# plt.plot(linha_md_vrd_max)
# plt.plot(linha_md_azl_min)
# plt.show()

# plt.title("Line Blue")
# plt.plot(linha_md_azl)
# plt.plot(linha_md_azl_max)
# plt.plot(linha_md_azl_min)
# plt.show()

# plt.title("Line Grey")
# plt.plot(linha_md_cin)
# plt.plot(linha_md_cza_max)
# plt.plot(linha_md_cza_neg)
# plt.show()

# Indique outros dados da imagem (nível de cinza mínimopara cada cor, nível máximo para cada cor, mostre 5 imagens das 20 adquiridas, taxa de amostragem máxima, etc).

# Lista com 5 imagens em cada banda
img_verm_5 = img_verm[0:5]
img_verde_5 = img_verde[0:5]
img_azul_5 = img_azul[0:5]

# Máximo e mínimo de cada cor em cada imagem
for n in range(len(img_verm_5)):
    print("Max vermelho na img", (n+1), ":", np.max(img_verm_5[n]))
print("")
for n in range(len(img_verm_5)):
    print("Min vermelho na img", (n+1), ":", np.min(img_verm_5[n]))
print("")
for n in range(len(img_verde_5)):
    print("Max verde na img", (n+1), ":", np.max(img_verde_5[n]))
print("")
for n in range(len(img_verde_5)):
    print("Min verde na img", (n+1), ":", np.min(img_verde_5[n]))
print("")
for n in range(len(img_azul_5)):
    print("Max azul na img", (n+1), ":", np.max(img_azul_5[n]))
print("")
for n in range(len(img_azul_5)):
    print("Min azul na img", (n+1), ":", np.min(img_azul_5[n]))

# Histograma de cada imagem em cada canal de cor

for n in range(1, 6):
    n1 = str(n)
    plt.title("Histograma img " + n1)
    image = lista_imagem[n-1]
    for i, col in enumerate(['r', 'g', 'b']):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.legend(['Vermelho', 'Verde', 'Azul'])
        plt.xlim([0, 256])
    plt.show()
