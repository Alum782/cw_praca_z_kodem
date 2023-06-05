# Instrukcja jak poprawnie zainstalować zależności i uruchomić aplikację

!Instrukcja napisana dla systemów Linux opartych o dystrybucję Ubuntu!

1. Sklonuj repozytorium na swój lokalny komputer:

   a) Otwórz terminal lub wiersz polecenia na swoim komputerze.
   
   b) Przejdź do katalogu, w którym chcesz umieścić sklonowane repozytorium. 
      Wpisz: `cd ścieżka_do_katalogu`
   
   c) Wpisz polecenie: `git clone https://github.com/Alum782/cw_praca_z_kodem.git`

2. Upewnij się, że masz zainstalowanego Pythona:

   Wpisz: `python --version`
   
   Powinna pojawić się informacja o zainstalowanej wersji Pythona na twoim komputerze. Jeśli nie, musisz zainstalować Pythona.

3. Zainstaluj wirtualne środowisko Pythona:

   a) Przejdź do katalogu, w którym chcesz utworzyć wirtualne środowisko.
   
   b) Wykonaj polecenie: `sudo apt install python3.8-venv`
   
   c) Wykonaj polecenie: `python3 -m venv nazwa_środowiska`, gdzie nazwa_środowiska to nazwa, którą chcesz nadać swojemu wirtualnemu środowisku.
   
   d) Aktywuj wirtualne środowisko: `source nazwa_środowiska/bin/activate`

4. Zainstaluj Flask:

   Wpisz: `pip3 install flask`
   
   Aby sprawdzić, czy Flask zainstalował się pomyślnie, wpisz: `flask --version`
   
5. Zainstaluj Curl:

   Wpisz: `apt-get install curl`

6. Przejdź do katalogu, w którym sklonowane jest repozytorium Git:

   Wpisz: `cd ścieżka_do_katalogu`

7. W terminalu wpisz po kolei polecenia:

   a) `make install`
   
   b) `make init`
   
   c) `make run`

8. Otwórz drugie okno terminala za pomocą skrótu klawiszowego `Ctrl + Shift + T` i wpisz polecenia:

   a) `curl http://127.0.0.1:5000/`
   
   b) `curl -L http://127.0.0.1:5000/hello`
   
   c) `curl http://127.0.0.1:5000/hello/<name>` - gdzie w miejsce `<name>` wpisz własne imię (bez tych znaków <>)

9. (Opcjonalnie) Możesz otworzyć przeglądarkę i wpisać powyższe adresy bez polecenia curl, aby zobaczyć, jak wygląda strona.

10. Aby wyłączyć serwer Flask, przejdź do terminala, gdzie jest uruchomiony i naciśnij `Ctrl + C`.

Plik README.md jest ważne w projekcie bo może zawierać informacje na temat funkcji, zastosowania, wymagań systemowych, struktury projektu, instrukcji dla programistów oraz wiele innych istotnych informacji.
