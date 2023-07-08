# Chiffrement RSA

Ce projet consiste à implémenter le chiffrement RSA, un algorithme de cryptographie à clé publique, en utilisant le langage de programmation Python. Le chiffrement RSA est largement utilisé pour sécuriser les données sensibles, notamment dans les communications sur Internet.

## Fonctions implémentées

- `is_prime(n)`: Cette fonction vérifie si un nombre `n` est premier. Elle utilise une approche de vérification de primalité simple et efficace.

- `gcd(a, b)`: Cette fonction calcule le plus grand commun diviseur (PGCD) de deux nombres `a` et `b` en utilisant l'algorithme d'Euclide.

- `multiplicative_inverse(e, phi)`: Cette fonction calcule l'inverse multiplicatif de `e` modulo `phi`. C'est une étape essentielle dans la génération de la clé privée dans RSA.

- `generate_keypair(p, q)`: Cette fonction génère une paire de clés RSA à partir de deux nombres premiers `p` et `q`. Elle vérifie d'abord si `p` et `q` sont premiers et distincts, puis elle calcule les clés publique et privée.

- `encrypt(message, public_key)`: Cette fonction chiffre un message en utilisant la clé publique. Elle convertit chaque caractère du message en son code ASCII, le met à la puissance `e` et prend le reste de la division par `n`.

- `decrypt(cipher, private_key)`: Cette fonction déchiffre un message chiffré en utilisant la clé privée. Elle prend chaque nombre du message chiffré, le met à la puissance `d` et prend le reste de la division par `n`, puis convertit le résultat en caractère.

Cette application Streamlit utilise des fonctionnalités pour permettre à l'utilisateur de générer une paire de clés RSA à partir de deux nombres premiers modifiables (par défaut : 11 et 23). Ensuite, l'utilisateur peut chiffrer un message avec la clé publique et le déchiffrer avec la clé privée. Le message chiffré est affiché à l'utilisateur sous la forme d'une liste de nombres [Nombre,Nombre,….]. 

Notre application fournie est une implémentation efficace et conviviale du chiffrement RSA. Elle illustre bien comment le chiffrement RSA fonctionne et comment il peut être utilisé pour sécuriser les communications. Cependant, il est important de noter que dans un contexte réel, des mesures de sécurité supplémentaires seraient nécessaires pour protéger les clés et les données sensibles.

## ScreenShots

![image1](screenshots/screencapture-chiffrementrsa-streamlit-app-1.png)

![image1](screenshots/screencapture-chiffrementrsa-streamlit-app-2.png)

![image1](screenshots/screencapture-chiffrementrsa-streamlit-app-3.png)

![image1](screenshots/screencapture-chiffrementrsa-streamlit-app-4.png)
