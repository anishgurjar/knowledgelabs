class MacBookConfiguration:
    
    def __init__(self, model: str, chip: str, ram_gb: int = 8, storage_gb: int = 256, color: str = "Silver", apple_care: bool = False, engraving_text:str=""):

        allowed_models = ["14-inch", "16-inch"]
        if model not in allowed_models:
            raise ValueError(f"Model entered is incorrect. Allowed values are {allowed_models}")
        
        allowed_chips = ["M3", "M3 Pro", "M3 Max"]
        if chip not in allowed_chips:
            raise ValueError(f"Incorrect chip provided. Allowed values are {allowed_chips}")
        
        allowed_ram_values = [4,8,16,32,64,128,256,512]
        if ram_gb not in allowed_ram_values:
            raise ValueError(f"Incorrect ram gb provided. Allowed values are 2,4,8,16, etc.")
        
        allowed_storage_values = [256,512,1024,2048,3096]
        if storage_gb not in allowed_storage_values:
            raise ValueError(f"Invalid storage provided. Allowed values are {allowed_storage_values}")
        
        max_engraving_length = 25
        if len(engraving_text) > max_engraving_length:
            raise ValueError(f"Engraving text length too large. Max length = {max_engraving_length}")
        
        allowed_colors = ["Silver", "Space Gray"]
        if color not in allowed_colors:
            raise ValueError(f"Incorrect Color. Allowed colors are {allowed_colors}")

        self.model = model
        self.chip = chip
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.color = color
        self.apple_care = apple_care
        self.engraving_text = engraving_text
    