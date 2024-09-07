
# Projet de Fin d'Études : Intégration d'un Processus de Fabrication dans l'ERP Odoo

## Description du Projet

Ce projet a pour objectif l'intégration d'un processus de fabrication au sein de l'ERP **Odoo** pour **Maghreb Metal Énergie**, spécialisée dans la fabrication de réservoirs de stockage des hydrocarbures. Cette transformation numérique permettra de :
- **Optimiser les processus de production**,
- **Accroître la cadence de fabrication**,
- **Renforcer la compétitivité de l'entreprise** sur un marché en constante évolution.

Le projet couvre les aspects fonctionnels et techniques de la gestion de la production, incluant la capture des besoins, la gestion des stocks, la génération automatique de la documentation, et la traçabilité complète des produits fabriqués.

## Objectif Global

L'objectif du projet est de fournir une **solution intégrée** et centralisée, permettant à Maghreb Metal Énergie de synchroniser ses processus de production avec d'autres modules de gestion, tels que :
- **Vente** (gestion des commandes),
- **Achat** (vérification des matériaux),
- **Inventaire** (suivi des stocks),
- **Comptabilité** (analyse des coûts).

## Fonctionnalités Clés

1. **Gestion des Commandes** : 
   - Les commandes sont saisies avec les coordonnées des clients et leurs besoins spécifiques.
   - Une commande est assignée à la production uniquement si le produit est un **réservoir**.

2. **Gestion de la Production** : 
   - Génération d’un **ordre de fabrication (OF)** avec la capacité, la catégorie, et le type de réservoir.
   - Création d'une **note de calcul** automatisée pour chaque réservoir basé sur des données de la base de données.
   - Génération de la **nomenclature (BOM)** et vérification automatique de la disponibilité des matériaux dans le stock.

3. **Traçabilité des Produits** : 
   - Chaque produit fabriqué est assigné un **numéro de série (SN)** unique.
   - Documentation associée à chaque produit, disponible à l'importation via l'ERP.

4. **Gestion des Stocks** :
   - Suivi en temps réel des stocks de matières premières et produits finis.
   - Mise à jour automatique du stock après chaque production.

## Technologies Utilisées

- **Odoo ERP** : Intégration des modules de production, vente, achat et inventaire.
- **Python** : Pour le développement de fonctionnalités personnalisées dans Odoo.
- **PostgreSQL** : Base de données pour le stockage des informations de production, stock et clients.
- **XML** et **HTML/CSS** : Pour la personnalisation de l’interface et des rapports.

## Architecture du Projet

- **Diagramme de Classe** : Un diagramme de classe a été développé pour modéliser les différentes entités du système, telles que les commandes, la production, les réservoirs, et les ordres de fabrication.
- **Interface Utilisateur** : Un tableau de bord intégré permet de visualiser les commandes, la production et les indicateurs de performance.

## Installation

### Prérequis

- Python 3.x
- Odoo (version utilisée : 15.0 ou supérieure)
- PostgreSQL
- Git

### Étapes d'Installation

1. Clonez ce dépôt Git dans votre environnement local :
   ```bash
   git clone https://github.com/username/nom-du-projet.git
   ```
2.mettez à jour le fichier de configuration d'Odoo (`odoo.conf`) avec les informations nécessaires.
4. Démarrez le serveur Odoo :
   ```bash
   service odoo16 restart 
   ```
5. Accédez à l'interface Odoo à l'adresse : `http://localhost:8069`
6. Connectez-vous à Odoo et activez le module Production MME.