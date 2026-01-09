import requests
response = requests.get('http://20.91.198.208:8081/get')

parameters = {
    "token": "c5fcbc32"
}

response = requests.get(f'http://20.91.198.208:8081/get', params=parameters)

print(response.status_code)
print(response.headers)
print(response.text)

#X-Secret-key = 'sZPSiR6xgy33NJ6udXavhBlK_4k-KCh6aqjLTPlpFxQ=' 
#encrypted text = gAAAAABpYLwwrvOG4eZMZeBWccM9l8SMtZ8sBzYPkXD-WNqbN1wscVKpSUjAI1uqaoZEqsfCteFi6jgQiohBrsmVXr4BR1D9YCMFWuOW_-L3qkUmrIEFAFa10esB0s06ROwFbWqqOac6Q4a0Zyl31WqGadQrizrVAgVO4KZbov5-HQPADe5uuCzsdve1sW-GQ-lz9qkoX1w79WtT0ruBhvtcvESqNFP19b3UnXi1UKIZjmYqozspvG-93VuHuROsUDUv8wxRHBl5qcL9sg4rI3haK2RU_sGm1ZA6sY_FQyv2of3OVjXDDcwoadG5oK-w-FcOfhJup4HrsVSM1JqK8PawCNblwZ0VcVonct01czgvgIgTP5C41vq2HGr_h_K5a1Bcmg7n1tKqM19vgq7sSQfdi-v_rbwfkhqXdbGhKfQ-P0505ahRqg6K3eoEKz9fvdm8uUQ6LaS0YjNYgElOT4c_amOAc5-fhpRtqakTp8nBTv8zPQtJ2ck=