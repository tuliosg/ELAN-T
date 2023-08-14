import spacy
import sys
import re
import os

tags_stoplist = ['SPACE', 'PUNCT', 'SYM']
stoplist = ['eh', 'hes', 'HES', 'RISOS', 'risos', 'BARULHO', 'INTERVENIENTE', 'PIGARRO', 'pigarro', 'CHORO', 'RUÍDO', 'RUÍDOS', 'est', 'EST']

def verifica_token(token):
    return bool((token.text.isupper()) or (str(token.pos_) in tags_stoplist) or (token.text in stoplist))

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
    DIR = sys.argv[1]
    if os.path.exists(f"{DIR}\_tagged") == False:
        os.mkdir(f"{DIR}\_tagged")

    for ARQUIVO in os.listdir(path=DIR):
        ENTREVISTA = os.path.join(DIR, ARQUIVO)
        if os.path.isfile(ENTREVISTA) ==  True:
            print(f"Etiquetando entrevista: {ARQUIVO}")

            entrevista_etiquetada = tagger(ENTREVISTA)
            novo_arquivo = DIR + f"\_tagged\TAG_{ARQUIVO}"

            f = open(novo_arquivo, 'w')
            f.writelines(entrevista_etiquetada)
            f.close()
            print(f"{ARQUIVO} etiquetada com sucesso.\n")
            print("="*75)

    print(f"Entrevista(s) etiquetada(s) com sucesso!\nPasta do(s) arquivo(s) etiquetado(s): {DIR}\_tagged")

if __name__ == "__main__":
    main()