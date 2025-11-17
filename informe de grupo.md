Integrantes:
Schimpf Marcos Gabriel
Brandan Luca Leandro
salvador lopez ogawa

Informe:

Marcos Schimpf:
La primera desicion que tuve fue la de buscar informacion de la funcionalidad de los algoritmos requeridos, mirando lo dificiles o faciles que serian de implementar a medida que el proyecto avance para luego decidir si implementar los opcionales, por medio de las siguientes paginas web:

https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/
https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/?_x_tr_sl&_x_tr_tl&_x_tr_hl
https://www.programiz.com/dsa/selection-sort

La primera dificultad fue averiguar que significaba cada variable (en sort_bubble), deduciendo que N era la longitud de la lista a ordenar, I era el numero de pasadas que tuvo la lista, y J era el indice de los 2 numeros a comparar. y actuando en step() como si fuera un ciclo "While done == False".
Con estas fuentes, prueba y error buscando lo que funcionaba y lo que estaba mal, y mirando los resultados en el HTML dado, fue medianamente simple, aunque no facil, formar el primer algoritmo de ordenamiento sort_bubble.

Durante el desarrollo del algoritmo sort_selection y despues de varios prototipos, me encontre con el problema que en un punto el grafico se quedaba atascado en el ultimo J y no continuaba a la fase "swap", antes de darme cuenta de un error basico en el cambio de fase cuando use == en vez de =, un error tonto pero humano. Despues de eso y doble chequeando cada variable, y unos tests mas con pocas complicaciones quedo bien implementado el algoritmo sort_selection


Luca Brandan:
En este caso tuve que resolver el algoritmo de insercion ordenada, asi que investigue como funcionaba, me concentre en verlo en forma de grafico sin ver codigo, Luego que entendi como funcionaba, lo empece a implementar en la pagina, tuve varios problemas, primero que no sabia que las variables globales se les hacia referencias, con la palabra reservada global, luego otro problema que tuve es que el algoritmo se quedaba trabado, pese a pensar que lo implementaba bien, esto fue por que al final me olvide de retornar el diccionario con el done en false, y por ultimo , el algoritmo parecia funcionar bien , pero solo lo comparaba con el elemento anterior, no con todos los anteriores, asi que me di cuenta que habia que restarle uno a i cada vez que el anterior era mayor al actual

salvador lopez ogawa:
Al principio, me costó mucho entender QuickSort, especialmente su adaptación iterativa y paso a paso. No estaba familiarizado con la partición, el manejo de índices y la pila de rangos. Mi código inicial tenía bugs, como bucles infinitos en la partición y subrangos incorrectos, lo que impedía ordenar completamente el array.vi videos en YouTube y leí páginas web como GeeksforGeeks, que explicaron QuickSort iterativo y el algoritmo de Lomuto.
El principal problema que tuve fue entender el funcionamiento del github, me perdi mucho pero pude entenderlo gracias a videos.
