[app]

# (Obligatoire) Titre de ton application
title = Secure Node

# (Obligatoire) Nom du package
package.name = securenode

# (Obligatoire) Domaine du package
package.domain = org.eni

# (Obligatoire) Où se trouve le code source
source.dir = .

# (Obligatoire) Version de l'application
version = 0.1

# Fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas

# Dépendances corrigées :
# - kivy==2.3.0 pour la stabilité
# - openssl est requis pour compiler cryptography sur Android
requirements = python3,kivy==2.3.0,cryptography,paho-mqtt,openssl

# Orientation et permissions
orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# --- Configuration Android ---
# Autorise Buildozer à accepter les licences SDK automatiquement
android.accept_sdk_license = True

# Utilisation d'une version stable de l'API
android.api = 34
android.sdk_build_tools_revision = 34.0.0
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Architecture cible : arm64-v8a est le standard moderne (plus stable sur GitHub Actions)
android.archs = arm64-v8a

# Réglage pour le clavier Android
android.window_softinput_mode = resize

[buildozer]
# Niveau de log (2 pour voir les erreurs de compilation en détail)
log_level = 2
warn_on_root = 1