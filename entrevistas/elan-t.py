import spacy
import string
import sys
import re
import os

tags_stoplist = ['SPACE', 'PUNCT', 'SYM']
stoplist = ['eh', 'hes', 'HES', 'RISOS', 'risos', 'BARULHO', 'INTERVENIENTE', 'PIGARRO', 'pigarro', 'CHORO', 'RUÍDO', 'RUÍDOS', 'est', 'EST']

def verifica_token(token):
    if (token.text.isupper() == True) or (str(token.pos_) in tags_stoplist) or (token.text in stoplist):
        return True
    else: return False

def verifica_linha(linha):
    return bool(re.search(r'\d{2,20}', linha))

def tagger(entrevista):
    ent_etiquetada = []
    
    nlp = spacy.blank("pt")
    nlp = spacy.load("pt_core_news_lg")

    arquivo = open(entrevista, encoding='utf-8').readlines()
    
    for linha in arquivo:
        temp = []
        if verifica_linha(linha) == False:
            doc = nlp(linha)
            for token in doc:
                if verifica_token(token) == False:
                    temp.append(f"{token.orth_}_{token.pos_}{token.whitespace_}")
                else:
                    temp.append(f"{token.orth_}{token.whitespace_}")
            ent_etiquetada.append(''.join(temp))
        else:
            ent_etiquetada.append(linha)

    return ent_etiquetada

def main():
    ARQUIVO = sys.argv[1]
    DIR = os.getcwd()
    ENTREVISTA = os.path.join(DIR, ARQUIVO)
    print(f"Etiquetando entrevista: {ARQUIVO}\n")

    entrevista_etiquetada = tagger(ENTREVISTA)
    novo_arquivo = DIR + f"\TAG_{ARQUIVO}"

    f = open(novo_arquivo, 'w')
    f.writelines(entrevista_etiquetada)
    f.close()

    print(f"Entrevista etiquetada com sucesso!\nO novo arquivo foi salvo no caminho: {novo_arquivo}")

if __name__ == "__main__":
    main()