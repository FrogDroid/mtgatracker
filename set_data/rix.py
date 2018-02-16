import sys
from models.card import Card
from models.set import Set
import inspect


BafflingEnd = Card("baffling_end", "RIX", 1, 66619)
BishopofBinding = Card("bishop_of_binding", "RIX", 2, 66621)
BlazingHope = Card("blazing_hope", "RIX", 3, 66623)
CleansingRay = Card("cleansing_ray", "RIX", 4, 66625)
DivineVerdict = Card("divine_verdict", "RIX", 5, 66627)
EverdawnChampion = Card("everdawn_champion", "RIX", 6, 66629)
ExultantSkymarcher = Card("exultant_skymarcher", "RIX", 7, 66631)
FamishedPaladin = Card("famished_paladin", "RIX", 8, 66633)
ForerunneroftheLegion = Card("forerunner_of_the_legion", "RIX", 9, 66635)
ImperialCeratops = Card("imperial_ceratops", "RIX", 10, 66637)
LegionConquistador = Card("legion_conquistador", "RIX", 11, 66639)
LuminousBonds = Card("luminous_bonds", "RIX", 12, 66641)
MajesticHeliopterus = Card("majestic_heliopterus", "RIX", 13, 66643)
MartyrofDusk = Card("martyr_of_dusk", "RIX", 14, 66645)
MomentofTriumph = Card("moment_of_triumph", "RIX", 15, 66647)
PaladinofAtonement = Card("paladin_of_atonement", "RIX", 16, 66649)
PrideofConquerors = Card("pride_of_conquerors", "RIX", 17, 66651)
RadiantDestiny = Card("radiant_destiny", "RIX", 18, 66653)
RaptorCompanion = Card("raptor_companion", "RIX", 19, 66655)
SanguineGlorifier = Card("sanguine_glorifier", "RIX", 20, 66657)
SkymarcherAspirant = Card("skymarcher_aspirant", "RIX", 21, 66659)
SlaughtertheStrong = Card("slaughter_the_strong", "RIX", 22, 66661)
SnubhornSentry = Card("snubhorn_sentry", "RIX", 23, 66663)
SphinxsDecree = Card("sphinxs_decree", "RIX", 24, 66665)
SquiresDevotion = Card("squires_devotion", "RIX", 25, 66667)
SunSentinel = Card("sun_sentinel", "RIX", 26, 66669)
SunCrestedPterodon = Card("suncrested_pterodon", "RIX", 27, 66671)
TempleAltisaur = Card("temple_altisaur", "RIX", 28, 66673)
TrapjawTyrant = Card("trapjaw_tyrant", "RIX", 29, 66675)
ZetalpaPrimalDawn = Card("zetalpa_primal_dawn", "RIX", 30, 66677)
AdmiralsOrder = Card("admirals_order", "RIX", 31, 66679)
AquaticIncursion = Card("aquatic_incursion", "RIX", 32, 66681)
CraftyCutpurse = Card("crafty_cutpurse", "RIX", 33, 66683)
CrashingTide = Card("crashing_tide", "RIX", 34, 66685)
CuriousObsession = Card("curious_obsession", "RIX", 35, 66687)
DeadeyeRigHauler = Card("deadeye_righauler", "RIX", 36, 66689)
ExpelfromOrazca = Card("expel_from_orazca", "RIX", 37, 66691)
FloodofRecollection = Card("flood_of_recollection", "RIX", 38, 66693)
Hornswoggle = Card("hornswoggle", "RIX", 39, 66695)
InducedAmnesia = Card("induced_amnesia", "RIX", 40, 66697)
KitesailCorsair = Card("kitesail_corsair", "RIX", 41, 66699)
KumenasAwakening = Card("kumenas_awakening", "RIX", 42, 66701)
MistCloakedHerald = Card("mistcloaked_herald", "RIX", 43, 66703)
Negate = Card("negate", "RIX", 44, 66705)
NezahalPrimalTide = Card("nezahal_primal_tide", "RIX", 45, 66707)
ReleasetotheWind = Card("release_to_the_wind", "RIX", 46, 66709)
RiverDarter = Card("river_darter", "RIX", 47, 66711)
RiverwiseAugur = Card("riverwise_augur", "RIX", 48, 66713)
SailorofMeans = Card("sailor_of_means", "RIX", 49, 66715)
SeaLegs = Card("sea_legs", "RIX", 50, 66717)
SeafloorOracle = Card("seafloor_oracle", "RIX", 51, 66719)
SecretsoftheGoldenCity = Card("secrets_of_the_golden_city", "RIX", 52, 66721)
SilvergillAdept = Card("silvergill_adept", "RIX", 53, 66723)
SirenReaver = Card("siren_reaver", "RIX", 54, 66725)
SlipperyScoundrel = Card("slippery_scoundrel", "RIX", 55, 66727)
SouloftheRapids = Card("soul_of_the_rapids", "RIX", 56, 66729)
SpireWinder = Card("spire_winder", "RIX", 57, 66731)
SwornGuardian = Card("sworn_guardian", "RIX", 58, 66733)
TimestreamNavigator = Card("timestream_navigator", "RIX", 59, 66735)
WarkiteMarauder = Card("warkite_marauder", "RIX", 60, 66737)
Waterknot = Card("waterknot", "RIX", 61, 66739)
ArterialFlow = Card("arterial_flow", "RIX", 62, 66741)
CanalMonitor = Card("canal_monitor", "RIX", 63, 66743)
ChampionofDusk = Card("champion_of_dusk", "RIX", 64, 66745)
DarkInquiry = Card("dark_inquiry", "RIX", 65, 66747)
DeadMansChest = Card("dead_mans_chest", "RIX", 66, 66749)
DinosaurHunter = Card("dinosaur_hunter", "RIX", 67, 66751)
DireFleetPoisoner = Card("dire_fleet_poisoner", "RIX", 68, 66753)
DuskCharger = Card("dusk_charger", "RIX", 69, 66755)
DuskLegionZealot = Card("dusk_legion_zealot", "RIX", 70, 66757)
FathomFleetBoarder = Card("fathom_fleet_boarder", "RIX", 71, 66759)
ForerunneroftheCoalition = Card("forerunner_of_the_coalition", "RIX", 72, 66761)
GoldenDemise = Card("golden_demise", "RIX", 73, 66763)
GraspingScoundrel = Card("grasping_scoundrel", "RIX", 74, 66765)
GruesomeFate = Card("gruesome_fate", "RIX", 75, 66767)
Impale = Card("impale", "RIX", 76, 66769)
MastermindsAcquisition = Card("masterminds_acquisition", "RIX", 77, 66771)
MausoleumHarpy = Card("mausoleum_harpy", "RIX", 78, 66773)
MomentofCraving = Card("moment_of_craving", "RIX", 79, 66775)
OathswornVampire = Card("oathsworn_vampire", "RIX", 80, 66777)
PitilessPlunderer = Card("pitiless_plunderer", "RIX", 81, 66779)
RavenousChupacabra = Card("ravenous_chupacabra", "RIX", 82, 66781)
ReaverAmbush = Card("reaver_ambush", "RIX", 83, 66783)
Recover = Card("recover", "RIX", 84, 66785)
SadisticSkymarcher = Card("sadistic_skymarcher", "RIX", 85, 66787)
TetzimocPrimalDeath = Card("tetzimoc_primal_death", "RIX", 86, 66789)
TombRobber = Card("tomb_robber", "RIX", 87, 66791)
TwilightProphet = Card("twilight_prophet", "RIX", 88, 66793)
VampireRevenant = Card("vampire_revenant", "RIX", 89, 66795)
VonasHunger = Card("vonas_hunger", "RIX", 90, 66797)
VoraciousVampire = Card("voracious_vampire", "RIX", 91, 66799)
BloodSun = Card("blood_sun", "RIX", 92, 66801)
Bombard = Card("bombard", "RIX", 93, 66803)
BrasssBounty = Card("brasss_bounty", "RIX", 94, 66805)
BrazenFreebooter = Card("brazen_freebooter", "RIX", 95, 66807)
BuccaneersBravado = Card("buccaneers_bravado", "RIX", 96, 66809)
ChargingTuskodon = Card("charging_tuskodon", "RIX", 97, 66811)
DaringBuccaneer = Card("daring_buccaneer", "RIX", 98, 66813)
DireFleetDaredevil = Card("dire_fleet_daredevil", "RIX", 99, 66815)
EtaliPrimalStorm = Card("etali_primal_storm", "RIX", 100, 66817)
FanaticalFirebrand = Card("fanatical_firebrand", "RIX", 101, 66819)
ForerunneroftheEmpire = Card("forerunner_of_the_empire", "RIX", 102, 66821)
FormoftheDinosaur = Card("form_of_the_dinosaur", "RIX", 103, 66823)
FrilledDeathspitter = Card("frilled_deathspitter", "RIX", 104, 66825)
GoblinTrailblazer = Card("goblin_trailblazer", "RIX", 105, 66827)
Mutiny = Card("mutiny", "RIX", 106, 66829)
NeedletoothRaptor = Card("needletooth_raptor", "RIX", 107, 66831)
OrazcaRaptor = Card("orazca_raptor", "RIX", 108, 66833)
PiratesPillage = Card("pirates_pillage", "RIX", 109, 66835)
RecklessRage = Card("reckless_rage", "RIX", 110, 66837)
RekindlingPhoenix = Card("rekindling_phoenix", "RIX", 111, 66839)
SeeRed = Card("see_red", "RIX", 112, 66841)
ShaketheFoundations = Card("shake_the_foundations", "RIX", 113, 66843)
Shatter = Card("shatter", "RIX", 114, 66845)
SilvercladFerocidons = Card("silverclad_ferocidons", "RIX", 115, 66847)
StampedingHorncrest = Card("stampeding_horncrest", "RIX", 116, 66849)
StormFleetSwashbuckler = Card("storm_fleet_swashbuckler", "RIX", 117, 66851)
SunCollaredRaptor = Card("suncollared_raptor", "RIX", 118, 66853)
SwaggeringCorsair = Card("swaggering_corsair", "RIX", 119, 66855)
TilonallisCrown = Card("tilonallis_crown", "RIX", 120, 66857)
TilonallisSummoner = Card("tilonallis_summoner", "RIX", 121, 66859)
AggressiveUrge = Card("aggressive_urge", "RIX", 122, 66861)
Cacophodon = Card("cacophodon", "RIX", 123, 66863)
CherishedHatchling = Card("cherished_hatchling", "RIX", 124, 66865)
ColossalDreadmaw = Card("colossal_dreadmaw", "RIX", 125, 66867)
CrestedHerdcaller = Card("crested_herdcaller", "RIX", 126, 66869)
DeeprootElite = Card("deeproot_elite", "RIX", 127, 66871)
EntertheUnknown = Card("enter_the_unknown", "RIX", 128, 66873)
ForerunneroftheHeralds = Card("forerunner_of_the_heralds", "RIX", 129, 66875)
GhaltaPrimalHunger = Card("ghalta_primal_hunger", "RIX", 130, 66877)
GiltgroveStalker = Card("giltgrove_stalker", "RIX", 131, 66879)
HardyVeteran = Card("hardy_veteran", "RIX", 132, 66881)
HunttheWeak = Card("hunt_the_weak", "RIX", 133, 66883)
JadeBearer = Card("jade_bearer", "RIX", 134, 66885)
JadecraftArtisan = Card("jadecraft_artisan", "RIX", 135, 66887)
JadelightRanger = Card("jadelight_ranger", "RIX", 136, 66889)
JunglebornPioneer = Card("jungleborn_pioneer", "RIX", 137, 66891)
KnightoftheStampede = Card("knight_of_the_stampede", "RIX", 138, 66893)
Naturalize = Card("naturalize", "RIX", 139, 66895)
OrazcaFrillback = Card("orazca_frillback", "RIX", 140, 66897)
OvergrownArmasaur = Card("overgrown_armasaur", "RIX", 141, 66899)
PathofDiscovery = Card("path_of_discovery", "RIX", 142, 66901)
Plummet = Card("plummet", "RIX", 143, 66903)
Polyraptor = Card("polyraptor", "RIX", 144, 66905)
StrengthofthePack = Card("strength_of_the_pack", "RIX", 145, 66907)
SwiftWarden = Card("swift_warden", "RIX", 146, 66909)
TendershootDryad = Card("tendershoot_dryad", "RIX", 147, 66911)
ThrashingBrontodon = Card("thrashing_brontodon", "RIX", 148, 66913)
ThunderherdMigration = Card("thunderherd_migration", "RIX", 149, 66915)
WaywardSwordtooth = Card("wayward_swordtooth", "RIX", 150, 66917)
WorldShaper = Card("world_shaper", "RIX", 151, 66919)
AngraththeFlameChained = Card("angrath_the_flamechained", "RIX", 152, 66921)
AtzocanSeer = Card("atzocan_seer", "RIX", 153, 66923)
AzortheLawbringer = Card("azor_the_lawbringer", "RIX", 154, 66925)
DeadeyeBrawler = Card("deadeye_brawler", "RIX", 155, 66927)
DireFleetNeckbreaker = Card("dire_fleet_neckbreaker", "RIX", 156, 66929)
ElendatheDuskRose = Card("elenda_the_dusk_rose", "RIX", 157, 66931)
HadanasClimb = Card("hadanas_climb", "RIX", 158, 66933)
WingedTempleofOrazca = Card("winged_temple_of_orazca", "RIX", 158, 66935)
HuatliRadiantChampion = Card("huatli_radiant_champion", "RIX", 159, 66937)
JourneytoEternity = Card("journey_to_eternity", "RIX", 160, 66939)
AtzalCaveofEternity = Card("atzal_cave_of_eternity", "RIX", 160, 66941)
JungleCreeper = Card("jungle_creeper", "RIX", 161, 66943)
KumenaTyrantofOrazca = Card("kumena_tyrant_of_orazca", "RIX", 162, 66945)
LegionLieutenant = Card("legion_lieutenant", "RIX", 163, 66947)
MerfolkMistbinder = Card("merfolk_mistbinder", "RIX", 164, 66949)
PathofMettle = Card("path_of_mettle", "RIX", 165, 66951)
MetzaliTowerofTriumph = Card("metzali_tower_of_triumph", "RIX", 165, 66953)
ProfaneProcession = Card("profane_procession", "RIX", 166, 66955)
TomboftheDuskRose = Card("tomb_of_the_dusk_rose", "RIX", 166, 66957)
ProteanRaider = Card("protean_raider", "RIX", 167, 66959)
RagingRegisaur = Card("raging_regisaur", "RIX", 168, 66961)
RelentlessRaptor = Card("relentless_raptor", "RIX", 169, 66963)
ResplendentGriffin = Card("resplendent_griffin", "RIX", 170, 66965)
SiegehornCeratops = Card("siegehorn_ceratops", "RIX", 171, 66967)
StormFleetSprinter = Card("storm_fleet_sprinter", "RIX", 172, 66969)
StormtheVault = Card("storm_the_vault", "RIX", 173, 66971)
VaultofCatlacan = Card("vault_of_catlacan", "RIX", 173, 66973)
ZacamaPrimalCalamity = Card("zacama_primal_calamity", "RIX", 174, 66975)
AwakenedAmalgam = Card("awakened_amalgam", "RIX", 175, 66977)
AzorsGateway = Card("azors_gateway", "RIX", 176, 66979)
SanctumoftheSun = Card("sanctum_of_the_sun", "RIX", 176, 66981)
CaptainsHook = Card("captains_hook", "RIX", 177, 66983)
GleamingBarrier = Card("gleaming_barrier", "RIX", 178, 66985)
GoldenGuardian = Card("golden_guardian", "RIX", 179, 66987)
GoldForgeGarrison = Card("goldforge_garrison", "RIX", 179, 66989)
TheImmortalSun = Card("the_immortal_sun", "RIX", 180, 66991)
OrazcaRelic = Card("orazca_relic", "RIX", 181, 66993)
SilentGravestone = Card("silent_gravestone", "RIX", 182, 66995)
StriderHarness = Card("strider_harness", "RIX", 183, 66997)
TravelersAmulet = Card("travelers_amulet", "RIX", 184, 66999)
ArchofOrazca = Card("arch_of_orazca", "RIX", 185, 67001)
EvolvingWilds = Card("evolving_wilds", "RIX", 186, 67003)
ForsakenSanctuary = Card("forsaken_sanctuary", "RIX", 187, 67005)
FoulOrchard = Card("foul_orchard", "RIX", 188, 67007)
HighlandLake = Card("highland_lake", "RIX", 189, 67009)
StoneQuarry = Card("stone_quarry", "RIX", 190, 67011)
WoodlandStream = Card("woodland_stream", "RIX", 191, 67013)
Plains = Card("plains", "RIX", 192, 67015)
Island = Card("island", "RIX", 193, 67017)
Swamp = Card("swamp", "RIX", 194, 67019)
Mountain = Card("mountain", "RIX", 195, 67021)
Forest = Card("forest", "RIX", 196, 67023)
VraskaSchemingGorgon = Card("vraska_scheming_gorgon", "RIX", 197, 67025)
VampireChampion = Card("vampire_champion", "RIX", 198, 67027)
VraskasConquistador = Card("vraskas_conquistador", "RIX", 199, 67029)
VraskasScorn = Card("vraskas_scorn", "RIX", 200, 67031)
AngrathMinotaurPirate = Card("angrath_minotaur_pirate", "RIX", 201, 67033)
AngrathsAmbusher = Card("angraths_ambusher", "RIX", 202, 67035)
SwabGoblin = Card("swab_goblin", "RIX", 203, 67037)
AngrathsFury = Card("angraths_fury", "RIX", 204, 67039)
CinderBarrens = Card("cinder_barrens", "RIX", 205, 67041)

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
RivalsOfIxalan = Set("rivals_of_ixalan", cards=clsmembers)

