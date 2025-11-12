```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    class Noppa{
        HeitaNoppa()
    }
    Monopolipeli "1" -- "1" Pelilauta
    class Pelilauta{
        List~Ruudut
        pelinappula
        aloitusruutu
        vankila
        siirraNappula(pelaaja, askeleet)
    }
    Pelilauta "1" -- "40" Ruutu
    class Ruutu{
        aloitusruutu
        vankila
        katu
        asema
        laitos
        sattumaJaYhteism
    }
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    class Pelinappula{
        pelaaja
        indeksi
    }
    Pelinappula "1" -- "1" Pelaaja
    class Pelaaja{
        id
        heitaNoppa()
    }
    Pelaaja "2..8" -- "1" Monopolipeli
```