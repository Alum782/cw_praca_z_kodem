
**Instrukcja jak poprawnie zainstalować zależności i uruchomić aplikację.**

!Instrukcja napisana dla systemów Linuks opartych o dystrybucję Ubuntu!

1.Sklonuj repozytorium na swój lokalny komputer:

  a) Otwórz terminal lub wiersz polecenia na swoim komputerze.
  b) Przejdź do katalogu, w którym chcesz umieścić sklonowane repozytorium.
  c) Wpisz polecenie: **git clone https://github.com/Alum782/cw_praca_z_kodem.git**
  
2. Upewnij się że masz zainstalowany Python
  Wpisz: **python --version**
  Powinna wyskoczyć informacja jaka jest zainstalowana wersja pythona na twoim komputerze. Jeśli nie, to musisz zainstalować pythona

3. Zainstaluj wirtualne środowisko Pythona:
   a) Przejdź do katalogu, w którym chcesz utworzyć wirtualne środowisko
   b) Wykonaj polecenie: **sudo apt install python3.8-venv**
   c) Wykonaj polecenie: **python3 -m venv nazwa_środowiska**, gdzie nazwa_środowiska jest nazwą, którą chcesz nadać swojemu wirtualnemu środowisku.
   d) Aktywuj wirtualne środowisko Wpisz: **source nazwa_środowiska/bin/activate**

4. Zainstaluj Flask
    Wpisz: **pip3 install flask**
    Aby sprawdzić czy flask zainstalował się pomyślnie wpisz: **flask --version**
    
5. Przejdź do katalogu, w którym skonowane jest repozytorium git
    Wpisz: **cd ścieżka_do_katalogu**
6. W terminalu wpisz po kolei polecenia:
    **a) make install
    b) make init
    c) make run**
7. Otwórz drugie okno terminala i wpisz polecenia:
    **curl http://127.0.0.1:5000/**
    **curl -L http://127.0.0.1:5000/hello**
    **curl http://127.0.0.1:5000/hello/<name>** - gdzie w miejsce <name> wpisz własne imię (bez tych znaków <>)
8. (Opcjonalnie) Możesz otworzyć przeglądarkę i wpisać wyżej wymienione adresy bez polecenia curl, aby zobaczyć jak wygląda strona
9. Aby wyłączyć serwer Flask przejdź do terminala, gdzie jest uruchomiony i kliknij **ctrl + c**

  Plik README.md jest ważne w projekcie bo może zawierać informacje na temat funkcji, zastosowania, wymagań systemowych, struktury projektu, instrukcji dla programistów oraz wiele innych istotnych informacji.
