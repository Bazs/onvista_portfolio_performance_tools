### Overview
Tools to import data from an [onvista bank](https://www.onvista-bank.de/) depot account into the free and useful 
[Portfolio Performance](https://www.portfolio-performance.info/portfolio/) application.

### Import data from onvista to Portfolio Performance
#### Initial import
To set up your initial Portfolio Performance portfolio, export your "Deportübersicht Wertpapiere" to CSV.
![depotuebersicht](doc\depotuebersicht.PNG)

![csv_export](doc\csv_export.PNG)

Then import this into Portfolio Performance using the template provided in this repo called `Portfolio Performance CSV templates\onvista_securites_account_statement_(initial_import).json`
The CSV import is under File/Import/CSV Files.

#### Import further transactions
After the initial import, any new transactions you perform in your account can be exported via the "Transaktionsliste Wertpapiere" menu in the onvista webapp.
![transaktionsliste](doc\transaktionsliste.PNG) export to CSV again.

This CSV needs to be converted to a Portfolio Performance-friendly format, using the script `convert_onvista_transaction_list.py`.
The only argument is `-f`, which should point to the transaction list CSV you've exported from onvista. It'll convert it and place it in the same folder, with the `_import_ready` filename suffix.

This file can then be imported into Portfolio Performance using the template in this repo called `Portfolio Performance CSV templates\onvista_transaction_list.json`


