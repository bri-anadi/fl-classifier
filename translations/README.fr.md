# Classifieur de Fichiers

Un utilitaire Python multiplateforme puissant pour organiser automatiquement les fichiers et dossiers en fonction des extensions, des noms de dossiers ou des horodatages.

## Fonctionnalités

- **Méthodes de Classification Multiples** :
  - **Basée sur les Extensions** : Classe les fichiers dans des catégories selon leurs extensions
  - **Basée sur le Temps** : Organise les fichiers par date de création, modification ou accès
  - **Classification des Dossiers** : Catégorise les dossiers selon des modèles de nommage courants

- **Catégories de Fichiers** :
  - Documents (PDF, DOC, TXT, etc.)
  - Images (JPG, PNG, GIF, etc.)
  - Audio (MP3, WAV, FLAC, etc.)
  - Vidéos (MP4, AVI, MKV, etc.)
  - Archives (ZIP, RAR, 7Z, etc.)
  - Code (PY, JAVA, HTML, etc.)
  - Exécutables (EXE, MSI, APP, etc.)
  - Autres (pour les extensions non incluses dans les catégories ci-dessus)

- **Catégories de Dossiers** :
  - Projects : Pour les dossiers de développement et de projets
  - Backups : Pour le contenu de sauvegarde et d'archivage
  - Documents : Pour les dossiers de documents et de rapports
  - Media : Pour les dossiers de photos, vidéos, musique
  - Downloads : Pour les dossiers de téléchargement
  - Applications : Pour les logiciels et applications
  - Data : Pour les ensembles de données et bases de données
  - Web : Pour le contenu lié au web
  - Dated : Pour les dossiers avec des modèles de date (détectés automatiquement)
  - Versioned : Pour les dossiers avec des modèles de version (détectés automatiquement)
  - Uncategorized : Pour les dossiers qui ne correspondent à aucun modèle

- **Modes d'Opération** :
  - Déplacer (par défaut) : Déplace les fichiers/dossiers vers les répertoires cibles
  - Copier : Crée des copies au lieu de déplacer
  - Lien symbolique : Crée des liens symboliques vers les fichiers/dossiers originaux
  - Simulation (Dry-run) : Montre ce qui se passerait sans effectuer de changements

- **Compatibilité Multiplateforme** :
  - Fonctionne sur Windows, macOS et Linux

## Prérequis

- Python 3.6 ou supérieur
- Aucune bibliothèque supplémentaire requise (utilise uniquement la bibliothèque standard)

## Installation

Si vous avez le code source, vous pouvez l'exécuter en tant que module :

```bash
python -m fl_classifier [options]
```

## Utilisation

### Utilisation de Base

```bash
python -m fl_classifier REP_SOURCE [REP_CIBLE]
```

Si `REP_CIBLE` n'est pas spécifié, les fichiers seront organisés dans un nouveau répertoire appelé `./classified`.

### Options Communes

```
-l, --symlinks       Créer des liens symboliques au lieu de déplacer les fichiers
-c, --copy           Copier les fichiers au lieu de les déplacer
-d, --dry-run        Montrer ce qui serait fait sans réellement le faire
-f, --folders        Inclure les dossiers dans la classification
```

### Méthodes de Classification

```
-e, --extensions     Classer par extensions de fichier (comportement par défaut)
-t, --time           Organiser par attribut de temps
```

### Options d'Organisation Basée sur le Temps

```
--time-attr {modified,created,accessed}
                     Attribut de temps à utiliser (par défaut : modified)
--time-format FORMAT
                     Format de temps pour les répertoires (par défaut : '%Y-%m' pour année-mois)
```

## Exemples

### Organisation Basée sur les Extensions

```bash
# Classer tous les fichiers du dossier Téléchargements par extension
python -m fl_classifier ~/Downloads ~/Organized

# Classer les fichiers et dossiers, créer des copies au lieu de déplacer
python -m fl_classifier ~/Documents ~/Organized -f -c

# Créer des liens symboliques au lieu de déplacer les fichiers
python -m fl_classifier ~/Pictures ~/Organized -l

# Prévisualiser ce qui se passerait sans effectuer de changements
python -m fl_classifier ~/Desktop -d
```

### Organisation Basée sur le Temps

```bash
# Organiser les fichiers par leur temps de modification (année-mois)
python -m fl_classifier ~/Documents ~/TimeOrganized -t

# Organiser par date de création avec format année-mois-jour
python -m fl_classifier ~/Photos ~/Chronological -t --time-attr created --time-format "%Y-%m-%d"

# Organiser les fichiers et dossiers par temps d'accès
python -m fl_classifier ~/Downloads ~/AccessOrganized -t --time-attr accessed -f
```

## FAQ

**Q : Que se passe-t-il si un fichier ou dossier existe déjà dans le répertoire cible ?**
R : Le script le sautera et enregistrera un message d'avertissement.

**Q : L'organisation préservera-t-elle la structure du répertoire ?**
R : Non, tous les fichiers sont aplatis dans les répertoires de catégorie correspondants. Pour une organisation hiérarchique, envisagez d'utiliser l'organisation basée sur le temps avec un format hiérarchique comme `%Y/%m/%d`.

**Q : Puis-je personnaliser les catégories de fichiers ?**
R : Oui, vous pouvez modifier le dictionnaire `FILE_CATEGORIES` dans le script pour ajouter ou modifier des catégories.

## Licence

Cet utilitaire est publié sous la Licence MIT. N'hésitez pas à l'utiliser, le modifier et le distribuer.
