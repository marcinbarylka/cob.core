"""Room feature module."""


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
