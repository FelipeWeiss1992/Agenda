import calendar
import datetime

data = datetime.datetime.now()

print(f"Imprime o ano {data.year}")
print(f"Imprime a mês {data.month}")
print(f"Imprime o dia {data.day}")

# Exemplo 1: Exibir o calendário de determinado mês.

#resultado_mes = calendar.month(data.year, data.month)
#print(resultado_mes)


# Exemplo 2: Exibir o calendário de um determinado ano.
    
#print ("O calendário do ano 2022 é:")  
#print (calendar.calendar(2022, 2, 1, 6))


# Exemplo 3: Exibir o calendário de determinado mês em formato HTML. 

tc = calendar.HTMLCalendar(firstweekday = 6)
print(tc.formatmonth(data.year, data.month))


# Exemplo 4: 
cal = calendar.Calendar(firstweekday=6)
print(f"Aqui a variavel cal {cal}")
dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
print(f"Aqui dias da semana {dias_da_semana}")
calDays = cal.monthdayscalendar(data.year, data.month)
print(f"Aqui a variavel calDays {calDays}")


"""
class calendar.Calendar:

classe Calendar cria um objeto Calendar. Um objeto Calendar fornece
vários métodos que podem ser usados para preparar os dados do
calendário para formatação. Esta classe não faz nenhuma formatação.
Esse é o trabalho das subclasses. A classe do calendário permite os
cálculos para várias tarefas com base na data, mês e ano. A classe
Calendar fornece os seguintes métodos:


FUNÇÃO	                DESCRIÇÃO
iterweekdays()	        Retorna um iterador para os números dos
                        dias da semana que serão usados por uma semana
    
itermonthdates()        Retorna um iterador para o mês (1-12) no ano

itermonthdays()         Retorna um iterador de um mês e um ano especificados

itermonthdays2()        O método é usado para obter um iterador para o mês
                        do ano semelhante a itermonthdates(). Os dias
                        retornados serão tuplas compostas por um número do
                        dia do mês e um número do dia da semana.

itermonthdays3()        Retorna um iterador para o mês do ano semelhante a
                        itermonthdates(), mas não restrito pelo intervalo
                        datetime.date. Os dias devolvidos serão tuplas
                        compostas por um ano, um mês e um dia do mês.

itermonthdays4()        Retorna um iterador para o mês do ano semelhante a
                        itermonthdates(), mas não restrito pelo intervalo
                        datetime.date. Os dias devolvidos serão tuplas 
                        compostas por um ano, um mês, um dia do mês e um
                        dia da semana.

monthdatescalendar()	Costumava obter uma lista das semanas no mês do 
                        ano como semanas inteiras

monthdays2calendar()	Costumava obter uma lista das semanas no mês do
                        ano como semanas inteiras
                        
calendário do dia       Costumava obter uma lista das semanas no mês do ano
do mês                  como semanas inteiras

yeardatescalendar()     Costumava obter uma lista das semanas no mês do ano
                        como semanas inteiras
yeardays2calendar() 	Usado para obter os dados do ano especificado. As
                        entradas nas listas da semana são tuplas de números
                        de dias e números de dias da semana

calendário do dia   	Usado para obter os dados do ano especificado. As
do ano()                entradas nas listas da semana são números dos dias

 
class calendar.TextCalendar:

A classe TextCalendar pode ser usada para gerar calendários de texto
simples. A classe TextCalendar em Python permite que você edite o
calendário e use conforme sua necessidade.


FUNÇÃO                  DESCRIÇÃO
formatmonth()	        O método é usado para obter o calendário do mês em uma
                        string multilinha

prmonth()               O método é usado para imprimir o calendário de um mês
                        conforme retornado por formatmonth()

formatyear()            O método é usado para obter o calendário de m colunas
                        para um ano inteiro como uma string de várias linhas

pryear()                O método é usado para imprimir o calendário de um ano
                        inteiro conforme retornado por formatmonth()

 
class calendar.HTMLCalendar:

A classe HTMLCalendar pode ser usada para gerar calendários HTML. A classe
HTMLCalendar em Python permite que você edite o calendário e use de acordo
com suas necessidades.


FUNÇÃO	                DESCRIÇÃO
formatmonth()           O método é usado para obter o calendário do mês como uma
                        tabela HTML

formatyear()            O método é usado para obter o calendário do ano como uma
                        tabela HTML.

formatyearpage()        O método é usado para obter o calendário do ano como uma
                        página HTML completa

 
Simple TextCalendar class:

Para calendários de texto simples, o módulo de calendário fornece as seguintes
funções:


FUNÇÃO	                DESCRIÇÃO
setfirstweekday()       A função define o número de início do dia da semana

primeiro dia da semana()    A função retorna o primeiro número do dia da semana.
                            Por padrão 0 (segunda-feira)

isleap()                A função verifica se o ano mencionado no argumento é
                        bissexto ou não

dias bissextos()        A função retorna o número de dias bissextos entre os
                        anos especificados em argumentos

dia da semana()         A função retorna o número do dia da semana (0 é segunda-feira)
                        da data especificada em seus argumentos

cabeçalho da semana()   Retorna um cabeçalho contendo nomes abreviados dos dias da semana

intervalo de meses()    A função retorna dois inteiros, primeiro, o número do dia
                        inicial da semana (0 como segunda-feira), segundo, o número
                        de dias no mês

monthcalendar()         Retorna uma matriz que representa o calendário de um mês.
                        Cada linha representa uma semana; dias fora do mês são
                        representados por zeros

prmonth()               A função também imprime o mês do ano específico, mas não há
                        necessidade de operação de "impressão" para executar isso

mês()                   A função imprime o mês de um ano específico mencionado em
                        argumentos

prcal()                 A função também imprime o calendário do ano específico, mas
                        não há necessidade de operação de "impressão" para executar isso

calendário()            Função exibe o ano, largura de caracteres, não. de linhas por
                        semana e separações de coluna.
"""