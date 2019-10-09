import re

prefixes = {
    'mtn': ['0803', '0703', '0903', '0806', '0706', '0813', '0814', '0816', '0810', '0906', '07025', '07026', '0704'],
    'glo': ['0805', '0705', '0905', '0807', '0815', '0905', '0811'],
    'airtel': ['0802', '0902', '0701', '0808', '0708', '0812', '0901', '0907'],
    '9mobile': ['0809', '0909', '0817', '0818', '0908'],
    'ntel': ['0804'],
    'smile': ['0702'],
    'multilinks': ['0709', '07027'],
    'visafone': ['07025', '07026', '0704'],
    'starcomms': ['07028', '07029', '0819'],
    'zoom': ['0707'],
}

area_codes = {
    'Lagos': '01',
    'Ibadan': '02',
    'Abuja': '09',
    'Ado-Ekiti': '30',
    'Ilorin': '31',
    'New Bussa': '33',
    'Akure': '34',
    'Oshogbo': '35',
    'Ile-Ife': '36',
    'Ijebu-Ode': '37',
    'Oyo': '38',
    'Abeokuta': '39',
    'Wukari': '41',
    'Enugu': '42',
    'Abakaliki': '43',
    'Makurdi': '44',
    'Ogoja': '45',
    'Onitsha': '46',
    'Lafia': '47',
    'Awka': '48',
    'Ikare': '50',
    'Owo': '51',
    'Benin City': '52',
    'Warri': '53',
    'Sapele': '54',
    'Agbor': '55',
    'Asaba': '56',
    'Auchi': '57',
    'Lokoja': '58',
    'Okitipupa': '59',
    'Sokoto': '60',
    'Kafanchan': '61',
    'Kaduna': '62',
    'Gusau': '63',
    'Kano': '64',
    'Katsina': '65',
    'Minna': '66',
    'Kontagora': '67',
    'Birnin-Kebbi': '68',
    'Zaria': '69',
    'Pankshin': '73',
    'Azare': '71',
    'Gombe': '72',
    'Jos': '73',
    'Yola': '75',
    'Maiduguri': '76',
    'Bauchi': '77',
    'Hadejia': '78',
    'Jalingo': '79',
    'Aba, Nigeria': '82',
    'Owerri': '83',
    'Port Harcourt': '84',
    'Uyo': '85',
    'Ahoada': '86',
    'Calabar': '87',
    'Umuahia': '88',
    'Yenagoa': '89',
    'Ubiaja': '55',
    'Kwara': '31',
    'Igarra': '57',
    'Ughelli': '53',
    'Uromi': '57'
}


class NigerianPhone:
    def __init__(self, line):
        self.line = re.sub("[^0-9]", "", str(line))
        lists = []
        for key, value in prefixes.items():
            lists.append(value)
        self.prefixes = [item for sublist in lists for item in sublist]
        lists = []
        for key, value in area_codes.items():
            lists.append(value)
        self.area_codes = lists
        self.is_valid_phone = False
        self.is_valid_land_line = False
        self.is_valid()

    def is_valid(self):
        # contains country calling code
        if self.line[:3] == '234':
            # phone number
            if len(self.line) == 13:
                # remove country code for further analysis
                strip_ccc = self.line.replace(self.line[:3], '0')

                # contains valid phone prefix
                if strip_ccc[:5] in self.prefixes or strip_ccc[:4] in self.prefixes:
                    self.is_valid_phone = True
                    return True

            # is a land line
            elif len(self.line) == 11:
                # remove country code
                strip_ccc = self.line.replace(self.line[:3], '0')

                # contains valid area code
                if strip_ccc[:2] in self.area_codes:
                    self.is_valid_land_line = True
                    return True

        # doesn't contain country calling code
        else:
            # check if it starts with any prefix [0807,0906 etc..]
            if self.line[:1] == '0' and len(self.line) == 11 and (self.line[:5] in self.prefixes or self.line[:4] in self.prefixes):
                self.is_valid_phone = True
                return True

            # check if it starts with any prefix without 0 e.g [807,906, 701 etc..]
            elif len(self.line) == 10 and (self.line[:4] in self.prefixes or self.line[:3] in self.prefixes):
                # add the missing zero for completion
                self.line = '0' + self.line
                self.is_valid_phone = True
                return True

            # check if it's a land line starting with 0
            elif self.line[:1] == 0 and self.line[:3].replace(self.line[:1], '') in self.area_codes and len(self.line) == 8:
                self.is_valid_land_line = True
                return True
        return False

    def formatted(self):
        if self.line[:3] == '234':
            return self.line.replace(self.line[:3], '0')
        return self.line

    def get_network(self):
        if self.is_mtn():
            return 'mtn'
        elif self.is_glo():
            return 'glo'
        elif self.is_airtel():
            return 'airtel'
        elif self.is_9mobile():
            return '9mobile'
        elif self.is_smile():
            return 'smile'
        elif self.is_multilinks():
            return 'multilinks'
        elif self.is_visafone():
            return 'visafone'
        elif self.is_ntel():
            return 'ntel'
        elif self.is_starcomms():
            return 'starcomms'
        elif self.is_zoom():
            return 'zoom'
        else:
            return 'unknown'

    def get_area_code(self):
        formatted = self.formatted()
        removed_zero = formatted.replace('0', '')
        code = removed_zero[:2]
        for c in self.area_codes:
            if c == code:
                return c

        return None

    def is_mtn(self):
        if self.formatted()[:5] in prefixes['visafone'] or self.formatted()[:4] in prefixes['mtn']:
            return True
        return False

    def is_glo(self):
        if self.formatted()[:4] in prefixes['glo']:
            return True
        return False

    def is_airtel(self):
        if self.formatted()[:4] in prefixes['airtel']:
            return True
        return False

    def is_9mobile(self):
        if self.formatted()[:4] in prefixes['9mobile']:
            return True
        return False

    def is_smile(self):
        if self.formatted()[:4] in prefixes['smile']:
            return True
        return False

    def is_multilinks(self):
        if self.formatted()[:5] in prefixes['multilinks'] or self.formatted()[:4] in prefixes['multilinks']:
            return True
        return False

    def is_visafone(self):
        if self.formatted()[:5] in prefixes['visafone'] or self.formatted()[:4] in prefixes['visafone']:
            return True
        return False

    def is_ntel(self):
        if self.formatted()[:4] in prefixes['ntel']:
            return True
        return False

    def is_starcomms(self):
        if self.formatted()[:5] in prefixes['starcomms'] or self.formatted()[:4] in prefixes['starcomms']:
            return True
        return False

    def is_zoom(self):
        if self.formatted()[:4] in prefixes['zoom']:
            return True
        return False

    def get_prefixes_by_network(self, network):
        if network in prefixes:
                return prefixes[network]
        else:
                return []

    def get_network_by_prefix(self, prefix):
        for key, value in prefixes.items():
            if prefix in value:
                return key
        else:
                return []

    def get_area_code_by_name(self, code=None):
        for key,value in area_codes.items():
            if key == code:
                return value
        return None

