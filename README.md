# Tutoria de Python para Análise de Dados - BRISA

## Descrição

Repositório destinado a ser um tutorial de Python para do projeto BRISA. O leitor será introduzido a linguagem e bibliotecas relevantes a análise de dados (Pandas, Numpy e MatPlotlib), além de tecnologias que aumentarão a eficiência na criação de um projeto.

## Introdução Python

- ### Descrição

Python é uma linguagem de programação de alto nível, dinâmica, interpretada, modular, multiplataforma e que suporta uma arquitetura orientada a objetos.

Por ser uma linguagem de sintaxe relativamente simples e de fácil compreensão, ganhou popularidade entre profissionais da indústria tecnológica que não são especificamente programadores, como engenheiros, matemáticos, cientistas de dados, pesquisadores e outros. 

Python é uma linguagem poderosa, possui uma grande comunidade e uma vasta quantidade de bibliotecas, o que faz com que essa seja uma linguagem muito versátil e de fácil aprendizado devido ao grande número de documentações. A seguir estão algumas dass principais áreas onde o Python é utilizado:

<br>

1 - Scripting e automação: Algumas das bibliotecas para essa área são [Pywin32](https://wiki.python.org.br/PyWin32) e [Selenium](https://www.selenium.dev/pt-br/documentation/)

2 - Desenvolvimento web: A linguagem possui uma extensa variedade de frameworks para todos os tipos de gosto, entre eles os famosos [Django](https://docs.djangoproject.com/pt-br/4.2/), [Flask](https://flask.palletsprojects.com/en/2.3.x/) e [FastAPI](https://pythonacademy.com.br/blog/como-usar-o-fastapi-para-construir-apis-no-python#:~:text=O%20FastAPI%20%C3%A9%20uma%20biblioteca%20Python%20que%20permite,APIs%20seguras%2C%20documentadas%20e%20test%C3%A1veis%20de%20maneira%20eficiente.).
    
3 - Enquadramento de testes: Isso justifica por que desenvolvedores de software em Python adoram utilizar TDD (Test Driven Development). Para mais informações sobre essa técnica, acesse [TDD](https://kenzie.com.br/blog/o-que-e-tdd/)
    
4 - Big Data: Para essa área o Python tem como a principal biblioteca o [Pandas](https://pandas.pydata.org/docs/)
    
5 - Ciência de dados: Nesse tutorial iremos focar nessa área, onde vamos conhecer as bibliotecas [Pandas](https://pandas.pydata.org/docs/), [NumPy](https://numpy.org/doc/stable/) e [MatPlot](https://matplotlib.org/stable/index.html)
    
6 - Computação gráfica: Pacotes de soluções para esta área, como [PyOpenGL](https://pyopengl.sourceforge.net/documentation/) e [PyGame](https://www.pygame.org/docs/)
    
7 - Inteligência artificial: Entre as bibliotecas mais comuns voltadas ao aprendizado de máquina estão o [TensorFlow](https://www.tensorflow.org/about/bib?hl=pt-br), [PyThorch](https://pytorch.org/docs/stable/index.html), [Theano](https://theano.readthedocs.io/en/0.8.x/), [Keras](https://keras.io/getting_started/).

</br>

- ### Vantagens

    - É fácil de aprender

    - É portátil e multiplataforma

    - É open source e gratuito

    - Oferece múltiplas possibilidades de desenvolvimento

    - É uma linguagem “curinga”

</br>

- ### Desvantagens

    - Aplicações que lidam diretamente com o hardware

    - Aplicações onde o hardware não é escalável
    
    - Aplicações de missões críticas que processam dados em tempo real
    
    - Aplicações nativas com interfaces gráficas
    
    - Aplicações com vida útil muito longa  

</br>

- ### Instalação

     - **Linux**

        - Red Hat, CentOS, or Fedora
            ```
            dnf install python3 python3-devel
            ```

        - Debian or Ubuntu
            ```
            apt-get install python3 python3-dev
            ```
        
        - Gentoo
            ```
            emerge dev-lang/python
            ```

        - Arch Linux
            ```
            pacman -S python3
            ```

     - **Windows**

    Para fazer o Download do Python para Windows acesse o site [Python Download](https://www.python.org/downloads/)

<br>

## Introdução Venv

- ### Descrição 

O **virtualenv(Venv)** no Python é utilizado para isolar a versão do Python e das bibliotecas usadas em um determinado sistema.

Caso você não utilize o Venv, todas as bibliotecas necessárias para seu sistema seriam instaladas no ambiente do sistema operacional.

<br>

- ### Cenário

Você foi contratado para desenvolver um sistema de análise de dados pela empresa A e para isso você utilizará o Python 3.7.4 e as bibliotecas pandas e numpy.

Esta mesma empresa te contrata para montar um sistema de cadastro e você opta por utilizar o mesmo Python 3.7.4, porém, como você irá disponibilizar este sistema na intranet deles, você usa o Flask, psycopg2 (para acesso ao PostgreSQL) e o marshmallow.

Você tem o hobby de criar jogos e resolve estudar o pygame, porém, a versão do Python escolhida é o 3.8.1

Um amigo pediu para você fazer um web scrapping e você resolve testar o Python 3.9. Além disso, você irá utilizar as bibliotecas requests e bs4 (BeautifulSoup)

<br>

- ### Solução

Caso você não utilize Venv **para cada projeto**, você teria que utilizar o Python instalado no seu sistema e teria que colocar todas as bibliotecas nele. Isso causaria um problema de gerenciamento das bibliotecas.

<br>

- ### Problema

A passagem "para cada projeto" foi grifada, pois caso você utilize um Venv para todos os projetos, você resolve apenas o isolamento do ambiente frente ao Python do sistema operacional, **porém não resolve o gerenciamento das bibliotecas usadas e nem teria a possibilidade de usar versões de Python diferentes.**

<br>

- ### Vantagem

Caso você use a mesma biblioteca em dois projetos diferentes e necessite fazer o upgrade dela em um dos projetos, isso é possível com Venv. O mesmo caso, sem Venv, seria arriscado, pois você poderia "quebrar" o sistema que não necessita da atualização.

(Fonte: MARQUES, Paulo. 2020) [2]

<br>

- ### Importante

Para mais informações de como criar, gerenciar e como funcionam os Venv no Python, acesse a [Documentação do Venv](https://docs.python.org/pt-br/3/library/venv.html).

**Dica:** Utilizem ou aprendam a utilizar um Venv, pois a maioria dos projetos em Python fazem uso dessa tecnologia, além disso ao utilizar Venv vocês diminiuem a possibilidade de inconsistência de versões de linguagem e de bibliotecas.

<br>

## Introdução Pandas



<br>

## Introdução NumPy

<br>

## Introdução MatPlotlib

<br>

## Referências Bibliográficas

[1] Kenzie Academy Brasil, ["O que é Python ?"](https://kenzie.com.br/blog/o-que-e-python/). Acesso em 18/05/2023

[2] Stack Overflow, ["Para que serve o Venv no Python ?](https://pt.stackoverflow.com/questions/482743/para-que-serve-o-virtualenv-no-python#:~:text=O%20virtualenv%20do%20Python%20%C3%A9%20utilizado%20para%20isolar,sistema%20seriam%20instaladas%20no%20ambiente%20do%20sistema%20operacional.). Acesso em 22/05/2023

[3] 

## Metas 

- Todo repositório deve ser pensado para o sistema Linux
- Linkar toda documentação e referênciar tudo que possível
- Dar exemplo de tudo, talvez usando o jupiter notebook
- Percorrer o básico de python, pandas, numpy e análise de dados (DataFrames), além de um tutorial básico de plotar gráficos
- Lembrar de não recriar a roda
- Deixar tudo bem didático
- Exercícios simples, com tabelas dadas por mim 
- Instroduzir os conseitos e fazer algo bem teórico
- Equilibrar carga prática e teórica
- Colocar um código de conduta e um de contribuição
- Templates de issue e pull request