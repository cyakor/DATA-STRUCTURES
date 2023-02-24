#Index number- 6949821
# https://github.com/cyakor/DATA-STRUCTURES
print('Welcome to BeSpoke exotic cars')
carBrand = input("Please enter the car brand prefered:  \n")
carName = input('Please input the name of the car with the year of release:  \n\n')
car={'BMW M2 2022':'$110,000.00', 'BMW M3 2022':'$100,000.00', 'BMW M4 2022':'$150,000.00', 'Mercedes Maybach 2020':'$250,000.00'\
       ,'Mercedes Maybach 2022':'$300,000.00', 'Mercedes Benz gt63':'$250,000.00', 'Meercedes Benz amg gt 2019':'$350,000.00',\
            'Mercedes Benz g63 2022':'$400,000.00', 'BMW M8 2022':'$255,000.00', 'Mercedes Benz glc 300 2020':'$155,000.00', \
                'Cadillac CT5-V 2021':'$245,000.00', 'Toyota corolla 2022':'$75,000.00', 'Honda civic 2022':'$50,000.00', 'Mercedes Benz c300 2018':'$80,000.00', \
                    'Honda accord 2022':'$55,000.00', 'Ferarri 812 competizione 2022':'$300,000.00', 'Range Rover Velar 2020':'$100,000.00', 'Range Rover 2022 Bespoke edition':'$500,000.00', \
                        'Mercedes Maybach 2022 Bespoke edition':'$750,000.00', 'Mustang shelby 2022':'$175,000.00', 'Lamborghini Aventador 2022':'$750,000.00', 'Mercedes Benz gt63 YC edition':'$400,000.00', \
                            'Tesla model s plaid 2022':'$120,000.00', 'Toyota Land Cruiser v8 2022':'$125,000.00', 'Range Rover YC Bespoke 2023':'$600,000.00', 'Mercedes Benz amg gt coupe 2023':'$350,000.00', 'Porshe 911 carerra s 2020':'$290,000.00', \
                                'Audi A8 2022':'$170,000.00', 'Audi A4 2022':'$155,500.00', 'Rolls Royce Phantom 2022':'$350,000.00', 'Rolls Royce Ghost':'$500,000.00', 'Rolls Royce YC edition 2023':'$700,000.00', 'Chevy Camaro 2022':'$125,000.00'}
carPrice = car[carName]
print('The {} cost {}'.format(carName,carPrice))
answer=input("Are you ready to make payment now? Yes/No'   \n\n")
if answer is str('Yes'):
    input('Would you make payment in cash, card or by momo?   \n\n')
else:
    print('WBHBYD')