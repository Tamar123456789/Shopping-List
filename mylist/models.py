from django.db import models  # hier kann man Klassen definieren
from datetime import date

# Create your models here.

class ShoppingItem(models.Model): # Textfelder fuer Datenbank erstellen
    created_at = models.DateField(default=date.today)  # das "date" kommt von Python ,damit kann man sich immer das aktuelle Datum holen muss importiert werden 
    name = models.CharField(max_length=200)    # gibt bereits Python Code mitdem kann man definieren wie es aussehen soll - in dem bsp ein Textfeld
    done = models.BooleanField(default=False)   # kann hier nur wahr oder falsch sein


    def __str__(self):
        return self.name 
