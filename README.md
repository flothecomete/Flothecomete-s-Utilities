# msg_to_txt

## Description
`msg_to_txt` est un utilitaire de ligne de commande permettant de convertir des fichiers Outlook .msg en fichiers texte (.txt). Cet outil est particulièrement utile pour ceux qui ont besoin d'extraire et de lire le contenu des fichiers .msg sans utiliser Outlook.

## Installation
Clonez le dépôt GitHub et installez les dépendances nécessaires :

```bash
git clone https://github.com/flothecomete/Flothecomete-s-Utilities
cd Flothecomete-s-Utilities
```

## Utilisation

### Syntaxe
```bash
msg_to_txt [OPTIONS] ARGUMENTS
```

### Options
- `-h` : Affiche ce manuel d'utilisation.
- `-f` : Mode fichier. Permet de convertir un seul fichier .msg.
- `-d` : Mode répertoire. Convertit tous les fichiers .msg du répertoire spécifié.

### Arguments
- `PATH` : Chemin du fichier ou du répertoire à convertir.

### Exemples
- Pour convertir un fichier spécifique :
  ```bash
  msg_to_txt -f mail.msg
  ```
- Pour convertir tous les fichiers dans un répertoire :
  ```bash
  msg_to_txt -d path/to/folder
  ```

## Auteur
Écrit par Flothecomete.

## Signalement des bugs
Veuillez signaler les bugs à l'adresse suivante : <https://github.com/flothecomete/Flothecomete-s-Utilities>.

## Licence
`msg_to_txt` est distribué sous la licence GPLv3+ :
- Copyright © 2024 Flothecomete.
- Licence GPLv3+ : GNU GPL version 3 ou ultérieure <https://gnu.org/licenses/gpl.html>.

Ceci est un logiciel libre : vous êtes libre de le modifier et de le redistribuer. Il n'y a AUCUNE GARANTIE, dans la mesure permise par la loi.
