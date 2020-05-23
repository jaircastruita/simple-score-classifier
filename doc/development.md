## Definición de términos

Los encuestados representan una medida muestral $N$ de la población de la que se desea obtener información. Para la muestra es de interés notar aquellas observaciones $n$ en donde esté presente la condición $C$ de la que se desea conocer una relación, donde $\textbf{C ='Lenin Moreno'}$. En este caso $X$ es una respuesta que puede estar presente en la población encuestada $N_x$:

<a href="https://render.githubusercontent.com/render/math?math=e%5E%7Bi%20%5Cpi%7D%20%3D%20-1&mode=inline">`https://render.githubusercontent.com/render/math?math=e%5E%7Bi%20%5Cpi%7D%20%3D%20-1&mode=inline`</a>

<img src="https://render.githubusercontent.com/render/math?math=$$\left ( N \bigcap X \right )$$">

Por otro lado, las observaciones donde se encuentra presente la condición $C$ se define como $N_c$ y se interpreta como:

$$\left ( N \bigcap C \right )$$

Por último, las observaciones donde se encuentra presente la condición $C$ y la respuesta $X$ se define como $N_{cx}$ y se interpreta como:

$$\left ( N \bigcap C \bigcap X \right )$$

Definimos a la probabilidad de encontrar una observación dentro de la población en la que esté presente la condición $C$, $P(C)$ como la siguiente ecuación:

$$P\left ( C \right ) = \frac{N_c}{N}$$

Definimos a la probabilidad de encontrar una observación dentro de la población en la que esté presente la característica $X$, $P(X)$ como la siguiente ecuación:

$$P\left ( X \right ) = \frac{N_x}{N}$$

Para determinar la probabilidad condicional de observar $X$ cuando se observa $C$, $P(C|X)$ Se tiene:

$$P\left ( C \mid X \right ) = \frac{N_{cx}}{N_x}$$

## Naive Bayes

Antes de continuar con el desarrollo del clasificador es necesario hablar de un método de deducción del que se ha partido. El método de naive Bayes asume $K$ subpoblaciones $S_1, S_2, \dots, S_k$ mutuamente excluyentes con probabilidades $P(S_1), P(S_2), \dots, P(S_k)$. Si ocurre un evento $A$ la brobabilidad posterior de $S_i$ dado $A$ es la probabilidad condicional:

$$P\left ( S_i \mid A \right ) = \frac{P\left ( S_i \right )P\left ( A \mid S_i \right )}{\sum_{j=i}^{K}P\left ( S_j \right )P\left ( A \mid S_j \right )}$$

## Score

¿Qué tan probable es que un elemento de los registros pertenezca a la clase $C$?

La medida de de Score $S$ es una medida de confiabilidad de que la variable $X_i$ que está siendo observada pertenezca a la clase $C$. Del teorema de naive Bayes tenemos que:

$$P\left ( C \mid X \right ) = \frac{P\left ( X \mid C \right )P\left ( C \right )}{P\left ( X \right )}$$

Donde:
- $P\left (  X \right )$: Probabilidad a priori.
- $P\left ( C \mid X \right )$: Probabilidad a posteriori.
- $P\left ( X \mid C \right )$: Función de probabilidad condicional.

Expandiendo para la variable $X$:

$$P\left ( C \mid X \right ) = \frac{P\left ( X_1,X_2, \cdots ,X_n \mid C \right )P\left ( C \right )}{P\left ( X_1, X_2, \cdots, X_n \right )}$$

También se usa la regla de Bayes para su complemento $\bar{C}$:

$$P\left ( \bar{C} \mid X \right ) = \frac{P\left ( X_1,X_2, \cdots ,X_n \mid \bar{C} \right )P\left ( \bar{C} \right )}{P\left ( X_1, X_2, \cdots, X_n \right )} $$

Se relacionan las dos ecuaciones para $C$ y para $\bar{C}$, asumiendo de que cada $X_i$ es independiente:

$$\frac{P\left ( C \mid X \right )}{P\left ( \bar{C} \mid X \right )} = \frac{\frac{P\left ( X \mid C \right )P\left ( C \right )}{P\left ( X \right )}}{\frac{P\left ( X \mid \bar{C} \right )P\left ( \bar{C} \right )}{P\left ( X \right )}} $$

También se tiene lo siguiente:

$$P\left ( X \mid C \right ) = \prod_{1}^{n} P\left ( X \mid C \right )$$

$${S}'\left ( X \right ) = ln\frac{P\left ( C \mid X \right )}{P\left ( \bar{C} \mid X \right )}$$

$${S}'\left ( X \right ) = ln\frac{\prod_{1}^{n}P\left ( C \mid X_i \right )}{\prod_{1}^{n}P\left ( \bar{C} \mid X_i \right )} + ln\frac{P\left ( C \right )}{P\left ( \bar{C} \right )}$$

Aplicando la igualdad de los logaritmos tenemos que $S(X)$:

$${S}'\left ( X \right ) = \sum_{1}^{n} ln\frac{P\left ( C \mid X_i \right )}{P\left ( \bar{C} \mid X_i \right )}$$

Donde:

$$S\left ( X \right ) =  ln\frac{P\left ( C \mid X_i \right )}{P\left ( \bar{C} \mid X_i \right )} = ln\frac{\frac{N_{cx_i}}{N_c}}{\frac{N_{\bar{c}x_i}}{N_{\bar{c}}}}$$

Un valor alto en $S$ indica una alta probabilidad de pertenecer a la clase $C$

## Suavizado de Laplace

El suavizado de laplace evita errores de desbordamiento  provocados por una división entre cero que puede ser expresado con la siguiente ecuación:

$$P\left ( X_i \mid C \right ) = \frac{N_{cx_i} + 1}{N_c + k}$$

Donde $k$ es el total de clases a las que se puede pertenecer (para esta caso solo existen 2).

## Score Classifier

Ya con un score $S$ obtenido para cada característica $X$, lo que resta es seleccionar, en función de criterios arbitrarios, los variables que serán tomados en cuenta para la clasificación para nuevos elementos utilizando el modelo ajustado. 

$$S\left ( C \mid X \right ) = \sum_{i=1}^{N} ln\left [ \frac{P \left ( X_i \mid C \right )}{P \left ( X_i \mid \bar{C} \right )} \right ] = \sum_{i=1}^{N} ln\frac{\frac{N_{cx_i}}{N_c}}{\frac{N_{\bar{c}x_i}}{N_{\bar{c}}}}$$