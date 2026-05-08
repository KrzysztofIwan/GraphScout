def delete_polish_chars(text:str):
    polska_mapa = str.maketrans(
        "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
        "acelnoszzACELNOSZZ"
    )
    return text.translate(polska_mapa).strip().replace(" ", "_")