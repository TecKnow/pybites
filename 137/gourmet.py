#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator
from typing import List, Tuple

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _similarity(a: str, b: str) -> float:
    counter_a = Counter(a.casefold())
    counter_b = Counter(b.casefold())
    counter_intersection = {key: min(counter_a[key], counter_b[key]) for key in set(
        counter_a.keys()).union(counter_b.keys())}
    intersection_sum = sum(counter_intersection.values())
    len_diff_squared = pow(len(a)-len(b), 2)
    return intersection_sum / (1 + len_diff_squared)


def best_match_per_wine(wine_type: str = "all") -> Tuple[str, str, float]:
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    wine_lists_by_type = {
        "red": RED_WINES,
        "white": WHITE_WINES,
        "sparkling": SPARKLING_WINES,
        "all": RED_WINES + WHITE_WINES + SPARKLING_WINES
    }
    wine_list = wine_lists_by_type.get(wine_type)
    if wine_list is None:
        raise ValueError()
    return max(((wine, cheese, _similarity(wine, cheese)) for wine in wine_list for cheese in CHEESES), key=lambda x: x[2])


def match_wine_5cheeses() -> List[Tuple[str, List[str]]]:
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    all_wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    results = list()
    for wine in all_wines:
        pairings = [(cheese, _similarity(wine, cheese)) for cheese in CHEESES]
        pairings.sort(key=lambda x: x[0])
        pairings.sort(key=lambda x: x[1], reverse=True)
        best_pairings = [pairing[0] for pairing in pairings[:5]]
        results.append((wine, best_pairings))
    sorted_results = sorted(results, key=lambda x: x[0])
    return sorted_results


