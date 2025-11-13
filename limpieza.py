def reemplazar_por_media(df, columna):
    df_reempl=df.copy()
    df_reempl['AvgBill'] =df_reempl['AvgBill'].mean()

    return df_reempl