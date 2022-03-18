from utente import Utente
from postgres import PostGres



db = PostGres('localhost', 'postgres', 'postgres', 'root')
ut = Utente('Lorenzo', 'Germano', 'booo@booo.com', db)

ut.save()

#ut.update_email('ciao@ciao', 43)
#ut.update_name('Lore', 43)
#ut.update_surname('Germ', 43)

#ut.delete(43)