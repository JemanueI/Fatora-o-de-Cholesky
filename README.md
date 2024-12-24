# Fatoração de Cholesky

## O que é?
A fatoração de Cholesky é uma das técnicas matématicas abordadas nas turmas de Cálculo Númerico em cursos nas áreas de Engenharias e Ciências Exatas e da Terra. Essa fatoração é útil quando se necessita de soluções númericas ou até mesmo em algoritmos de otimização, sendo bastante utilizada em problemas de Álgebra Linear, Estatística e Aprendizado de Máquina.

## Qual o objetivo?
A fatoração de Cholesky tem por objetivo decompor uma matriz simétrica e definida positiva em duas matrizes triangulares, sendo expressa da seguinte forma:
<p align="center">
  $$ A = L * L^T $$
</p>
<p>
Onde:
  
- $A$ é a matriz simétrica e definida positiva;
- $L$ é uma matriz triangular inferior;
- $L^t$ é a transposta de L, portando sendo a matriz triangular superior.
</p>

## Qual a finalidade?
Por fim, a fatoração de Cholesky aplica-se:
- Na resolução de sistemas lineares, onde se busca resolver sistemas de equações do tipo $Ax = b$ quando a matriz $A$ é simétrica e definida positiva.
- Em métodos númericos, como na regressão linear e em algoritmos de aprendizado de máquina, onde se busca a otimização. Exemplo: Método de Máxima Verossimilhança.
- Em simulações e amostragem, para gerar amostras de distrubuições multivariadas.

## Conclusão
A fatoração de Cholesky é uma téncica matématica eficiente e numericamente estável, sendo recomendável quando possível, se comparada a outras fatorações, principalmente quando há uso em sistemas computacionais, devido ao baixo custo computacional, e tendo uma maior precisão.

## Referências
- Aula 06 - Fatoração de Cholesky e Condicionamento de uma Matriz [https://www.ime.unicamp.br/~valle/Teaching/MS211/Aula06.pdf]
- RODRIGUES, Carlos R. de F. C. *Análise Numérica: Teoria e Prática*. 10ª ed.
