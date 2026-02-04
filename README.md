## PROYECTO 3

### Titulo

Análisis del talento sudamericano en el fútbol de Inglaterra. 

## Objetivo del proyecto

Analizar si el futbol inglés concentra una cantidad relevante de jugadores de selecciones que se ubican dentro del Top 20 del Ranking  y en particular cual es la participación de los jugadores de selecciones CONMEBOL. 
El objetivo de este proyecto es poder verificar si hay una conecentración de talento y a su vez constatar si el jugador sudamericano tiene presencia en esta liga. 

## Contexto del negocio
Este proyecto se plantea como una consultora especializada en scouting y analisis deportivo, la cual fue contrada por Oller Group (empresa especializada en representación de jugadores) para obtener información del mercado Inglés. La empresa nos ha solicitado un análisis puntual sobre la liga inglesa a través del cual se pueda catalogar su nivel y a su vez la presencia de jugadores sudamericanos en ella. 
Con ello se busca identificar si el futbol ingles es hoy en dia el que mayor talento colectivo tiene y además, verificar la incidencia de los futbolistas sudamericanos con el objetivo de proponer estrategias de scouting, fichajes y verificar si están desarrollados de tal forma que puedan ser transferidos directamente a un equipo de esta liga.

## Dataset

Los datasets utilizados recogen registros de los futbolistas de todo el mundo y el ranking FIFA de selecciones. 
Tomados de la página web "www.kaggle.com" y descargamos el ranking a traves de una API ubicada en "www.rapidapi.com" llamada "World Football Ranking"

Contiene información sobre:

- Jugadores (csv): nombre del jugador, país/selección del jugador, club actual del jugador, entre otras.
- Raking FIFA (API): posición del ranking, nombre de la selección, puntos FIFA, confederación a la que pertenece(CONMEBOL, UEFA, etc.)

Las variables principales utilizadas en el análisis son:

- full_name (jugadores), nationality (jugadores), club_name (jugadores), rank (FIFA), name (FIFA), points (FIFA) y confederation (FIFA) 

## Notas sobre la calidad del dato

- La unión entre datasets depende de la columna de nombres de país (`Nationality` vs `name`).  
- Algunos jugadores de la liga inglesa quedaron con valores nulos en la columna ranking dado que la selección a la que representan no esta dentro del ranking FIFA o bien porque los nombres de los países estaban mal escritos (Ej: IR Iran e Iran).
- Para el análisis Top 20 se excluyeron aquellas filas sin ranking para evitar sesgos.

## Preguntas clave / Hipótesis

- ¿Qué proporción de jugadores del futbol inglés pertenece a selecciones Top 20 del Ranking FIFA?  
- Dentro de los jugadores Top 20 en Premier League, ¿qué confederaciones están más representadas (UEFA vs CONMEBOL, etc.)?  
- Teniendo en cuenta la presencia de jugadores de selecciones CONMEBOL en el futbol inglés, ¿es un mercado cerrado dado el nivel de competición?  
- Dentro del top 10 del ranking FIFA solo estan Argentina y Brasil por lo que el scouting principal hay que hacerlo en estas dos ligas. 


## Proceso de análisis

El análisis incluye:
- Exploración inicial del dataset (EDA).
- Limpieza y estandarización de variables.
- Integración entre las bases de datos a traves de un merge teniendo en cuenta la columna Nationality.
- Filtrado principal sobre los jugadores que están en el futbol ingles y luego un filtrado de aquellos jugadores cuyas selecciones están dentro del top 20 del ranking FIFA.
- Análisis descriptivo y comparativo mediante tablas y gráficos.

## Resultados / Insights

- El 68,57% de los jugadores de la Premier League pertenece a selecciones Top 20 del Ranking FIFA.  
- Dentro del subconjunto Top 20:
  - UEFA: 92,47%  
  - CONMEBOL: 5,51%  
  - Otras: 2,02%
- Los países CONMEBOL con mayor presencia son Brasil y Argentina, 31 y 8 respectivamente por lo que habría que trabajar en primera instancia en estos dos mercados.  


## Recomendaciones de negocios

- Priorizar mercados con mayor representación Top 20 para maximizar la probabilidad de poder ingresar a esta liga.  
- Analizando la cantidad de jugarodes CONMEBOL en esta liga y compararlos con la liga española, alemana y portuguesa para estudiar y proyectar la viabilidad de una arribo directo al futbol ingles o bien hacer un paso previo. 

## Limitaciones

- Posibles errores de match por nombres diferentes de países/nacionalidades.  
- El dataset de jugadores puede estar desfasado respecto a transferencias recientes (jugadores cambian de club).  
- No se mide “mejor liga” de forma integral, faltan variables como competitividad interna, ingresos, rendimiento internacional de clubes, en otras cuestiones.

## Próximos pasos

- Comparar la presencia de selecciones Top 20 entre Premier League y otras ligas europeas.    
- Analizar variables de rendimiento de clubes (puntos, títulos, cantidad de Champions League/Europa League) para medir “mejor liga” con criterios deportivos y económicos.  
- Analizar donde hay mayor concentración de talento por posiciones (defensas/mediocampistas/delanteros) para luego scoutear aquellos jugadores cuya posición no está concentrada.


## Cómo replicar el proyecto
1. Clonar el repositorio.
2. Instalar las librerías necesarias ( pandas, numpy, mysql).
3. Ejecutar el cuaderno a través de github.