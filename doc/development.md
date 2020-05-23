## Definición de términos

Los encuestados representan una medida muestral <img src="https://render.githubusercontent.com/render/math?math=N"> de la población de la que se desea obtener información. Para la muestra es de interés notar aquellas observaciones <img src="https://render.githubusercontent.com/render/math?math=n"> en donde esté presente la condición <img src="https://render.githubusercontent.com/render/math?math=C"> de la que se desea conocer una relación, donde <img src="https://render.githubusercontent.com/render/math?math=\textbf{C ='Lenin Moreno'}">. En este caso <img src="https://render.githubusercontent.com/render/math?math=X"> es una respuesta que puede estar presente en la población encuestada <img src="https://render.githubusercontent.com/render/math?math=N_x">:


<img src="https://render.githubusercontent.com/render/math?math=\left ( N \bigcap X \right )">

Por otro lado, las observaciones donde se encuentra presente la condición <img src="https://render.githubusercontent.com/render/math?math=C"> se define como <img src="https://render.githubusercontent.com/render/math?math=N_c"> y se interpreta como:

<img src="https://render.githubusercontent.com/render/math?math=\left ( N \bigcap C \right )">

Por último, las observaciones donde se encuentra presente la condición <img src="https://render.githubusercontent.com/render/math?math=C"> y la respuesta <img src="https://render.githubusercontent.com/render/math?math=X"> se define como <img src="https://render.githubusercontent.com/render/math?math=N_{cx}"> y se interpreta como:

<img src="https://render.githubusercontent.com/render/math?math=\left ( N \bigcap C \bigcap X \right )">

Definimos a la probabilidad de encontrar una observación dentro de la población en la que esté presente la condición <img src="https://render.githubusercontent.com/render/math?math=C">, <img src="https://render.githubusercontent.com/render/math?math=P(C)"> como la siguiente ecuación:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \right ) = \frac{N_c}{N}">

Definimos a la probabilidad de encontrar una observación dentro de la población en la que esté presente la característica <img src="https://render.githubusercontent.com/render/math?math=X">, <img src="https://render.githubusercontent.com/render/math?math=P(X)"> como la siguiente ecuación:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( X \right ) = \frac{N_x}{N}">

Para determinar la probabilidad condicional de observar <img src="https://render.githubusercontent.com/render/math?math=X"> cuando se observa <img src="https://render.githubusercontent.com/render/math?math=C">, <img src="https://render.githubusercontent.com/render/math?math=P(C|X)"> Se tiene:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right ) = \frac{N_{cx}}{N_x}">

## Naive Bayes

Antes de continuar con el desarrollo del clasificador es necesario hablar de un método de deducción del que se ha partido. El método de naive Bayes asume <img src="https://render.githubusercontent.com/render/math?math=K"> subpoblaciones <img src="https://render.githubusercontent.com/render/math?math=S_1, S_2, \dots, S_k"> mutuamente excluyentes con probabilidades <img src="https://render.githubusercontent.com/render/math?math=P(S_1), P(S_2), \dots, P(S_k)">. Si ocurre un evento <img src="https://render.githubusercontent.com/render/math?math=A"> la brobabilidad posterior de <img src="https://render.githubusercontent.com/render/math?math=S_i"> dado <img src="https://render.githubusercontent.com/render/math?math=A"> es la probabilidad condicional:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( S_i \mid A \right ) = \frac{P\left ( S_i \right )P\left ( A \mid S_i \right )}{\sum_{j=i}^{K}P\left ( S_j \right )P\left ( A \mid S_j \right )}">

## Score

¿Qué tan probable es que un elemento de los registros pertenezca a la clase <img src="https://render.githubusercontent.com/render/math?math=C">?

La medida de de Score <img src="https://render.githubusercontent.com/render/math?math=S"> es una medida de confiabilidad de que la variable <img src="https://render.githubusercontent.com/render/math?math=X_i"> que está siendo observada pertenezca a la clase <img src="https://render.githubusercontent.com/render/math?math=C">. Del teorema de naive Bayes tenemos que:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right ) = \frac{P\left ( X \mid C \right )P\left ( C \right )}{P\left ( X \right )}">

