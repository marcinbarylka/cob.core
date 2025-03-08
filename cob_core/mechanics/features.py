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

    pass


### Fountains ###
class Fountain(Feature):
    """Fountain class."""

    pass


class PoisonFountain(Fountain):
    """PoisonFountain class."""

    pass


class PotionFountain(Fountain):
    """PotionFountain class."""

    pass


class AlcoholFountain(Fountain):
    """AlcoholFountain class."""

    pass


class JewelFouintain(Fountain):
    """JewelFountain class."""

    pass


class WaterFountain(Fountain):
    """WaterFountain class."""

    pass


class BloodFountain(Fountain):
    """BloodFountain class."""

    pass


### Altars ###
class Altar(Feature):
    """Altar class."""

    pass


class AllocesAltar(Altar):
    """AllocesAltar class."""

    pass


class VassagoAltar(Altar):
    """VassagoAltar class."""

    pass


class AvnasAltar(Altar):
    """AvnasAltar class."""

    pass


class MelthusAltar(Altar):
    """MelthusAltar class."""

    pass


class LerajeAltar(Altar):
    """LerajeAltar class."""

    pass


class AsmodayAltar(Altar):
    """AsmodayAltar class."""

    pass


### Trapdoors ###
class TrapDoor(Feature):
    """TrapDoor class."""

    pass


class TrapTrapDoor(TrapDoor):
    """TrapTrapDoor class."""

    pass


class RoomTrapDoor(TrapDoor):
    """RoomTrapDoor class."""

    pass


class PitTrapDoor(TrapDoor):
    """PitTrapDoor class."""

    pass


class HellgateTrapDoor(TrapDoor):
    """HellgateTrapDoor class."""

    pass


### Stairs ###
class Staircase(Feature):
    """Staircase class."""

    pass


### Furnitures ###
class Furniture(Feature):
    """Furniture class."""

    pass


class CoffinFurniture(Furniture):
    """CoffinFurniture class."""

    pass


class BookcaseFurniture(Furniture):
    """BookcaseFurniture class."""

    pass


class DeskFurnitire(Furniture):
    """DeskFurniture class."""

    pass


class BedFurniture(Furniture):
    """BedFurniture class."""

    pass


class ClavicordFurniture(Furniture):
    """ClavicordFurniture class."""

    pass


class MirrorFurniture(Furniture):
    """MirrorFurniture class."""

    pass


### Artworks ###
class Artwork(Feature):
    """Artwork class."""

    pass


class TapestryArtwork(Artwork):
    """TapestryArtwork class."""

    pass


class PaintingArtwork(Artwork):
    """PaintingArtwork class."""

    pass


class StatueArtwork(Artwork):
    """StatueArtwork class."""

    pass


class CutGlassArtwork(Artwork):
    """CutGlassArtwork class."""

    pass


class IconArtwork(Artwork):
    """IconArtwork class."""

    pass


class ManuscriptArtwork(Artwork):
    """ManuscriptArtwork class."""

    pass


### Statues ###
class Statue(Feature):
    """Statue class."""

    pass


class MedusaStatue(Statue):
    """MedusaStatue class."""

    pass


class JewelsStatue(Statue):
    """JewelsStatue class."""

    pass


class MedallionStatue(Statue):
    """MedallionStatue class."""

    pass


class DemonStatue(Statue):
    """DemonStatue class."""

    pass


class TalismanStatue(Statue):
    """TalismanStatue class."""

    pass


class XStatue(Statue):
    """XStatue class."""

    pass


### Mirrors ###
class Mirror(Feature):
    """Mirror class."""

    pass
