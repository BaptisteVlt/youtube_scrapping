# youtube_scrapping
Test of scrapping youtube data : title of the videos, author, number of likes ...

Pour pouvoir faire tourner le code :
  un fichier input.json dans le dossier du code.
  pour le format du fichier voir l'exemple du fichier input.json déjà présent
  les résultats seront stockés dans output.json
  commande : python3 scrapper.py --input input.json --output output.json
  
Pour lancer les tests :
  python3 -m unittest tests/test.py
  Les tests ne prennet pas la description et les external link par problème d'importation des emojis donc il fail souvent.
  Les tests ne prennent pas les likes car c'est une variable dynamique et donc ils échouent.
  
Le code ne scrappe pas les n premiers commentaires car ils sont dynamiques il est donc compliqué d'y arriver uniquement avec BeautifulSoup et requests
  
  
