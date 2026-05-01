[app]
# (Obligatoire) Titre de ton application
title = Secure Node

# (Obligatoire) Nom du package
package.name = securenode

# (Obligatoire) Domaine du package
package.domain = org.eni

# (Obligatoire) Où se trouve le code source (le point indique le dossier courant)
source.dir = .

# (Obligatoire) Version de l'application
version = 0.1

# Fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas

# Dépendances (Inclus cryptography et paho-mqtt comme vu dans ton code)
requirements = python3,kivy,cryptography,paho-mqtt

# Orientation de l'écran
orientation = portrait

# Permissions Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Réglage pour le clavier
android.window_softinput_mode = resize

# (Optionnel) Icône de l'application
# icon.filename = %(source.dir)s/icon.png

[buildozer]
# Niveau de log (2 pour plus de détails)
log_level = 2