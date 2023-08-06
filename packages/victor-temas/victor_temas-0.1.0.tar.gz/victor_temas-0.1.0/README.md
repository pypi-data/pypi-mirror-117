# Victor Temas

## Modo de uso
Importe a classe VictorThemes, do arquivo victor_temas/victor_themes.py
Instancie a classe VictorThemes com os parametros: tfidf, vectorizer e o DataFrame de temas.
O método predict recebe um texto não processado e retorna uma lista de resultados sobre o texto para cada tema, cada elemento é uma tupla contendo:
1. Pertinência não limitada
2. Similaridade mínima entre o texto de entrada e os textos do tema analisado
3. Similaridade média entre o texto de entrada e os textos do tema analisado
4. Similaridade máxima entre o texto de entrada e os textos do tema analisado
5. A lista de temas sendo analisada
6. O número de amostras contidas nesse tema.

Os parâmetros opcionais da funcao predict são:
1. ordenar_por. Domínio:['pertinencia','similaridade'], valor default:'pertinencia'.
Define a ordem de ordenacão da lista de saída do método predict. 
Caso seja 'pertinencia', ordena os elementos por maior 

limiar_pert=-10000, limiar_sim=0

Exemplo:    
    
    from victor_temas import VictorThemes
 
    vt=VictorThemes(TFIDF_PATH, VEC_PATH,THEMES_PATH)
    vt.predict(texto)