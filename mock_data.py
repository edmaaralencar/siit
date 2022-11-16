atracao1 ={
    'ID':1,
    'NOME':"Restaurante Beiramar",
    'DESCRICAO': "Melhores frutos do mar de Maceió.",
    'TIPO': "alimentação",
    'HORARIOS': "dia"
}
atracao2 ={
    'ID':2,
    'NOME':"Praia do Sol",
    'DESCRICAO': "Bela praia com piscinas naturais e passeios de bugre.",
    'TIPO':"praia",
    'HORARIOS': "dia"
}
atracao3 ={
    'ID':3,
    'NOME':"Boate Love",
    'DESCRICAO': "Melhor boate de Maceió.",
    'TIPO':"balada",
    'HORARIOS': "noite"
}
atracao4 ={
    'ID':4,
    'NOME':"Feira de Artesanato",
    'DESCRICAO': "Artesanato típico de Alagoas.",
    'TIPO':"compras",
    'HORARIOS': 'noite,dia'
}
atracao5 ={
    'ID':5,
    'NOME':"Bar do Jangadeiro",
    'DESCRICAO': "Jovens reunidos, cerveja gelada e ótimos petiscos.",
    'TIPO':"alimentação,balada",
    'HORARIOS': 'noite'
}

lista_atracoes = [atracao1,atracao2,atracao3,atracao4,atracao5]

roteiro1 = {
    'ID':1,
    'NOME':"Roteiro Família",
    'ATRACOES': [atracao2,atracao1,atracao4]
}
roteiro2 = {
    'ID':2,
    'NOME':"Roteiro Noturno",
    'ATRACOES': [atracao5,atracao3]
}
roteiro3 = {
    'ID':3,
    'NOME':"Roteiro Praia e Gastronomia",
    'ATRACOES': [atracao2,atracao1,atracao5]
}

roteiros= [roteiro1,roteiro2,roteiro3]
