from sklearn.preprocessing import LabelEncoder


def encode_data(data, user_column, item_column, rating_column):
    user_enc = LabelEncoder()
    data['user'] = user_enc.fit_transform(data[user_column].values)

    item_enc = LabelEncoder()
    data['movie'] = item_enc.fit_transform(data[item_column].values)

    data[rating_column] = data[rating_column].values.astype(float)

    return data, user_enc, item_enc
