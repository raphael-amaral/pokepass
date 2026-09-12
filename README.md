# Pokémon Passphrase

A simple CLI passphrase generator that uses Pokémon names from the PokéAPI.

## Requirements

* Python 3.10+

## Usage

Generate a passphrase with the default length of 6 Pokémon:

```bash
python3 main.py
```

Choose the number of Pokémon:

```bash
python3 main.py -n 10
```

Example output:

```text
dewott-pikachu-buneary-burmy-heliolisk-happiny
```

## Notes

Pokémon names are retrieved from the [PokéAPI](https://pokeapi.co/).

Passphrases are generated using Python's `secrets` module.
