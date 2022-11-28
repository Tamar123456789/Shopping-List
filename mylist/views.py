from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.

def mylist(request): #kann man views definieren (so definiert man Funktionen in Python)
    if request.method == 'POST': # Abfrage ob es sich um einen POST request handelt
        print('Received data:', request.POST['itemName']) # Daten werden hier von dem Frontend an das Backend uebergeben
        ShoppingItem.objects.create(name = request.POST['itemName']) # aus Models Datei importiert ,koennen neue Elemente hinzugefuegt werden
    all_items = ShoppingItem.objects.all()

    return render(request, 'shopping_list.html' , {'all_items' : all_items})  #html datei am ende noch mit url verknuepfen


    