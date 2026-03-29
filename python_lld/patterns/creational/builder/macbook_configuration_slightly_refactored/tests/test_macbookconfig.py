import pytest
from macbook_configuration_brute_force.macbookconfig import MacBookConfiguration
from macbook_configuration_brute_force.configs import Model, Chip, Color, RAM, Storage

def test_valid_macbook_config():
    config = MacBookConfiguration(
        model = Model.INCH_14,
        chip = Chip.M3,
        ram_gb=RAM.GB16,
        storage_gb=Storage.GB2048,
        color=Color.SPACE_GRAY,
        apple_care= True,
        engraving_text="mynameisanish"
    )
    
    assert config.model == Model.INCH_14
    assert config.chip == Chip.M3
    assert config.ram_gb == RAM.GB16
    assert config.storage_gb == Storage.GB2048
    assert config.apple_care ==True
    assert config.color == Color.SPACE_GRAY
    assert config.engraving_text == "mynameisanish"

def test_invalid_macbook_config():
    with pytest.raises(ValueError):
        MacBookConfiguration(
            model = Model.INCH_14,
            chip = Chip.M3,
            ram_gb=RAM.GB16,
            storage_gb=Storage.GB2048,
            color=Color.SPACE_GRAY,
            apple_care= True,
            engraving_text="mynameisatrsdtngravn1234567890nish"
        )
