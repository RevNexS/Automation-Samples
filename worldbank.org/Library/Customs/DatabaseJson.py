class JsonData:
    # This is Countries Data from MasterDb_AMS_Funding and 
    # Read ISO 3166 country code on wikipedia to more about country code.
    countryTable = [
        {# MasterDb_AMS_Funding table Below till next sections 
            "id": 1,
            "Country": "AFGHANISTAN",
            "Code": "AF",
            "Geo_Id": "1033"
        },
        {
            "id": 2,
            "Country": "LAND ISLANDS",
            "Code": "AX",
            "Geo_Id": "1042"
        },
        {
            "id": 3,
            "Country": "ALBANIA",
            "Code": "AL",
            "Geo_Id": "1043"
        },
        {
            "id": 4,
            "Country": "ALGERIA",
            "Code": "DZ",
            "Geo_Id": "1013"
        },
        {
            "id": 5,
            "Country": "AMERICAN SAMOA",
            "Code": "AS",
            "Geo_Id": "1054"
        },
        {
            "id": 6,
            "Country": "ANDORRA",
            "Code": "AD",
            "Geo_Id": "1043"
        },
        {
            "id": 7,
            "Country": "ANGOLA",
            "Code": "AO",
            "Geo_Id": "1012"
        },
        {
            "id": 8,
            "Country": "ANGUILLA",
            "Code": "AI",
            "Geo_Id": "1022"
        },
        {
            "id": 9,
            "Country": "ANTARCTICA",
            "Code": "AQ",
            "Geo_Id": "0"
        },
        {
            "id": 10,
            "Country": "ANTIGUA AND BARBUDA",
            "Code": "AG",
            "Geo_Id": "1022"
        },
        {
            "id": 11,
            "Country": "ARGENTINA",
            "Code": "AR",
            "Geo_Id": "1024"
        },
        {
            "id": 12,
            "Country": "ARMENIA",
            "Code": "AM",
            "Geo_Id": "1035"
        },
        {
            "id": 13,
            "Country": "ARUBA",
            "Code": "AW",
            "Geo_Id": "1022"
        },
        {
            "id": 14,
            "Country": "AUSTRALIA",
            "Code": "AU",
            "Geo_Id": "1051"
        },
        {
            "id": 15,
            "Country": "AUSTRIA",
            "Code": "AT",
            "Geo_Id": "1044"
        },
        {
            "id": 16,
            "Country": "AZERBAIJAN",
            "Code": "AZ",
            "Geo_Id": "1035"
        },
        {
            "id": 17,
            "Country": "BAHAMAS",
            "Code": "BS",
            "Geo_Id": "1022"
        },
        {
            "id": 18,
            "Country": "BAHRAIN",
            "Code": "BH",
            "Geo_Id": "1035"
        },
        {
            "id": 19,
            "Country": "BANGLADESH",
            "Code": "BD",
            "Geo_Id": "1033"
        },
        {
            "id": 20,
            "Country": "BARBADOS",
            "Code": "BB",
            "Geo_Id": "1022"
        },
        {
            "id": 21,
            "Country": "BELARUS",
            "Code": "BY",
            "Geo_Id": "1041"
        },
        {
            "id": 22,
            "Country": "BELGIUM",
            "Code": "BE",
            "Geo_Id": "1044"
        },
        {
            "id": 23,
            "Country": "BELIZE",
            "Code": "BZ",
            "Geo_Id": "1021"
        },
        {
            "id": 24,
            "Country": "BENIN",
            "Code": "BJ",
            "Geo_Id": "1015"
        },
        {
            "id": 25,
            "Country": "BERMUDA",
            "Code": "BM",
            "Geo_Id": "1023"
        },
        {
            "id": 26,
            "Country": "BHUTAN",
            "Code": "BT",
            "Geo_Id": "1033"
        },
        {
            "id": 27,
            "Country": "BOLIVIA, PLURINATIONAL STATE OF",
            "Code": "BO",
            "Geo_Id": "1024"
        },
        {
            "id": 28,
            "Country": "BONAIRE, SAINT EUSTATIUS AND SABA",
            "Code": "BQ",
            "Geo_Id": "1022"
        },
        {
            "id": 29,
            "Country": "BOSNIA AND HERZEGOVINA",
            "Code": "BA",
            "Geo_Id": "1043"
        },
        {
            "id": 30,
            "Country": "BOTSWANA",
            "Code": "BW",
            "Geo_Id": "1014"
        },
        {
            "id": 31,
            "Country": "BOUVET ISLAND",
            "Code": "BV",
            "Geo_Id": "1042"
        },
        {
            "id": 32,
            "Country": "BRAZIL",
            "Code": "BR",
            "Geo_Id": "1024"
        },
        {
            "id": 33,
            "Country": "BRITISH INDIAN OCEAN TERRITORY",
            "Code": "IO",
            "Geo_Id": "1022"
        },
        {
            "id": 34,
            "Country": "BRUNEI DARUSSALAM",
            "Code": "BN",
            "Geo_Id": "1034"
        },
        {
            "id": 35,
            "Country": "BULGARIA",
            "Code": "BG",
            "Geo_Id": "1041"
        },
        {
            "id": 36,
            "Country": "BURKINA FASO",
            "Code": "BF",
            "Geo_Id": "1015"
        },
        {
            "id": 37,
            "Country": "BURUNDI",
            "Code": "BI",
            "Geo_Id": "1011"
        },
        {
            "id": 38,
            "Country": "CAMBODIA",
            "Code": "KH",
            "Geo_Id": "1034"
        },
        {
            "id": 39,
            "Country": "CAMEROON",
            "Code": "CM",
            "Geo_Id": "1012"
        },
        {
            "id": 40,
            "Country": "CANADA",
            "Code": "CA",
            "Geo_Id": "1023"
        },
        {
            "id": 41,
            "Country": "CAPE VERDE",
            "Code": "CV",
            "Geo_Id": "1015"
        },
        {
            "id": 42,
            "Country": "CAYMAN ISLANDS",
            "Code": "KY",
            "Geo_Id": "1022"
        },
        {
            "id": 43,
            "Country": "CENTRAL AFRICAN REPUBLIC",
            "Code": "CF",
            "Geo_Id": "1012"
        },
        {
            "id": 44,
            "Country": "CHAD",
            "Code": "TD",
            "Geo_Id": "1012"
        },
        {
            "id": 45,
            "Country": "CHILE",
            "Code": "CL",
            "Geo_Id": "1024"
        },
        {
            "id": 46,
            "Country": "CHINA",
            "Code": "CN",
            "Geo_Id": "1032"
        },
        {
            "id": 47,
            "Country": "CHRISTMAS ISLAND",
            "Code": "CX",
            "Geo_Id": "1042"
        },
        {
            "id": 48,
            "Country": "COCOS (KEELING) ISLANDS",
            "Code": "CC",
            "Geo_Id": "1051"
        },
        {
            "id": 49,
            "Country": "COLOMBIA",
            "Code": "CO",
            "Geo_Id": "1024"
        },
        {
            "id": 50,
            "Country": "COMOROS",
            "Code": "KM",
            "Geo_Id": "1011"
        },
        {
            "id": 51,
            "Country": "CONGO",
            "Code": "CG",
            "Geo_Id": "1012"
        },
        {
            "id": 52,
            "Country": "CONGO, THE DEMOCRATIC REPUBLIC OF THE",
            "Code": "CD",
            "Geo_Id": "1012"
        },
        {
            "id": 53,
            "Country": "COOK ISLANDS",
            "Code": "CK",
            "Geo_Id": "1054"
        },
        {
            "id": 54,
            "Country": "COSTA RICA",
            "Code": "CR",
            "Geo_Id": "1021"
        },
        {
            "id": 55,
            "Country": "C?TE D\\'IVOIRE",
            "Code": "CI",
            "Geo_Id": "1015"
        },
        {
            "id": 56,
            "Country": "CROATIA",
            "Code": "HR",
            "Geo_Id": "1043"
        },
        {
            "id": 57,
            "Country": "CUBA",
            "Code": "CU",
            "Geo_Id": "1022"
        },
        {
            "id": 58,
            "Country": "CURACAO",
            "Code": "CW",
            "Geo_Id": "1022"
        },
        {
            "id": 59,
            "Country": "CYPRUS",
            "Code": "CY",
            "Geo_Id": "1035"
        },
        {
            "id": 60,
            "Country": "CZECH REPUBLIC",
            "Code": "CZ",
            "Geo_Id": "1041"
        },
        {
            "id": 61,
            "Country": "DENMARK",
            "Code": "DK",
            "Geo_Id": "1042"
        },
        {
            "id": 62,
            "Country": "DJIBOUTI",
            "Code": "DJ",
            "Geo_Id": "1011"
        },
        {
            "id": 63,
            "Country": "DOMINICA",
            "Code": "DM",
            "Geo_Id": "1022"
        },
        {
            "id": 64,
            "Country": "DOMINICAN REPUBLIC",
            "Code": "DO",
            "Geo_Id": "1022"
        },
        {
            "id": 65,
            "Country": "ECUADOR",
            "Code": "EC",
            "Geo_Id": "1024"
        },
        {
            "id": 66,
            "Country": "EGYPT",
            "Code": "EG",
            "Geo_Id": "1013"
        },
        {
            "id": 67,
            "Country": "EL SALVADOR",
            "Code": "SV",
            "Geo_Id": "1021"
        },
        {
            "id": 68,
            "Country": "EQUATORIAL GUINEA",
            "Code": "GQ",
            "Geo_Id": "1012"
        },
        {
            "id": 69,
            "Country": "ERITREA",
            "Code": "ER",
            "Geo_Id": "1011"
        },
        {
            "id": 70,
            "Country": "ESTONIA",
            "Code": "EE",
            "Geo_Id": "1042"
        },
        {
            "id": 71,
            "Country": "ETHIOPIA",
            "Code": "ET",
            "Geo_Id": "1011"
        },
        {
            "id": 72,
            "Country": "FALKLAND ISLANDS (MALVINAS)",
            "Code": "FK",
            "Geo_Id": "1024"
        },
        {
            "id": 73,
            "Country": "FAROE ISLANDS",
            "Code": "FO",
            "Geo_Id": "1042"
        },
        {
            "id": 74,
            "Country": "FIJI",
            "Code": "FJ",
            "Geo_Id": "1052"
        },
        {
            "id": 75,
            "Country": "FINLAND",
            "Code": "FI",
            "Geo_Id": "1042"
        },
        {
            "id": 76,
            "Country": "FRANCE",
            "Code": "FR",
            "Geo_Id": "1044"
        },
        {
            "id": 77,
            "Country": "FRENCH GUIANA",
            "Code": "GF",
            "Geo_Id": "1024"
        },
        {
            "id": 78,
            "Country": "FRENCH POLYNESIA",
            "Code": "PF",
            "Geo_Id": "1054"
        },
        {
            "id": 79,
            "Country": "FRENCH SOUTHERN TERRITORIES",
            "Code": "TF",
            "Geo_Id": "1044"
        },
        {
            "id": 80,
            "Country": "GABON",
            "Code": "GA",
            "Geo_Id": "1012"
        },
        {
            "id": 81,
            "Country": "GAMBIA",
            "Code": "GM",
            "Geo_Id": "1015"
        },
        {
            "id": 82,
            "Country": "GEORGIA",
            "Code": "GE",
            "Geo_Id": "1035"
        },
        {
            "id": 83,
            "Country": "GERMANY",
            "Code": "DE",
            "Geo_Id": "1044"
        },
        {
            "id": 84,
            "Country": "GHANA",
            "Code": "GH",
            "Geo_Id": "1015"
        },
        {
            "id": 85,
            "Country": "GIBRALTAR",
            "Code": "GI",
            "Geo_Id": "1043"
        },
        {
            "id": 86,
            "Country": "GREECE",
            "Code": "GR",
            "Geo_Id": "1043"
        },
        {
            "id": 87,
            "Country": "GREENLAND",
            "Code": "GL",
            "Geo_Id": "1023"
        },
        {
            "id": 88,
            "Country": "GRENADA",
            "Code": "GD",
            "Geo_Id": "1022"
        },
        {
            "id": 89,
            "Country": "GUADELOUPE",
            "Code": "GP",
            "Geo_Id": "1022"
        },
        {
            "id": 90,
            "Country": "GUAM",
            "Code": "GU",
            "Geo_Id": "1053"
        },
        {
            "id": 91,
            "Country": "GUATEMALA",
            "Code": "GT",
            "Geo_Id": "1021"
        },
        {
            "id": 92,
            "Country": "GUERNSEY",
            "Code": "GG",
            "Geo_Id": "1042"
        },
        {
            "id": 93,
            "Country": "GUINEA",
            "Code": "GN",
            "Geo_Id": "1015"
        },
        {
            "id": 94,
            "Country": "GUINEA-BISSAU",
            "Code": "GW",
            "Geo_Id": "1015"
        },
        {
            "id": 95,
            "Country": "GUYANA",
            "Code": "GY",
            "Geo_Id": "1024"
        },
        {
            "id": 96,
            "Country": "HAITI",
            "Code": "HT",
            "Geo_Id": "1022"
        },
        {
            "id": 97,
            "Country": "HEARD ISLAND AND MCDONALD ISLANDS",
            "Code": "HM",
            "Geo_Id": "1051"
        },
        {
            "id": 98,
            "Country": "HOLY SEE (VATICAN CITY STATE)",
            "Code": "VA",
            "Geo_Id": "1043"
        },
        {
            "id": 99,
            "Country": "HONDURAS",
            "Code": "HN",
            "Geo_Id": "1021"
        },
        {
            "id": 100,
            "Country": "HONG KONG",
            "Code": "HK",
            "Geo_Id": "1032"
        },
        {
            "id": 101,
            "Country": "HUNGARY",
            "Code": "HU",
            "Geo_Id": "1041"
        },
        {
            "id": 102,
            "Country": "ICELAND",
            "Code": "IS",
            "Geo_Id": "1042"
        },
        {
            "id": 103,
            "Country": "INDIA",
            "Code": "IN",
            "Geo_Id": "1033"
        },
        {
            "id": 104,
            "Country": "INDONESIA",
            "Code": "ID",
            "Geo_Id": "1034"
        },
        {
            "id": 105,
            "Country": "IRAN, ISLAMIC REPUBLIC OF",
            "Code": "IR",
            "Geo_Id": "1033"
        },
        {
            "id": 106,
            "Country": "IRAQ",
            "Code": "IQ",
            "Geo_Id": "1035"
        },
        {
            "id": 107,
            "Country": "IRELAND",
            "Code": "IE",
            "Geo_Id": "1042"
        },
        {
            "id": 108,
            "Country": "ISLE OF MAN",
            "Code": "IM",
            "Geo_Id": "1042"
        },
        {
            "id": 109,
            "Country": "ISRAEL",
            "Code": "IL",
            "Geo_Id": "1035"
        },
        {
            "id": 110,
            "Country": "ITALY",
            "Code": "IT",
            "Geo_Id": "1043"
        },
        {
            "id": 111,
            "Country": "JAMAICA",
            "Code": "JM",
            "Geo_Id": "1022"
        },
        {
            "id": 112,
            "Country": "JAPAN",
            "Code": "JP",
            "Geo_Id": "1032"
        },
        {
            "id": 113,
            "Country": "JERSEY",
            "Code": "JE",
            "Geo_Id": "1042"
        },
        {
            "id": 114,
            "Country": "JORDAN",
            "Code": "JO",
            "Geo_Id": "1035"
        },
        {
            "id": 115,
            "Country": "KAZAKHSTAN",
            "Code": "KZ",
            "Geo_Id": "1031"
        },
        {
            "id": 116,
            "Country": "KENYA",
            "Code": "KE",
            "Geo_Id": "1011"
        },
        {
            "id": 117,
            "Country": "KIRIBATI",
            "Code": "KI",
            "Geo_Id": "1053"
        },
        {
            "id": 118,
            "Country": "KOREA, DEMOCRATIC PEOPLE\\'S REPUBLIC OF(North Korea)",
            "Code": "KP",
            "Geo_Id": "1032"
        },
        {
            "id": 119,
            "Country": "KOREA, REPUBLIC OF(South Korea)",
            "Code": "KR",
            "Geo_Id": "1032"
        },
        {
            "id": 120,
            "Country": "KUWAIT",
            "Code": "KW",
            "Geo_Id": "1035"
        },
        {
            "id": 121,
            "Country": "KYRGYZSTAN",
            "Code": "KG",
            "Geo_Id": "1031"
        },
        {
            "id": 122,
            "Country": "LAO PEOPLE\\'S DEMOCRATIC REPUBLIC",
            "Code": "LA",
            "Geo_Id": "1034"
        },
        {
            "id": 123,
            "Country": "LATVIA",
            "Code": "LV",
            "Geo_Id": "1042"
        },
        {
            "id": 124,
            "Country": "LEBANON",
            "Code": "LB",
            "Geo_Id": "1035"
        },
        {
            "id": 125,
            "Country": "LESOTHO",
            "Code": "LS",
            "Geo_Id": "1014"
        },
        {
            "id": 126,
            "Country": "LIBERIA",
            "Code": "LR",
            "Geo_Id": "1015"
        },
        {
            "id": 127,
            "Country": "LIBYAN ARAB JAMAHIRIYA",
            "Code": "LY",
            "Geo_Id": "1013"
        },
        {
            "id": 128,
            "Country": "LIECHTENSTEIN",
            "Code": "LI",
            "Geo_Id": "1044"
        },
        {
            "id": 129,
            "Country": "LITHUANIA",
            "Code": "LT",
            "Geo_Id": "1042"
        },
        {
            "id": 130,
            "Country": "LUXEMBOURG",
            "Code": "LU",
            "Geo_Id": "1044"
        },
        {
            "id": 131,
            "Country": "MACAO",
            "Code": "MO",
            "Geo_Id": "1032"
        },
        {
            "id": 132,
            "Country": "MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
            "Code": "MK",
            "Geo_Id": "1043"
        },
        {
            "id": 133,
            "Country": "MADAGASCAR",
            "Code": "MG",
            "Geo_Id": "1011"
        },
        {
            "id": 134,
            "Country": "MALAWI",
            "Code": "MW",
            "Geo_Id": "1011"
        },
        {
            "id": 135,
            "Country": "MALAYSIA",
            "Code": "MY",
            "Geo_Id": "1034"
        },
        {
            "id": 136,
            "Country": "MALDIVES",
            "Code": "MV",
            "Geo_Id": "1033"
        },
        {
            "id": 137,
            "Country": "MALI",
            "Code": "ML",
            "Geo_Id": "1015"
        },
        {
            "id": 138,
            "Country": "MALTA",
            "Code": "MT",
            "Geo_Id": "1043"
        },
        {
            "id": 139,
            "Country": "MARSHALL ISLANDS",
            "Code": "MH",
            "Geo_Id": "1053"
        },
        {
            "id": 140,
            "Country": "MARTINIQUE",
            "Code": "MQ",
            "Geo_Id": "1022"
        },
        {
            "id": 141,
            "Country": "MAURITANIA",
            "Code": "MR",
            "Geo_Id": "1015"
        },
        {
            "id": 142,
            "Country": "MAURITIUS",
            "Code": "MU",
            "Geo_Id": "1011"
        },
        {
            "id": 143,
            "Country": "MAYOTTE",
            "Code": "YT",
            "Geo_Id": "1011"
        },
        {
            "id": 144,
            "Country": "MEXICO",
            "Code": "MX",
            "Geo_Id": "1021"
        },
        {
            "id": 145,
            "Country": "MICRONESIA, FEDERATED STATES OF",
            "Code": "FM",
            "Geo_Id": "1053"
        },
        {
            "id": 146,
            "Country": "MOLDOVA, REPUBLIC OF",
            "Code": "MD",
            "Geo_Id": "1041"
        },
        {
            "id": 147,
            "Country": "MONACO",
            "Code": "MC",
            "Geo_Id": "1044"
        },
        {
            "id": 148,
            "Country": "MONGOLIA",
            "Code": "MN",
            "Geo_Id": "1032"
        },
        {
            "id": 149,
            "Country": "MONTENEGRO",
            "Code": "ME",
            "Geo_Id": "1043"
        },
        {
            "id": 150,
            "Country": "MONTSERRAT",
            "Code": "MS",
            "Geo_Id": "1022"
        },
        {
            "id": 151,
            "Country": "MOROCCO",
            "Code": "MA",
            "Geo_Id": "1013"
        },
        {
            "id": 152,
            "Country": "MOZAMBIQUE",
            "Code": "MZ",
            "Geo_Id": "1011"
        },
        {
            "id": 153,
            "Country": "MYANMAR",
            "Code": "MM",
            "Geo_Id": "1034"
        },
        {
            "id": 154,
            "Country": "NAMIBIA",
            "Code": "NA",
            "Geo_Id": "1014"
        },
        {
            "id": 155,
            "Country": "NAURU",
            "Code": "NR",
            "Geo_Id": "1053"
        },
        {
            "id": 156,
            "Country": "NEPAL",
            "Code": "NP",
            "Geo_Id": "1033"
        },
        {
            "id": 157,
            "Country": "NETHERLANDS",
            "Code": "NL",
            "Geo_Id": "1044"
        },
        {
            "id": 158,
            "Country": "NEW CALEDONIA",
            "Code": "NC",
            "Geo_Id": "1052"
        },
        {
            "id": 159,
            "Country": "NEW ZEALAND",
            "Code": "NZ",
            "Geo_Id": "1051"
        },
        {
            "id": 160,
            "Country": "NICARAGUA",
            "Code": "NI",
            "Geo_Id": "1021"
        },
        {
            "id": 161,
            "Country": "NIGER",
            "Code": "NE",
            "Geo_Id": "1015"
        },
        {
            "id": 162,
            "Country": "NIGERIA",
            "Code": "NG",
            "Geo_Id": "1015"
        },
        {
            "id": 163,
            "Country": "NIUE",
            "Code": "NU",
            "Geo_Id": "1054"
        },
        {
            "id": 164,
            "Country": "NORFOLK ISLAND",
            "Code": "NF",
            "Geo_Id": "1051"
        },
        {
            "id": 165,
            "Country": "NORTHERN MARIANA ISLANDS",
            "Code": "MP",
            "Geo_Id": "1053"
        },
        {
            "id": 166,
            "Country": "NORWAY",
            "Code": "NO",
            "Geo_Id": "1042"
        },
        {
            "id": 167,
            "Country": "OMAN",
            "Code": "OM",
            "Geo_Id": "1035"
        },
        {
            "id": 168,
            "Country": "PAKISTAN",
            "Code": "PK",
            "Geo_Id": "1033"
        },
        {
            "id": 169,
            "Country": "PALAU",
            "Code": "PW",
            "Geo_Id": "1053"
        },
        {
            "id": 170,
            "Country": "PALESTINIAN TERRITORY, OCCUPIED",
            "Code": "PS",
            "Geo_Id": "1035"
        },
        {
            "id": 171,
            "Country": "PANAMA",
            "Code": "PA",
            "Geo_Id": "1021"
        },
        {
            "id": 172,
            "Country": "PAPUA NEW GUINEA",
            "Code": "PG",
            "Geo_Id": "1052"
        },
        {
            "id": 173,
            "Country": "PARAGUAY",
            "Code": "PY",
            "Geo_Id": "1024"
        },
        {
            "id": 174,
            "Country": "PERU",
            "Code": "PE",
            "Geo_Id": "1024"
        },
        {
            "id": 175,
            "Country": "PHILIPPINES",
            "Code": "PH",
            "Geo_Id": "1034"
        },
        {
            "id": 176,
            "Country": "PITCAIRN",
            "Code": "PN",
            "Geo_Id": "1054"
        },
        {
            "id": 177,
            "Country": "POLAND",
            "Code": "PL",
            "Geo_Id": "1041"
        },
        {
            "id": 178,
            "Country": "PORTUGAL",
            "Code": "PT",
            "Geo_Id": "1043"
        },
        {
            "id": 179,
            "Country": "PUERTO RICO",
            "Code": "PR",
            "Geo_Id": "1022"
        },
        {
            "id": 180,
            "Country": "QATAR",
            "Code": "QA",
            "Geo_Id": "1035"
        },
        {
            "id": 181,
            "Country": "R?UNION",
            "Code": "RE",
            "Geo_Id": "1011"
        },
        {
            "id": 182,
            "Country": "ROMANIA",
            "Code": "RO",
            "Geo_Id": "1041"
        },
        {
            "id": 183,
            "Country": "RUSSIAN FEDERATION",
            "Code": "RU",
            "Geo_Id": "1041"
        },
        {
            "id": 184,
            "Country": "RWANDA",
            "Code": "RW",
            "Geo_Id": "1011"
        },
        {
            "id": 185,
            "Country": "SAINT BARTH?LEMY",
            "Code": "BL",
            "Geo_Id": "1022"
        },
        {
            "id": 186,
            "Country": "SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
            "Code": "SH",
            "Geo_Id": "1015"
        },
        {
            "id": 187,
            "Country": "SAINT KITTS AND NEVIS",
            "Code": "KN",
            "Geo_Id": "1022"
        },
        {
            "id": 188,
            "Country": "SAINT LUCIA",
            "Code": "LC",
            "Geo_Id": "1022"
        },
        {
            "id": 189,
            "Country": "SAINT MARTIN (FRENCH PART)",
            "Code": "MF",
            "Geo_Id": "1022"
        },
        {
            "id": 190,
            "Country": "SAINT PIERRE AND MIQUELON",
            "Code": "PM",
            "Geo_Id": "1023"
        },
        {
            "id": 191,
            "Country": "SAINT VINCENT AND THE GRENADINES",
            "Code": "VC",
            "Geo_Id": "1022"
        },
        {
            "id": 192,
            "Country": "SAMOA",
            "Code": "WS",
            "Geo_Id": "1054"
        },
        {
            "id": 193,
            "Country": "SAN MARINO",
            "Code": "SM",
            "Geo_Id": "1043"
        },
        {
            "id": 194,
            "Country": "SAO TOME AND PRINCIPE",
            "Code": "ST",
            "Geo_Id": "1012"
        },
        {
            "id": 195,
            "Country": "SAUDI ARABIA",
            "Code": "SA",
            "Geo_Id": "1035"
        },
        {
            "id": 196,
            "Country": "SENEGAL",
            "Code": "SN",
            "Geo_Id": "1015"
        },
        {
            "id": 197,
            "Country": "SERBIA",
            "Code": "RS",
            "Geo_Id": "1043"
        },
        {
            "id": 198,
            "Country": "SEYCHELLES",
            "Code": "SC",
            "Geo_Id": "1011"
        },
        {
            "id": 199,
            "Country": "SIERRA LEONE",
            "Code": "SL",
            "Geo_Id": "1015"
        },
        {
            "id": 200,
            "Country": "SINGAPORE",
            "Code": "SG",
            "Geo_Id": "1034"
        },
        {
            "id": 201,
            "Country": "SINT MAARTEN (DUTCH PART)",
            "Code": "SX",
            "Geo_Id": "1022"
        },
        {
            "id": 202,
            "Country": "SLOVAKIA",
            "Code": "SK",
            "Geo_Id": "1041"
        },
        {
            "id": 203,
            "Country": "SLOVENIA",
            "Code": "SI",
            "Geo_Id": "1043"
        },
        {
            "id": 204,
            "Country": "SOLOMON ISLANDS",
            "Code": "SB",
            "Geo_Id": "1052"
        },
        {
            "id": 205,
            "Country": "SOMALIA",
            "Code": "SO",
            "Geo_Id": "1011"
        },
        {
            "id": 206,
            "Country": "SOUTH AFRICA",
            "Code": "ZA",
            "Geo_Id": "1011"
        },
        {
            "id": 207,
            "Country": "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
            "Code": "GS",
            "Geo_Id": "1042"
        },
        {
            "id": 208,
            "Country": "SOUTH SUDAN",
            "Code": "SS",
            "Geo_Id": "1013"
        },
        {
            "id": 209,
            "Country": "SPAIN",
            "Code": "ES",
            "Geo_Id": "1043"
        },
        {
            "id": 210,
            "Country": "SRI LANKA",
            "Code": "LK",
            "Geo_Id": "1033"
        },
        {
            "id": 211,
            "Country": "SUDAN",
            "Code": "SD",
            "Geo_Id": "1013"
        },
        {
            "id": 212,
            "Country": "SURINAME",
            "Code": "SR",
            "Geo_Id": "1024"
        },
        {
            "id": 213,
            "Country": "SVALBARD AND JAN MAYEN",
            "Code": "SJ",
            "Geo_Id": "1042"
        },
        {
            "id": 214,
            "Country": "SWAZILAND",
            "Code": "SZ",
            "Geo_Id": "1014"
        },
        {
            "id": 215,
            "Country": "SWEDEN",
            "Code": "SE",
            "Geo_Id": "1042"
        },
        {
            "id": 216,
            "Country": "SWITZERLAND",
            "Code": "CH",
            "Geo_Id": "1044"
        },
        {
            "id": 217,
            "Country": "SYRIAN ARAB REPUBLIC",
            "Code": "SY",
            "Geo_Id": "1035"
        },
        {
            "id": 218,
            "Country": "TAIWAN, PROVINCE OF CHINA",
            "Code": "TW",
            "Geo_Id": "1032"
        },
        {
            "id": 219,
            "Country": "TAJIKISTAN",
            "Code": "TJ",
            "Geo_Id": "1031"
        },
        {
            "id": 220,
            "Country": "TANZANIA, UNITED REPUBLIC OF",
            "Code": "TZ",
            "Geo_Id": "1011"
        },
        {
            "id": 221,
            "Country": "THAILAND",
            "Code": "TH",
            "Geo_Id": "1034"
        },
        {
            "id": 222,
            "Country": "TIMOR-LESTE",
            "Code": "TL",
            "Geo_Id": "1034"
        },
        {
            "id": 223,
            "Country": "TOGO",
            "Code": "TG",
            "Geo_Id": "1015"
        },
        {
            "id": 224,
            "Country": "TOKELAU",
            "Code": "TK",
            "Geo_Id": "1054"
        },
        {
            "id": 225,
            "Country": "TONGA",
            "Code": "TO",
            "Geo_Id": "1054"
        },
        {
            "id": 226,
            "Country": "TRINIDAD AND TOBAGO",
            "Code": "TT",
            "Geo_Id": "1022"
        },
        {
            "id": 227,
            "Country": "TUNISIA",
            "Code": "TN",
            "Geo_Id": "1013"
        },
        {
            "id": 228,
            "Country": "TURKEY",
            "Code": "TR",
            "Geo_Id": "1035"
        },
        {
            "id": 229,
            "Country": "TURKMENISTAN",
            "Code": "TM",
            "Geo_Id": "1031"
        },
        {
            "id": 230,
            "Country": "TURKS AND CAICOS ISLANDS",
            "Code": "TC",
            "Geo_Id": "1022"
        },
        {
            "id": 231,
            "Country": "TUVALU",
            "Code": "TV",
            "Geo_Id": "1054"
        },
        {
            "id": 232,
            "Country": "UGANDA",
            "Code": "UG",
            "Geo_Id": "1011"
        },
        {
            "id": 233,
            "Country": "UKRAINE",
            "Code": "UA",
            "Geo_Id": "1041"
        },
        {
            "id": 234,
            "Country": "UNITED ARAB EMIRATES",
            "Code": "AE",
            "Geo_Id": "1035"
        },
        {
            "id": 235,
            "Country": "UNITED KINGDOM",
            "Code": "GB",
            "Geo_Id": "1042"
        },
        {
            "id": 236,
            "Country": "UNITED STATES",
            "Code": "US",
            "Geo_Id": "1023"
        },
        {
            "id": 237,
            "Country": "UNITED STATES MINOR OUTLYING ISLANDS",
            "Code": "UM",
            "Geo_Id": "1023"
        },
        {
            "id": 238,
            "Country": "URUGUAY",
            "Code": "UY",
            "Geo_Id": "1024"
        },
        {
            "id": 239,
            "Country": "UZBEKISTAN",
            "Code": "UZ",
            "Geo_Id": "1031"
        },
        {
            "id": 240,
            "Country": "VANUATU",
            "Code": "VU",
            "Geo_Id": "1052"
        },
        {
            "id": 241,
            "Country": "VENEZUELA, BOLIVARIAN REPUBLIC OF",
            "Code": "VE",
            "Geo_Id": "1024"
        },
        {
            "id": 242,
            "Country": "VIET NAM",
            "Code": "VN",
            "Geo_Id": "1034"
        },
        {
            "id": 243,
            "Country": "VIRGIN ISLANDS, BRITISH",
            "Code": "VG",
            "Geo_Id": "1042"
        },
        {
            "id": 244,
            "Country": "VIRGIN ISLANDS, U.S.",
            "Code": "VI",
            "Geo_Id": "1022"
        },
        {
            "id": 245,
            "Country": "WALLIS AND FUTUNA",
            "Code": "WF",
            "Geo_Id": "1054"
        },
        {
            "id": 246,
            "Country": "WESTERN SAHARA",
            "Code": "EH",
            "Geo_Id": "1013"
        },
        {
            "id": 247,
            "Country": "YEMEN",
            "Code": "YE",
            "Geo_Id": "1035"
        },
        {
            "id": 248,
            "Country": "ZAMBIA",
            "Code": "ZM",
            "Geo_Id": "1011"
        },
        {
            "id": 249,
            "Country": "ZIMBABWE",
            "Code": "ZW",
            "Geo_Id": "1011"
        },#Ungm specific below
        {   
            "id": '' ,
            "Country": "BOLIVIA",
            "Code": "BO",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "CÔTE D'IVOIRE",
            "Code": "CI",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "ESWATINI",
            "Code": "SZ",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "FALKLAND ISLANDS (MALVINAS) - A DISPUTE EXISTS BETWEEN THE ",
            "Code": "FK",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "GOVERNMENTS OF ARGENTINA AND THE UNITED KINGDOM OF GREAT ",
            "Code": "",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "BRITAIN AND NORTHERN IRELAND CONCERNING SOVEREIGNTY OVER THE ",
            "Code": "GB",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "FALKLAND ISLANDS (MALVINAS)",
            "Code": "FK",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "HONG KONG, SPECIAL ADMINISTRATIVE REGION OF CHINA",
            "Code": "HK",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
            "Code": "KP",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "KOREA, REPUBLIC OF",
            "Code": "KR",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "KOSOVO",
            "Code": "XK",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "LAO PEOPLE'S DEMOCRATIC REPUBLIC",
            "Code": "LA",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "MACAO, SPECIAL ADMINISTRATIVE REGION OF CHINA",
            "Code": "MO",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "NETHERLANDS ANTILLES",
            "Code": "",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "PALESTINE, STATE OF",
            "Code": "PS",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "REUNION",
            "Code": "RE",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "SAINT HELENA",
            "Code": "SH",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "SERBIA, REPUBLIC OF",
            "Code": "RS",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "TÜRKIYE",
            "Code": "TR",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "UNITED STATES OF AMERICA",
            "Code": "US",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "VENEZUELA",
            "Code": "VE",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "VIRGIN ISLANDS, U.  S.",
            "Code": "VI",
            "Geo_Id": ""
        },
        {   
            "id":'' ,
            "Country": "WALLIS AND FUTUNA ISLANDS",
            "Code": "WF",
            "Geo_Id": ""
        }
        ]
    # This is Org Data for Ungm
    financierDetails = [
        {
          "Abbreviation": "ADB",
          "ID": 13,
          "Org_Name": "Asian Development Bank (ADB)"
        },
        {
          "Abbreviation": "AFDB",
          "ID": 3,
          "Org_Name": "African Development Bank (AfDB)"
        },
        {
          "Abbreviation": "CTBTO",
          "ID": 93,
          "Org_Name": "Preparatory Commission for the Comprehensive Nuclear-Test-Ban Treaty Organization (CTBTO)"
        },
        {
          "Abbreviation": "ECLAC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ESCAP",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ESCWA",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "FAO",
          "ID": 48,
          "Org_Name": "Food And Agriculture Organisation (FAO)"
        },
        {
          "Abbreviation": "IAEA",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "IBRD",
          "ID": 60,
          "Org_Name": "International Bank for Reconstruction and Development (IBRD)"
        },
        {
          "Abbreviation": "ICAO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ICC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ICJ",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ICSID",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ICTP",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "IFAD",
          "ID": 65,
          "Org_Name": "International Fund for Agricultural Development (IFAD)"
        },
        {
          "Abbreviation": "IFC",
          "ID": 64,
          "Org_Name": "International Finance Corporation (IFC)"
        },
        {
          "Abbreviation": "ILO",
          "ID": 66,
          "Org_Name": "International Labor Organization (ILO)"
        },
        {
          "Abbreviation": "IMF",
          "ID": 67,
          "Org_Name": "International Monetary Fund (IMF)"
        },
        {
          "Abbreviation": "IMO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "IOM",
          "ID": 68,
          "Org_Name": "International Organization for Migration (IMO)"
        },
        {
          "Abbreviation": "ISA",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ITC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ITC-ILO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ITLOS",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "ITU",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "OHCHR",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "OPCW",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "PAHO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "STL",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN Auditors",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN Global Compact",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN Secretariat",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN-Habitat",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN-ICTR",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN-ICTY/MICT",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UN-Women",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNAIDS",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNAKRT",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNCCD",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNCDF",
          "ID": 107,
          "Org_Name": "United Nations Capital Development Fund (UNCDF)"
        },
        {
          "Abbreviation": "UNCTAD",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNDG",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNDP",
          "ID": 109,
          "Org_Name": "United Nations Development Programme (UNDP)"
        },
        {
          "Abbreviation": "UNECA",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNECE",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNEP",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNESCO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNFCCC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNFPA",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNHCR",
          "ID": 110,
          "Org_Name": "United Nations High Commissioner for Refugees (UNHCR)"
        },
        {
          "Abbreviation": "UNICC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNICEF",
          "ID": 108,
          "Org_Name": "United Nations Childrens Fund (UNICEF)"
        },
        {
          "Abbreviation": "UNICRI",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNIDIR",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNIDO",
          "ID": 111,
          "Org_Name": "United Nations Industrial Development Organization (UNIDO)"
        },
        {
          "Abbreviation": "UNIFEM",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNITAR",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNLIREC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNOCA",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNODC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNOG",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNON",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNOPS",
          "ID": 113,
          "Org_Name": "United Nations Office for Project Services (UNOPS)"
        },
        {
          "Abbreviation": "UNOV",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNRCO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNRISD",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNRWA",
          "ID": 115,
          "Org_Name": "United Nations Relief and Works Agency for Palestine Refugees in the Near East (UNRWA)"
        },
        {
          "Abbreviation": "UNSSC",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNTSO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNU",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNV",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UNWTO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "UPU",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "WBG",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "WFP",
          "ID": 120,
          "Org_Name": "World Food Organisation (WFP)"
        },
        {
          "Abbreviation": "WHO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "WIPO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "WMO",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "WMU",
          "ID": 116,
          "Org_Name": "United Nations System"
        },
        {
          "Abbreviation": "WTO",
          "ID": 121,
          "Org_Name": "World Trade Organization (WTO)"
        }
        ]

    @staticmethod
    def isInCountryTable(CountryName:str = None,Code:str = None,AcceptNone: bool = False, *args, **kwargs):
        '''Take country name and return value country code.
        Or checks if that country is there. if not then return empty string.
        * Dont pass None as a string like 'None'
        * use AcceptNone = True, when no value(None) is find and you want function to return ''.
        '''

        if CountryName is not None:
            CountryName = CountryName.upper()
            countryRow = next((subDict for subDict in JsonData.countryTable if subDict['Country'] == CountryName), None)
            ID = '' if countryRow == None else countryRow['id']
            Country = '' if countryRow == None else countryRow['Country']
            Country_code = '' if countryRow == None else countryRow['Code']
            Geo_ID = '' if countryRow == None else countryRow['Geo_Id']

            return ID, Country, Country_code, Geo_ID
        
        if Code is not None:
            Code = Code.upper()
            countryRow = next((subDict for subDict in JsonData.countryTable if subDict['Code'] == Code), None)
            ID = '' if countryRow == None else countryRow['id']
            Country = '' if countryRow == None else countryRow['Country']
            Country_code = '' if countryRow == None else countryRow['Code']
            Geo_ID = '' if countryRow == None else countryRow['Geo_Id']

            return ID, Country, Country_code, Geo_ID

        if AcceptNone == True and CountryName is None and Code is None:
            ID = ''
            Country = ''
            Country_code = ''
            Geo_ID = ''

            return ID, Country, Country_code, Geo_ID

    @staticmethod
    def getOrgDetails(Abbreviation):
        Abbreviation = str(Abbreviation)
        res = next((subDict for subDict in JsonData.financierDetails if subDict['Abbreviation'] == Abbreviation), None)
        Org_Abbribriated_name = '' if res == None else res['Abbreviation']
        financier_code  = '' if res == None else res['ID']
        Org_Name  = '' if res == None else res['Org_Name']

        return Org_Abbribriated_name ,financier_code, Org_Name