Donde:
- <img src="https://render.githubusercontent.com/render/math?math=P\left (  X \right )">: Probabilidad a priori.
- <img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right )">: Probabilidad a posteriori.
- <img src="https://render.githubusercontent.com/render/math?math=P\left ( X \mid C \right )">: Función de probabilidad condicional.

Expandiendo para la variable <img src="https://render.githubusercontent.com/render/math?math=X">:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right ) = \frac{P\left ( X_1,X_2, \cdots ,X_n \mid C \right )P\left ( C \right )}{P\left ( X_1, X_2, \cdots, X_n \right )}">

También se usa la regla de Bayes para su complemento <img src="https://render.githubusercontent.com/render/math?math=\bar{C}">:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( \bar{C} \mid X \right ) = \frac{P\left ( X_1,X_2, \cdots ,X_n \mid \bar{C} \right )P\left ( \bar{C} \right )}{P\left ( X_1, X_2, \cdots, X_n \right )}">

Se relacionan las dos ecuaciones para <img src="https://render.githubusercontent.com/render/math?math=C"> y para <img src="https://render.githubusercontent.com/render/math?math=\bar{C}">, asumiendo de que cada <img src="https://render.githubusercontent.com/render/math?math=X_i"> es independiente:

<img src="https://render.githubusercontent.com/render/math?math=\frac{P\left ( C \mid X \right )}{P\left ( \bar{C} \mid X \right )} = \frac{\frac{P\left ( X \mid C \right )P\left ( C \right )}{P\left ( X \right )}}{\frac{P\left ( X \mid \bar{C} \right )P\left ( \bar{C} \right )}{P\left ( X \right )}}">

También se tiene lo siguiente:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( X \mid C \right ) = \prod_{1}^{n} P\left ( X \mid C \right )">

<img src="https://render.githubusercontent.com/render/math?math={S}'\left ( X \right ) = ln\frac{P\left ( C \mid X \right )}{P\left ( \bar{C} \mid X \right )}">

<img src="https://render.githubusercontent.com/render/math?math={S}'\left ( X \right ) = ln\frac{\prod_{1}^{n}P\left ( C \mid X_i \right )}{\prod_{1}^{n}P\left ( \bar{C} \mid X_i \right )} + ln\frac{P\left ( C \right )}{P\left ( \bar{C} \right )}">

Aplicando la igualdad de los logaritmos tenemos que <img src="https://render.githubusercontent.com/render/math?math=S(X)">:

<img src="https://render.githubusercontent.com/render/math?math={S}'\left ( X \right ) = \sum_{1}^{n} ln\frac{P\left ( C \mid X_i \right )}{P\left ( \bar{C} \mid X_i \right )}">

Donde:

<img src="https://render.githubusercontent.com/render/math?math=S\left ( X \right ) =  ln\frac{P\left ( C \mid X_i \right )}{P\left ( \bar{C} \mid X_i \right )} = ln\frac{\frac{N_{cx_i}}{N_c}}{\frac{N_{\bar{c}x_i}}{N_{\bar{c}}}}">

Un valor alto en $S$ indica una alta probabilidad de pertenecer a la clase <img src="https://render.githubusercontent.com/render/math?math=C">

## Suavizado de Laplace

El suavizado de laplace evita errores de desbordamiento  provocados por una división entre cero que puede ser expresado con la siguiente ecuación:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( X_i \mid C \right ) = \frac{N_{cx_i} + 1}{N_c + k}">

Donde <img src="https://render.githubusercontent.com/render/math?math=k"> es el total de clases a las que se puede pertenecer (para esta caso solo existen 2).

## Score Classifier

Ya con un score <img src="https://render.githubusercontent.com/render/math?math=S"> obtenido para cada característica <img src="https://render.githubusercontent.com/render/math?math=X">, lo que resta es seleccionar, en función de criterios arbitrarios, los variables que serán tomados en cuenta para la clasificación para nuevos elementos utilizando el modelo ajustado. 

<img src="https://render.githubusercontent.com/render/math?math=S\left ( C \mid X \right ) = \sum_{i=1}^{N} ln\left [ \frac{P \left ( X_i \mid C \right )}{P \left ( X_i \mid \bar{C} \right )} \right ] = \sum_{i=1}^{N} ln\frac{\frac{N_{cx_i}}{N_c}}{\frac{N_{\bar{c}x_i}}{N_{\bar{c}}}}">