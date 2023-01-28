import sys
from krita import *

def adicionar_borda(imagem, largura_borda, cor_borda):
    # gets the atual selection
    selecao = imagem.selection()
    # create a new layer for the edge
    camada_borda = imagem.createLayer("Borda")
    # set the collor of the edge
    camada_borda.fill(cor_borda)
    # set the position and the size of the edge
    camada_borda.setX(selecao.x() - largura_borda)
    camada_borda.setY(selecao.y() - largura_borda)
    camada_borda.setWidth(selecao.width() + largura_borda * 2)
    camada_borda.setHeight(selecao.height() + largura_borda * 2)
    # adiciona a camada à imagem
    imagem.addNode(camada_borda)

# ask the user the edge width
largura_borda = int(input("Insira a largura da borda em pixels: "))

# gets the image
imagem_ativa = Application.activeImage()

# add the black edge
adicionar_borda(imagem_ativa, largura_borda, "#000000")
