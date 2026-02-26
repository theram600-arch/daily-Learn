# loops    Loops are programming constructs that repeat a specific set of instructions multiple times until a defined condition is met

# fruits=["apple","banana","cocunot","guava"]

# for i in fruits:
#     print(i)
#     if i=="banana":
#         break


# for i in range(3):
#     for j in range(2):
#         print(i, j)


# fruits=[(3,1),(5,6),(8,0)]

# for x in fruits:
#     print(f"{x=}and {y=}")



# i=0
# while i <len(numbers):
#     print(numbers[i])
#     i+=1


# fruits = ["orange", "apple", "mango", "lemon"]

# for i in range(len(fruits)):
#     fruit=fruits[i]
#     print(i,fruit)


# t=0
# u=0
# for i in range(1,101):
#     if i%2==0:
#         u=u+i
#         print(u)
# for j in range(0,101):
#     if j%2!=0:
#         t=t+j
#         print(j)



# even_sum = 0
# odd_sum = 0

# for i in range(0, 101):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print("Sum of even numbers =", even_sum)
# print("Sum of odd numbers =", odd_sum)




# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cabo Verde',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombia',
#   'Comoros',
#   'Congo, Democratic Republic of the',
#   'Congo, Republic of the',
#   'Costa Rica',
#   "Côte d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor-Leste)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Eswatini',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Montenegro',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'North Macedonia',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Palestine',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent and the Grenadines',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'South Sudan',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe'
# ]

# for i in countries:
#     if i.endswith("land"):
#         print(i)
        



# fruits=['banana', 'orange', 'mango', 'lemon']

# for i in reversed(fruits):
#     print(i)




                                                                        #    print vowels and alphabets from user input

# text=input("enter here: ")
# vowels="aeiouAEIOU"

# vowel_count=0
# alpha_count=0

# for i in text:
#     if i.isalpha():
#         if i in vowels:
#             vowel_count+=1
#         else:
#             alpha_count+=1

# print(f"vowels: {vowel_count}")
# print(f"alphabets: {alpha_count}")



#                                                             count upper case and lower case
# text= "Hello world"
# upperr=0
# lowerr=0
# for i in text:
#     if i.isupper():
#         upperr+=1
#     elif i.islower():
#         lowerr+=1
# print("uppercase: ",upperr)
# print("lowercase: ",lowerr)


                                                        #   count elements
# text=input("enter here: ")
# count=0
# for i in text:
#     count+=1
# print(count)

                                                        #  count spaces
# text = input("Enter a sentence: ")
# count=1
# for i in text:
#     if i==" ":
#         count+=1
# print("there are",count,"words")


                                            # find even and odd number 


# text=[1,2,3,4,5,6]
# even=[]
# odd=[]
# for i in text:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even", even)
# print("odd",odd)

