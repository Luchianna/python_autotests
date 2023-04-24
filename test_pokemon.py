import requests
import pytest

def test_status_code():
    token = '338f0f1f914339cd9207f6b30f457963'
    response = requests.get('https://pokemonbattle.me:9104/trainers', headers={'trainer_token' : token}, json={
        "trainer_id": "4126",
})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 4126})
    response_body = response.text
    assert response.json()['trainer_name'] == 'Нафаня'
