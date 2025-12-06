# Aplikacija za Generiranje Memov

## Opis

To je **aplikacija za generiranje memov**, ki je narejena z **Flaskom** in preprosto HTML predlogo za **Frontend**. Aplikacija omogoča uporabnikom, da naložijo sliko in nanjo dodajo besedilo (zgornje in spodnje), da ustvarijo prilagojen meme. Aplikacija je dockerizirana za enostavno namestitev in implementacijo.

## Zahteve

- Docker (za zagon aplikacije v vsebniku)
- Python 3.x (za lokalni razvoj, če je potrebno, uporabljen je 3.12)

## Namestitev in nastavitev

Za zagon te aplikacije z Dockerjem, sledite spodnjim korakom.

### 1. Kloniranje repozitorija

Klonirajte repozitorij na svojo lokalno napravo:

```bash
git clone <repository-url>
cd meme-generator
```

### 2. Zaganjanje v dockerju

#### Kreiranje Docker slike 
```bash
docker build -t meme-generator .
```

#### Zaganjanje
Ko je slika uspešno zagnana lahko container zaženemo z:
```bash
docker run -p 5556:5556 meme-generator
```
