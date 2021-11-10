from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from myapp.models import Studenci


def home(request):
    return render(request, "home.html", {})

def zapisz(request):

    if request.POST:
        try:
            IdStudent = request.POST['id']
            Imię = request.POST['Imię']
            Nazwisko = request.POST['Nazwisko']
            Miasto = request.POST['Miasto']
            Kod = request.POST['Kod_Pocztowy']

            student = Studenci(

                idStudent=IdStudent,
                Imię=Imię,
                Nazwisko=Nazwisko,
                Miasto=Miasto,
                Kod=Kod,
            )

            student.save()

            msg = "Record successfully added"
            return msg
        except:
            msg = "error in insert operation"
            return msg
    else:
        msg = "Error {request.POST}"
        return msg

def usuń(request):

    if request.method == 'POST':
        try:

            id = request.POST['id']

            Studenci.objects.filter(idStudent=id).delete()

            msg = "Usunięto pomyślnie"
        except:
            msg = "Błąd"

        finally:
            return render(request, "idUsuń.html", {'msg':msg})
    else:
        msg = "Error {request.POST}"
        return render(request, "idUsuń.html", {'msg': msg})

def dodaj(request):

    msg = zapisz(request)
    return render(request, "student.html", {"msg": msg})

def edytuj(request):

    if request.POST:
        try:
            id = request.POST.get('numer', None)
            IdStudent = request.POST.get('id', None)
            Imię = request.POST.get('Imię', None)
            Nazwisko = request.POST.get('Nazwisko',None)
            Miasto = request.POST.get('Miasto', None)
            Kod = request.POST.get('Kod_Pocztowy',None)

            stud = Studenci.objects.filter(idStudent=id)
            stud.idStudent = IdStudent
            stud.Imię = Imię
            stud.Nazwisko = Nazwisko
            stud.Miasto = Miasto
            stud.Kod_Pocztowy = Kod

            if IdStudent:
                stud.update(idStudent = IdStudent)

            if Imię:
                stud.update(Imię = Imię)

            if Nazwisko:
                stud.update(Nazwisko = Nazwisko)

            if Miasto:
                stud.update(Miasto = Miasto)

            if Kod:
                stud.update(Kod_Pocztowy = Kod)

            msg = "Aktualizacja zakończona sukcesem"

        except:
            msg = "Nie powodzenie"

        finally:
            return render(request, "idEdytuj.html", {'msg': msg})
    else:
        msg = "Error {request.POST}"
        return render(request, "idEdytuj.html", {'msg': msg})


class Lista_Studentów(generic.ListView):
    model = Studenci
