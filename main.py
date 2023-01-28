from PIL import Image, ImageDraw


def adicionar_borda(imagem, largura_borda, cor_borda):
  
    imagem_com_borda = Image.new("RGB", (imagem.width + largura_borda * 2, imagem.height + largura_borda * 2), cor_borda)
   
    imagem_com_borda.paste(imagem, (largura_borda, largura_borda))
   
    return imagem_com_borda


imagem = Image.open("imagem.png")


largura_borda = int(input("Insert the edge with in pixels: "))


imagem_com_borda = adicionar_borda(imagem, largura_borda, "black")


imagem_com_borda.save("imagem_com_borda.png")
