import pytest
from macbook_configuration_brute_force.macbookconfig import MacBookConfiguration

def test_valid_macbook_config():
    config = MacBookConfiguration(
        model = "14-inch",
        chip = "M3",
        ram_gb=16,
        storage_gb=2048,
        color="Space Gray",
        apple_care= True,
        engraving_text="mynameisanish"
    )
    
    assert config.model == "14-inch"
    assert config.chip == "M3"
    assert config.ram_gb == 16
    assert config.storage_gb == 2048
    assert config.apple_care ==True
    assert config.engraving_text == "mynameisanish"

def test_invalid_macbook_config():
    with pytest.raises(ValueError):
        MacBookConfiguration(
            model = "14-inch",
            chip = "M3",
            ram_gb=16,
            storage_gb=100,
            color="Space Gray",
            apple_care= True,
            engraving_text="mynameisanish"
        )
