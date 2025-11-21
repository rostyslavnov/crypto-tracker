# Crypto Tracker

Prosta aplikacja webowa do sprawdzania aktualnych kursów kryptowalut  
(Bitcoin, Ethereum, Litecoin, XRP) w wybranej walucie (USD, EUR, PLN).  
Projekt działa w architekturze **dwóch kontenerów Docker**:  
backend (FastAPI) + frontend (Nginx).

---

##  Funkcjonalność

- Pobieranie aktualnej ceny wybranej kryptowaluty  
- Pobieranie zmiany procentowej z ostatnich 24h  
- Wsparcie dla waluty: USD
- Ładny, responsywny frontend
- Brak konieczności używania kluczy API — dane pobierane z CoinPaprika API

---
Aplikacja uruchamia 2 kontenery:

1. **crypto-api** – backend (FastAPI)  
2. **crypto-frontend** – frontend (Nginx) pod adresem http://localhost:8080

---