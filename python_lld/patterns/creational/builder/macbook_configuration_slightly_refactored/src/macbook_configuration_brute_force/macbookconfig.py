from .configs import Model, Chip, Color, RAM, Storage

class MacBookConfiguration:
    
    def __init__(
        self, 
        model: Model, 
        chip: Chip, 
        ram_gb: RAM, 
        storage_gb: Storage, 
        color: Color, 
        apple_care: bool, 
        engraving_text:str
        ):
        
        self.model = model
        self.chip = chip
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.color = color
        self.apple_care = apple_care
        self.engraving_text = engraving_text

class MacBookBuilder:
    def __init__(self):
        self._model = None
        self._chip = None
        self._ram_gb = RAM.GB8
        self._storage_gb = Storage.GB256
        self._color = Color.SILVER
        self._apple_care = False
        self._engraving_text = ""

    def set_model(self, model: Model):
        self._model = model
        return self
    
    def set_chip(self, chip: Chip):
        self._chip = chip
        return self 
    
    def set_ram(self, ram: RAM):
        self._ram_gb = ram
        return self 
    
    def set_storage(self, storage: Storage):
        self._storage_gb = storage
        return self
    
    def color(self, color: Color):
        self._color = color
        return self
    
    def add_apple_care(self):
        self._apple_care = True
        return self
    
    def set_engraving(self, text:str):
        if len(text) > 25:
            raise ValueError("Engraving too large")
        self._engraving_text = text
        return self
    
    def build(self) -> MacBookConfiguration:
        if self._model is None:
            raise ValueError("Model must be set")
        
        if self._chip is None:
            raise ValueError("Chip Must be set")
        
        return MacBookConfiguration(
            model = self._model,
            chip=self._chip,
            ram_gb=self._ram_gb,
            storage_gb=self._storage_gb,
            color = self._color,
            apple_care=self._apple_care,
            engraving_text=self._engraving_text
        )