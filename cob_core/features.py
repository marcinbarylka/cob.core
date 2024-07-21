"""Room feature module."""

import random
from typing import Optional


class FeatureFactory:
    FEATURE_TABLE = {
        "Fountain": ["Poison", "Potion", "Alcohol", "Jewel", "Water", "Blood"],
        "Statue": ["Medusa", "Jewels", "Medallion", "Demon", "Talisman", "X"],
        "TrapDoor": ["Trap", "Trap", "Room", "Room", "Pit", "Hellgate"],
        "Furniture": ["Coffin", "Bookcase", "Desk", "Bed", "Clavicord", "Mirror"],
        "Altar": ["Alloces", "Vassago", "Avnas", "Melthus", "Leraje", "Asmoday"],
        "Artwork": ["Tapestry", "Painting", "Statue", "CutGlass", "Icon", "Manuscript"],
        "Mirror": ["Mirror"],  # Assuming a single type for simplicity
        "Staircase": ["Staircase"],  # Assuming a single type for simplicity
    }

    @staticmethod
    def random_feature() -> Optional["Feature"]:
        """
        Return a random feature.

        :return: a random feature or None if no feature is generated.
        """
        if random.randint(1, 80) > 50:  # 62.5% chance to have a feature
            return None

        total_variants = sum(len(variants) for variants in FeatureFactory.FEATURE_TABLE.values())
        random_variant_number = random.randint(1, total_variants)

        for feature_type, variants in FeatureFactory.FEATURE_TABLE.items():
            if random_variant_number <= len(variants):
                feature_variant = random.choice(variants)
                feature_class_name = f"{feature_variant}{feature_type}"
                feature_class = globals().get(feature_class_name)
                return feature_class() if feature_class else None
            random_variant_number -= len(variants)


class Feature: ...


### Fountains ###
class Fountain(Feature): ...


class PoisonFountain(Fountain): ...


class PotionFountain(Fountain): ...


class AlcoholFountain(Fountain): ...


class JewelFouintain(Fountain): ...


class WaterFountain(Fountain): ...


class BloodFountain(Fountain): ...


### Altars ###


class Altar(Feature): ...


class AllocesAltar(Altar): ...


class VassagoAltar(Altar): ...


class AvnasAltar(Altar): ...


class MelthusAltar(Altar): ...


class LerajeAltar(Altar): ...


class AsmodayAltar(Altar): ...


### Trapdoors ###


class TrapDoor(Feature): ...


class TrapTrapDoor(TrapDoor): ...


class RoomTrapDoor(TrapDoor): ...


class PitTrapDoor(TrapDoor): ...


class HellgateTrapDoor(TrapDoor): ...


### Stairs ###
class Staircase(Feature): ...


### Furnitures ###
class Furniture(Feature): ...


class CoffinFurniture(Furniture): ...


class BookcaseFurniture(Furniture): ...


class DeskFurnitire(Furniture): ...


class BedFurniture(Furniture): ...


class ClavicordFurniture(Furniture): ...


class MirrorFurniture(Furniture): ...


### Artworks ###
class Artwork(Feature): ...


class TapestryArtwork(Artwork): ...


class PaintingArtwork(Artwork): ...


class StatueArtwork(Artwork): ...


class CutGlassArtwork(Artwork): ...


class IconArtwork(Artwork): ...


class ManuscriptArtwork(Artwork): ...


### Statues ###
class Statue(Feature): ...


class MedusaStatue(Statue): ...


class JewelsStatue(Statue): ...


class MedallionStatue(Statue): ...


class DemonStatue(Statue): ...


class TalismanStatue(Statue): ...


class XStatue(Statue): ...


### Mirrors ###


class Mirror(Feature): ...
