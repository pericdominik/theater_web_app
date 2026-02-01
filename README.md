# Web Aplikacija Za Putujuću Lutkarsku Kazališnu Družinu

## Zadatak:
Kreirati web aplikaciju za putujuću lutkarsku kazališnu družinu. Svaka stranica sadrži izbornik koji korisnicima omogućuje odlazak na ostale stranice web aplikacije. Jedna stranica sadrži kalendar koji po tjednima prikazuje raspored predstava. Aplikacija sadrži tri tipa korisnika: administrator, registrirani korisnik i gost. Administrator potvrđuje svaki unos komentara prije objave. Proizvoljno dodati stranicu ili dvije koje bi bile potrebne korisnicima.

## Funkcionalni zahtjevi aplikacije
Funkcionalni zahtjevi izrađene aplikacije su: 
- Prijava, registracija i odjava korisnika
- Pregled predstava
- Prikaz termina predstava preko tjednog kalendara
- Komentiranje i lajkanje predstava
- Rezervacija ulaznica
- Pregledavanje i uređivanje profila

## Nefunkcionalni zahtjevi aplikacije
Nefunkcionalni zahtjevi aplikacije su:
- Upotrebljivost i kompatibilnost - sučelje jednostavno za korištenje, responzivan izgled
- Sigurnost (CSRF token) - zaštita od lažnih zahtjeva pri ispunjivanju obrazaca
- Pristupačnost – aplikacija je pregledna na mobilnim uređajima i lako se koristi preko izbornika
- Održavanje – programski kod je organiziran i lako se nadograđuje (Django arhitektura)

## Korištene tehnologije
- **Python** – programski jezik korišten za razvoj aplikacije
- **Django** – web framework za izradu backend logike, modela, pogleda i sigurnosnih mehanizama
- **HTML** – struktura web stranica
- **CSS** – stilizacija i raspored elemenata
- **Bootstrap** – responzivni dizajn i grid sustav
- **SQLite** – relacijska baza podataka za pohranu podataka o korisnicima, predstavama i rezervacijama
- **Git** – sustav za kontrolu verzija i praćenje razvoja aplikacije
- **Visual Studio Code** – razvojno okruženje
- **Microsoft Designer** – izrada grafičkih materijala i slika predstava
