Il faut télécharger toutes les dépendances necessaires au projet :
python.exe -m pip install --upgrade pip
pip install pytest  
pip install unittest
python -m unittest  -v     

Pour les commandes de teste:

python -m unittest test.test_sondage ou python -m unittest test.test_sondage.py
python -m unittest test.test_villes ou python -m unittest test.test_villes.py
python -m unittest test.test_calculs -v

pytest test/test_todo.py ou python -m pytest test/ test_todo
pytest test.test_bibliotheque.py ou pytest test.test_bibliotheque
pytest test.test_livre  ou pytest test/test_livre  
pytest test/ test_todo ou pytest test/ test_todo.py
 pytest test.test_livre    ou pytest test/test_livre 
python -m pytest test/ test_todo

