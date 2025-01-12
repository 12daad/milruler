

# 武器配件组合
class WeaponAccessory():

    WEAPON_ACCESSORY_LIST = []
    
    def set_dist_per_mil(self, dist_per_mil:float):
        self.dist_per_mil = dist_per_mil
        
    def set_pixel_per_mil(self, pixel_per_mil:float):
        self.pixel_per_mil = pixel_per_mil

    def __eq__(self, another):
        return  self.weapon == another.weapon and \
                self.barrel == another.barrel and \
                self.ammo == another.ammo and \
                self.scope == another.scope and \
                self.dist_per_mil == another.dist_per_mil and \
                self.pixel_per_mil == another.pixel_per_mil
                
        
    def __init__(self, weapon, barrel, ammo, scope, dist_per_mil:float, pixel_per_mil:float):
        self.weapon = weapon
        self.barrel = barrel
        self.ammo = ammo
        self.scope = scope
        self.dist_per_mil = dist_per_mil
        self.pixel_per_mil = pixel_per_mil

    def __str__(self):
        return f"{self.weapon}, {self.barrel}, {self.ammo}, {self.scope}"
    
    def calculate_correcting(self, dist:float) -> float:
        """
            计算弹道校正值，单位为平面像素
        """
        return dist / self.dist_per_mil * self.pixel_per_mil
    
    def set_pixel_per_mil(self, pixel_per_mil):
        self.pixel_per_mil = pixel_per_mil
        
    def set_dist_per_mil(self, dist_per_mil):
        self.dist_per_mil = dist_per_mil


def _init():
    import json
    
    try:
        with open(r"conf.json", 'r', encoding='utf-8') as file:
            conf = json.load(file)
    except Exception as e:
        print(e)
    
    for it in conf:
        accessory = WeaponAccessory(weapon=it["weapon"], 
                                    barrel=it["barrel"],   
                                    ammo=it["ammo"], 
                                    scope=it["scope"],  
                                    dist_per_mil=it["dist_per_mil"], 
                                    pixel_per_mil=it["pixel_per_mil"])
        WeaponAccessory.WEAPON_ACCESSORY_LIST.append(accessory)
    
_init()
