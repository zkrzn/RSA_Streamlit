import streamlit as st
import random

st.set_page_config(
    page_title="RSA Chiffrement",
    page_icon="random",
    initial_sidebar_state="collapsed"
)

def is_prime(n):
    """Vérifie si un nombre est premier"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    """Calcule le plus grand commun diviseur de a et b"""
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Calcule l'inverse multiplicatif de e modulo phi"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = extended_gcd(b % a, a)
            return g, y - (b // a) * x, x

    g, x, _ = extended_gcd(e, phi)
    if g == 1:
        return x % phi
    else:
        raise ValueError("L'inverse multiplicatif n'existe pas.")

def generate_keypair(p, q):
    """Génère la paire de clés RSA"""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p et q doivent être des nombres premiers.")
    elif p == q:
        raise ValueError("p et q ne peuvent pas être les mêmes.")

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    d = multiplicative_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(message, public_key):
    """Chiffre le message en utilisant la clé publique"""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    """Déchiffre le message chiffré en utilisant la clé privée"""
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return message

# Application Streamlit
st.title("Chiffrement RSA - FSR 2023")

# Obtention des paramètres de requête
query_params = st.experimental_get_query_params()
public_key_query = query_params.get("public_key", [None])[0]
private_key_query = query_params.get("private_key", [None])[0]

# Initialisation de public_key et private_key
public_key, private_key = None, None

# Vérifie si les paramètres de requête existent et les convertit en entiers
if public_key_query is not None and private_key_query is not None:
    try:
        public_key = tuple(map(int, public_key_query.split(",")))
        private_key = tuple(map(int, private_key_query.split(",")))
    except ValueError:
        pass


# Entrée des nombres premiers p et q
col1, col2 = st.columns(2)
with col1:
    p = st.number_input("__Saisir un nombre premier p:__", step = 1, value=11, min_value=0)
with col2:
    q = st.number_input("__Saisir un autre nombre premier q:__", step = 1, value=23, min_value=0)

# Génération des clés RSA
if st.button("__Générer les clés RSA__"):
    public_key, private_key = generate_keypair(int(p), int(q))
    public_key_query = ",".join(map(str, public_key))
    private_key_query = ",".join(map(str, private_key))
    st.experimental_set_query_params(public_key=public_key_query, private_key=private_key_query)
    st.success("__Vous avez généré des clés RSA.__")

st.write("---")

col3, col4 = st.columns(2)
# Entrée du message en clair
plaintext = col3.text_input("__Entrer le message à chiffrer:__")

# Chiffrement du message en clair
if col3.button("__Chiffrer__"):
    if public_key is not None:
        cipher = encrypt(plaintext, public_key)
        col3.success("__Message chiffré!__")
        col3.code(cipher)
    else:
        col3.warning("__Veuillez d'abord générer les clés RSA.__")

# Déchiffrement du message chiffré
ciphertext = col4.text_input("__Entrer le message à déchiffrer:__")
if col4.button("__Déchiffrer__"):
    if private_key is not None:
        if len(ciphertext) > 0:
            decrypted_message = decrypt(eval(ciphertext), private_key)
            col4.success("__Message déchiffré!__")
            col4.code(decrypted_message)
        else:
            col4.warning("__Veuillez entrer un texte chiffré valide.__")
    else:
        col4.warning("Veuillez d'abord générer les clés RSA.")

st.write("---")
st.markdown('**Z. IZ - A. NM**      -     :red[**MSID**]')
