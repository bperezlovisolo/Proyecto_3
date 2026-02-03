import pandas as pd

def informe(x):
    print("Información del DataFrame:")
    print(x.info())
    print("Descripción estadística:")
    print(x.describe())
    print("Valores nulos:")
    print(x.isnull().sum())
    print("Tipos de datos:")
    print(x.dtypes)
    
    print("Primeras 5 filas:")
    print(x.head())
    print("Últimas 5 filas:")
    print(x.tail())
    print("Forma del DataFrame:")
    print(x.shape)
    print("columnas")
    print(x.columns)
    print("numericos")
    print(x.select_dtypes(include=["number"]).columns)

def datos(x):
    print("datos nulos")
    print(x.isnull().sum())
    print("datos totales")
    print(x.count())   
    print("porcentaje de nulos")
    print(x.isnull().sum() / x.shape[0]*100)
    print("datos duplicados")
    print(x.duplicated().sum())
    print(x.duplicated().any())

def drop_columns (df, columns):
    df.drop(columns, axis=1, inplace=True)


def union_df (df1,df2):
    df_union = pd.merge(df1,df2,on=["nationality"],how='left')
    return df_union

def limpiar_nulos(x):
    df = x.copy()
    df = x.dropna()
    return df

def clean_column(df, column_name, english_club):
    df_clean = df.copy()
    df_clean = df_clean[df_clean[column_name].isin(english_club)]
    print(f"Valores únicos en '{column_name}':", 
          df_clean[column_name].unique())
    return df_clean

def porcentajes(x, y):
    return round(((x / y)*100),2)