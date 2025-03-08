"""Room feature module."""

import random
from typing import TypeVar

F = TypeVar("F", bound="Feature")


class FeatureFactory:
    """Factory class for creating features."""

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
    def random_feature() -> F | None:
        """Return a random feature.

        Returns
        -------
            a random feature or None

        """
        # todo: refactor me
        if random.randint(1, 80) > 50:  # 62.5% chance to have a feature in theory, but we use 50% for simplicity
            return None

        total_variants = sum(len(variants) for variants in FeatureFactory.FEATURE_TABLE.values())
        random_variant_number = random.randint(1, total_variants)  # noqa: S311 [random.randint() is used]

        for feature_type, variants in FeatureFactory.FEATURE_TABLE.items():
            if random_variant_number <= len(variants):
                feature_variant = random.choice(variants)  # noqa: S311 [random.choice() is used]
                feature_class_name = f"{feature_variant}{feature_type}"
                feature_class = globals().get(feature_class_name)
                return feature_class() if feature_class else None
            random_variant_number -= len(variants)
        return None


class Feature:
    """Feature class."""


### Fountains ###
class Fountain(Feature):
    """Fountain class."""


class PoisonFountain(Fountain):
    """PoisonFountain class."""


class PotionFountain(Fountain):
    """PotionFountain class."""


class AlcoholFountain(Fountain):
    """AlcoholFountain class."""


class JewelFouintain(Fountain):
    """JewelFountain class."""


class WaterFountain(Fountain):
    """WaterFountain class."""


class BloodFountain(Fountain):
    """BloodFountain class."""


### Altars ###
class Altar(Feature):
    """Altar class."""


class AllocesAltar(Altar):
    """AllocesAltar class."""


class VassagoAltar(Altar):
    """VassagoAltar class."""


class AvnasAltar(Altar):
    """AvnasAltar class."""


class MelthusAltar(Altar):
    """MelthusAltar class."""


class LerajeAltar(Altar):
    """LerajeAltar class."""


class AsmodayAltar(Altar):
    """AsmodayAltar class."""


### Trapdoors ###
class TrapDoor(Feature):
    """TrapDoor class."""


class TrapTrapDoor(TrapDoor):
    """TrapTrapDoor class."""


class RoomTrapDoor(TrapDoor):
    """RoomTrapDoor class."""


class PitTrapDoor(TrapDoor):
    """PitTrapDoor class."""


class HellgateTrapDoor(TrapDoor):
    """HellgateTrapDoor class."""


### Stairs ###
class Staircase(Feature):
    """Staircase class."""


### Furnitures ###
class Furniture(Feature):
    """Furniture class."""


class CoffinFurniture(Furniture):
    """CoffinFurniture class."""


class BookcaseFurniture(Furniture):
    """BookcaseFurniture class."""


class DeskFurnitire(Furniture):
    """DeskFurniture class."""


class BedFurniture(Furniture):
    """BedFurniture class."""


class ClavicordFurniture(Furniture):
    """ClavicordFurniture class."""


class MirrorFurniture(Furniture):
    """MirrorFurniture class."""


### Artworks ###
class Artwork(Feature):
    """Artwork class."""


class TapestryArtwork(Artwork):
    """TapestryArtwork class."""


class PaintingArtwork(Artwork):
    """PaintingArtwork class."""


class StatueArtwork(Artwork):
    """StatueArtwork class."""


class CutGlassArtwork(Artwork):
    """CutGlassArtwork class."""


class IconArtwork(Artwork):
    """IconArtwork class."""


class ManuscriptArtwork(Artwork):
    """ManuscriptArtwork class."""


### Statues ###
class Statue(Feature):
    """Statue class."""


class MedusaStatue(Statue):
    """MedusaStatue class."""


class JewelsStatue(Statue):
    """JewelsStatue class."""


class MedallionStatue(Statue):
    """MedallionStatue class."""


class DemonStatue(Statue):
    """DemonStatue class."""


class TalismanStatue(Statue):
    """TalismanStatue class."""


class XStatue(Statue):
    """XStatue class."""


### Mirrors ###
class Mirror(Feature):
    """Mirror class."""
