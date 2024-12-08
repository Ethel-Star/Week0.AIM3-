def clean_data(df, columns):
    # Fill missing values with median for numerical columns
    df[columns] = df[columns].fillna(df[columns].median())

    return df
