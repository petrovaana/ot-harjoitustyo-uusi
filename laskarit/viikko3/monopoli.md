---

title: Monopoli

---

classDiagram

&nbsp;   Monopolipeli "1" -- "2" Noppa

&nbsp;   Monopolipeli "1" -- "1" Pelilauta

&nbsp;   Pelilauta "1" -- "40" Ruutu

&nbsp;   Ruutu "1" -- "1" Ruutu : seuraava

&nbsp;   Ruutu "1" -- "0..8" Pelinappula

&nbsp;   Pelinappula "1" -- "1" Pelaaja

&nbsp;   Pelaaja "2..8" -- "1" Monopolipeli

&nbsp;   





&nbsp;   class Monopolipeli{

&nbsp;       +pelaaja

&nbsp;       +pelilauta

&nbsp;       +noppa

&nbsp;       +ruutu

&nbsp;       +aloitusruutu

&nbsp;       +vankila

&nbsp;       +aloita()

&nbsp;       +siirry(pelaaja, askeleet)

&nbsp;   }



&nbsp;   class Pelilauta{

&nbsp;       +ruudut (lista)

&nbsp;       +pelinappuloiden\_paikat

&nbsp;       +aloitusruutu

&nbsp;       +vankila

&nbsp;       +etsi\_ruutu(idx)

    }



    class Ruutu{

        +aloitusruutu

&nbsp;       +vankila

&nbsp;       +kadut

&nbsp;       +asemat

&nbsp;       +laitokset

&nbsp;       +sattumaJaYhteys

&nbsp;       +seuraava

&nbsp;       +suoritaRuutu()

    }



    class Noppa{

        +heitanoppaa() int

    }



    class Pelinappula{

        +paikka

&nbsp;       +siirry(ruutu)

    }



    class Pelaaja{

        +nimi

&nbsp;       +raha

&nbsp;       +pelinappula

&nbsp;       +heitanoppa()

&nbsp;       +siirry(ruutu)

&nbsp;       +osta(katu)

&nbsp;       +maksa(summa)

    }



    class Katu{

        +nimi

&nbsp;       +hinta

&nbsp;       +osta()

&nbsp;       +rakenna()

    }







