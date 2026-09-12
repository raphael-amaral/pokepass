import urllib
import urllib.request
import urllib.error
import argparse
import json
import secrets
import sys

def apiAccess(extra=None):
    url = "https://pokeapi.co/api/v2/pokemon-species/"

    if extra is not None:
        url = f"{url}{extra}"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "pokemon-passphrase/1.0"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return json.load(response)
        
    except urllib.error.HTTPError as error:
        print(f"HTTP error: {error.code}")
        sys.exit(1)

    except urllib.error.URLError as error:
        print(f"Connection error: {error.reason}")
        sys.exit(1)

    except json.JSONDecodeError:
        print(f"The API returned an invalid JSON")
        sys.exit(1)

    except TimeoutError:
        print("Connection timed out")
        sys.exit(1)

def discoverPokemonQuantity():
    return apiAccess()["count"]

def findPokemonNameBySpeciesId(speciesId):
    return apiAccess(speciesId)["name"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=6)
    args = parser.parse_args()
    phraseQuantity = args.n

    pokemonQuantity = discoverPokemonQuantity()
    
    if phraseQuantity <= 0:
        print("Number of pokemons in passphrase can't be 0 or lower")
        return
    
    if phraseQuantity > pokemonQuantity:
        print(f"There isn't enough pokemons for you passphrase (not yet). chose between 1 and {pokemonQuantity} (default is 6)")
        return

    passphrase = ""
    count = 0
    secure_random = secrets.SystemRandom()
    for speciesId in secure_random.sample(range(1, pokemonQuantity + 1), phraseQuantity):
        if count >= 1:
            passphrase += "-"
        passphrase += findPokemonNameBySpeciesId(speciesId)
        count += 1

    print(passphrase)

if __name__ == "__main__":
    main()
    