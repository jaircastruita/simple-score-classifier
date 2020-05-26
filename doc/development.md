## Terms definition

<img src="https://render.githubusercontent.com/render/math?math=N"> represents the population sample. Para la muestra es de interés notar aquellas observaciones <img src="https://render.githubusercontent.com/render/math?math=n"> represents observations where the class <img src="https://render.githubusercontent.com/render/math?math=C"> is positive. <img src="https://render.githubusercontent.com/render/math?math=X"> represents our categorical feature vector and <img src="https://render.githubusercontent.com/render/math?math=N_x"> are counts for samples containing each different values:


<img src="https://render.githubusercontent.com/render/math?math=\left ( N \bigcap X \right )">

We define <img src="https://render.githubusercontent.com/render/math?math=C"> as the present class  and <img src="https://render.githubusercontent.com/render/math?math=N_c"> as the total number of positive class observations:

<img src="https://render.githubusercontent.com/render/math?math=\left ( N \bigcap C \right )">

<img src="https://render.githubusercontent.com/render/math?math=N_{cx}"> are the counts where <img src="https://render.githubusercontent.com/render/math?math=C"> and a possible value <img src="https://render.githubusercontent.com/render/math?math=X"> can contain are present as in the following interception:

<img src="https://render.githubusercontent.com/render/math?math=\left ( N \bigcap C \bigcap X \right )">

<img src="https://render.githubusercontent.com/render/math?math=P(C)"> Is the probability for one observation to belong to class <img src="https://render.githubusercontent.com/render/math?math=C"> if it selected randomly from the sample:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \right ) = \frac{N_c}{N}">

The probability of selecting some observation with a particular value of <img src="https://render.githubusercontent.com/render/math?math=X"> from the sample <img src="https://render.githubusercontent.com/render/math?math=P(X)"> can be defined as the following:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( X \right ) = \frac{N_x}{N}">

The conditional probability of <img src="https://render.githubusercontent.com/render/math?math=X"> given <img src="https://render.githubusercontent.com/render/math?math=C">, (<img src="https://render.githubusercontent.com/render/math?math=P(C|X)">) can be obtained by:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right ) = \frac{N_{cx}}{N_x}">

## Naive Bayes

Naive Bayes method assumes <img src="https://render.githubusercontent.com/render/math?math=K"> subpopulations <img src="https://render.githubusercontent.com/render/math?math=S_1, S_2, \dots, S_k"> are mutually exclusive with probabilities <img src="https://render.githubusercontent.com/render/math?math=P(S_1), P(S_2), \dots, P(S_k)">. If event <img src="https://render.githubusercontent.com/render/math?math=A"> ocurs the posterior probability <img src="https://render.githubusercontent.com/render/math?math=S_i"> given <img src="https://render.githubusercontent.com/render/math?math=A"> can be obtained by:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( S_i \mid A \right ) = \frac{P\left ( S_i \right )P\left ( A \mid S_i \right )}{\sum_{j=i}^{K}P\left ( S_j \right )P\left ( A \mid S_j \right )}">

## Score

How to calculate a score for class <img src="https://render.githubusercontent.com/render/math?math=C"> for a given observation?

The Score measure <img src="https://render.githubusercontent.com/render/math?math=S"> is a confidence measure for variable <img src="https://render.githubusercontent.com/render/math?math=X_i"> To determine if class <img src="https://render.githubusercontent.com/render/math?math=C"> is present. Using the Naive Bayes equation:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right ) = \frac{P\left ( X \mid C \right )P\left ( C \right )}{P\left ( X \right )}">

Where:
- <img src="https://render.githubusercontent.com/render/math?math=P\left (  C \right )">:  prior probability.
- <img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right )">: posterior probability.
- <img src="https://render.githubusercontent.com/render/math?math=P\left ( X \mid C \right )">: likelihood.

Expanding with respect <img src="https://render.githubusercontent.com/render/math?math=X">:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( C \mid X \right ) = \frac{P\left ( X_1,X_2, \cdots ,X_n \mid C \right )P\left ( C \right )}{P\left ( X_1, X_2, \cdots, X_n \right )}">

Doing the same for the complement class <img src="https://render.githubusercontent.com/render/math?math=\bar{C}">:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( \bar{C} \mid X \right ) = \frac{P\left ( X_1,X_2, \cdots ,X_n \mid \bar{C} \right )P\left ( \bar{C} \right )}{P\left ( X_1, X_2, \cdots, X_n \right )}">

Using both equations <img src="https://render.githubusercontent.com/render/math?math=C"> and <img src="https://render.githubusercontent.com/render/math?math=\bar{C}"> to make a rate, assuming <img src="https://render.githubusercontent.com/render/math?math=X_i"> is independent:

<img src="https://render.githubusercontent.com/render/math?math=\frac{P\left ( C \mid X \right )}{P\left ( \bar{C} \mid X \right )} = \frac{\frac{P\left ( X \mid C \right )P\left ( C \right )}{P\left ( X \right )}}{\frac{P\left ( X \mid \bar{C} \right )P\left ( \bar{C} \right )}{P\left ( X \right )}}">

Also:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( X \mid C \right ) = \prod_{1}^{n} P\left ( X \mid C \right )">

<img src="https://render.githubusercontent.com/render/math?math={S}'\left ( X \right ) = ln\frac{P\left ( C \mid X \right )}{P\left ( \bar{C} \mid X \right )}">

<img src="https://render.githubusercontent.com/render/math?math={S}'\left ( X \right ) = ln\frac{\prod_{1}^{n}P\left ( C \mid X_i \right )}{\prod_{1}^{n}P\left ( \bar{C} \mid X_i \right )} + ln\frac{P\left ( C \right )}{P\left ( \bar{C} \right )}">

We can apply the logarithm on this equation to get <img src="https://render.githubusercontent.com/render/math?math=S(X)">:

<img src="https://render.githubusercontent.com/render/math?math={S}'\left ( X \right ) = \sum_{1}^{n} ln\frac{P\left ( C \mid X_i \right )}{P\left ( \bar{C} \mid X_i \right )}">

Where:

<img src="https://render.githubusercontent.com/render/math?math=S\left ( X \right ) =  ln\frac{P\left ( C \mid X_i \right )}{P\left ( \bar{C} \mid X_i \right )} = ln\frac{\frac{N_{cx_i}}{N_c}}{\frac{N_{\bar{c}x_i}}{N_{\bar{c}}}}">

A positive high <img src="https://render.githubusercontent.com/render/math?math=S"> value indicates high confidences that the observations belongs to class <img src="https://render.githubusercontent.com/render/math?math=C">

## Laplace smooth

We can apply Laplace smooth to precent zero-division errors:

<img src="https://render.githubusercontent.com/render/math?math=P\left ( X_i \mid C \right ) = \frac{N_{cx_i} + 1}{N_c + k}">

Where <img src="https://render.githubusercontent.com/render/math?math=k"> is equal to 2.

## Score Classifier

Finally, with score <img src="https://render.githubusercontent.com/render/math?math=S"> for each different feature <img src="https://render.githubusercontent.com/render/math?math=X">, a summation of every Score is obtained: 

<img src="https://render.githubusercontent.com/render/math?math=S\left ( C \mid X \right ) = \sum_{i=1}^{N} ln\left [ \frac{P \left ( X_i \mid C \right )}{P \left ( X_i \mid \bar{C} \right )} \right ] = \sum_{i=1}^{N} ln\frac{\frac{N_{cx_i}}{N_c}}{\frac{N_{\bar{c}x_i}}{N_{\bar{c}}}}">