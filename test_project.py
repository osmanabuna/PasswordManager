import os
import pytest
import tempfile
from project import (
    new_vault,
    add_new_password,
    remove_password,
    update_password,
)
def test_new_vault():
    vault_name = 'test_vault'
    vault_path = os.path.join('PasswordCSV', f"{vault_name}.csv")
    # Ensure the vault doesn't exist initially
    if os.path.isfile(vault_path):
        os.remove(vault_path)
    # Create a new vault successfully
    new_vault(vault_name)
    assert os.path.isfile(vault_path)
    # Try to create the same vault again and expect an OSError
    with pytest.raises(OSError):
        new_vault(vault_name)

def test_add_new_password_correct():
    vault_name = 'test_vault.csv'
    website_name = "Example.com"
    password = "123456"
    assert add_new_password(website_name, password, vault_name) == True

def test_add_new_password_wrong():
    vault_name = 'test_vault.csv'
    website_name = "Example.com"
    password = "123456"
    assert add_new_password(website_name, password, vault_name) == False

def test_update_password_correct():
    vault_name = 'test_vault.csv'
    assert update_password(1, vault_name, '445566') == True

def test_update_password_wrong():
    vault_name = 'test_vault.csv'
    assert update_password(0, vault_name, '445566') == False

def test_update_password_correct():
    vault_name = 'test_vault.csv'
    assert update_password(1, vault_name, '445566') == True



def test_remove_password_correct():
    vault_name = 'test_vault.csv'
    assert remove_password(1, vault_name) == True

def test_remove_password_wrong():
    vault_name = 'test_vault.csv'
    assert remove_password(1, vault_name) == False
