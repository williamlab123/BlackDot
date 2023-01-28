import sys
from krita import *

def adicionar_borda(imagem, largura_borda, cor_borda):
    # obtém a seleção atual
    selecao = imagem.selection()
    # cria uma nova camada para a borda
    camada_borda = imagem.createLayer("Borda")
    # configura a cor da borda
    camada_borda.fill(cor_borda)
    # configura a posição e tamanho da camada
    camada_borda.setX(selecao.x() - largura_borda)
    camada_borda.setY(selecao.y() - largura_borda)
    camada_borda.setWidth(selecao.width() + largura_borda * 2)
    camada_borda.setHeight(selecao.height() + largura_borda * 2)
    # adiciona a camada à imagem
    imagem.addNode(camada_borda)

# pergunta ao usuário a largura da borda
largura_borda = int(input("Insira a largura da borda em pixels: "))

# obtém a imagem ativa
imagem_ativa = Application.activeImage()

# adiciona a borda preta
adicionar_borda(imagem_ativa, largura_borda, "#000000")