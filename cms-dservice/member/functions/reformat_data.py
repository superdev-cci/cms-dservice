import re
# import pycountry
import requests
from requests.auth import HTTPBasicAuth
from member.models import Member
# from member.models import MemberLevel
# from member.models import MemberStatus
# from member.models import MemberType
# from member.models import HonorLevel
# from member.models import MemberAddressInfo
# from member.models import Person
# from member.legacy import address as address_builder
# from bank.legacy import account as bank_account
# from cci import legacy_config as legacy


def format_name(person, data):
    pattern = u'[\u0E01-\u0E4E\w]+'
    person_name = re.findall(pattern, data)
    if len(person_name) is 1:
        person['name'] = person_name[0]
        # person['surname'] = ''
    elif len(person_name) is 2:
        person['name'] = person_name[0]
        person['surname'] = person_name[1]
    else:
        person['name'] = person_name[0]
        person['surname'] = person_name[1]
        for i in range(len(person_name) - 2):
            person['surname'] = '{} {}'.format(person['surname'], person_name[i + 2])

    return person


def format_sex(data):
    sex = ''
    if data == 'หญิง':
        sex = 'F'
    elif data == 'ชาย':
        sex = 'M'
    return sex


# def format_nation(data):
#     if data == 'Lao':
#         data = 'LA'
#     elif data == 'USA':
#         c = pycountry.countries.get(name='Thailand')
#         data = c.alpha_2
#     elif data == 'Brunei':
#         data = 'BN'
#     elif data == 'Vietnam':
#         data = 'VN'
#     elif data == 'Korea':
#         data = 'KR'
#     elif data != '':
#         c = pycountry.countries.get(name=data)
#         data = c.alpha_2
#     else:
#         data = ''
#
#     return data


def format_id_card(data):
    pattern = r'\d+'
    id_card = re.findall(pattern, data)
    if len(id_card) is not 0:
        return id_card[0]
    else:
        return ''


def format_mobile_number(data):
    x = re.findall('\d+', data)
    number = ''
    for s in x:
        number += s

    if number == '':
        return None
    try:
        m_number = int(number)
    except Exception as e:
        m_number = 0
    return '{:010}'.format(m_number)


def verified_birthday(data):
    error_lise = (
        '1962--',
        '-543--',
        '-543--03',
        '-543--09',
        '-543--01',
        '-543-11-27',
        '1938--',
        '1947--',
        '1952--'
    )
    if data in error_lise:
        return True
    return False


# def get_status(member, data, cache=None):
#     if cache is None:
#         _m_lv = {x.code: x for x in MemberLevel.objects.all()}
#         _h_lv = {x.code: x for x in HonorLevel.objects.all()}
#         _sta = {x.code: x for x in MemberStatus.objects.all()}
#         _type = {x.code: x for x in MemberType.objects.all()}
#     else:
#         _m_lv = cache.get('level')
#         _h_lv = cache.get('honor')
#         _sta = cache.get('status')
#         _type = cache.get('type')
#
#     member['document'] = {
#         'id_card': False,
#         'id_pass': False,
#         'id_pass_stamp_date': '',
#         'bank': False,
#         'bank_pass': False,
#         'bank_pass_stamp_date': '',
#     }
#
#     if data['doc']['cmp'] == 'ครบ':
#         member['document'] = {
#             **member['document'],
#             'id_card': True,
#             'id_pass': True,
#             'id_pass_stamp_date': data['doc']['bmdate1'],
#         }
#     if data['doc']['cmp2'] == 'ครบ':
#         member['document'] = {
#             **member['document'],
#             'bank': True,
#             'bank_pass': True,
#             'bank_pass_stamp_date': data['doc']['bmdate2'],
#         }
#
#     member['level'] = _m_lv.get('MB')
#     if data['status']['terminate'] is 1:
#         member['status'] = _sta['TR']
#         member['level'] = _m_lv['MB']
#
#     else:
#         if data['level']['level'] == 'TN':
#             member['status'] = _sta['TR']
#         else:
#             if data['status']['suspend'] is 1:
#                 member['status'] = _sta['SP']
#             else:
#                 if data['doc']['cmp'] != 'ครบ' or data['doc']['cmp2'] != 'ครบ':
#                     member['status'] = _sta['WD']
#                 else:
#                     member['status'] = _sta['NL']
#
#     if data['level']['honor'] != '':
#         member['honor'] = _h_lv.get(data['level']['honor'], None)
#         # if member['honor'] is None:
#         #     fail_data['result'].append({data['mcode']: {
#         #         'error': 'Get honor fail',
#         #         'data': data
#         #     }})
#
#     if data['level']['level'] != 'TN':
#         member['level'] = _m_lv.get(data['level']['level'], None)
#     else:
#         member['level'] = _m_lv.get('MB')
#
#     if data['level']['type'] is 1:
#         member['type'] = _type.get('FR')
#     elif data['level']['type'] is 2:
#         member['type'] = _type.get('AG')
#     else:
#         member['type'] = _type.get('MB')
#
#     return member


# def legacy_request(**kwargs):
#     user = kwargs.get('user', 'cci')
#     password = kwargs.get('password', 'cci@2018')
#     endpoint = kwargs.get('endpoint', None)
#     host = kwargs.get('host', legacy.host)
#     port = kwargs.get('port', legacy.port)
#     assert endpoint is not None, AttributeError('end point not found')
#
#     uri = 'http://{}:{}/{}'.format(host, port, endpoint)
#     response = requests.get(uri, auth=HTTPBasicAuth(user, password))
#
#     if response.status_code is 200:
#         data = response.json().get('data')
#
#         return data
#     return None


# def get_member(code, **kwargs):
#     user = 'cci'
#     password = 'cci@2018'
#     member_endpoint = 'api/members/members'
#     host = kwargs.get('host', legacy.host)
#     port = kwargs.get('port', legacy.port)
#     uri = 'http://{}:{}/{}/{}'.format(host, port, member_endpoint, code)
#     response = requests.get(uri, auth=HTTPBasicAuth(user, password))
#
#     if response.status_code is 200:
#         data = response.json().get('data')
#         if response.json().get('message') == 'fail':
#             return None
#         try:
#             member_meta = {
#                 'country': data['mcode'][:2],
#                 'member_code': data['mcode'],
#                 'register_date': data['regDate']
#             }
#             member_meta = get_status(member_meta, data)
#             member_instance = Member(**member_meta)
#
#             person = data['person']
#             person_meta = {
#                 'name_title': person['name_title'],
#                 'age': person['age'],
#                 'sex': format_sex(person['sex']),
#                 'nation': format_nation(person['national']),
#                 'id_card': format_id_card(person['id_card']),
#                 'mobile': format_mobile_number(person['mobile'])
#             }
#             person_meta = format_name(person_meta, person['name'])
#             person_instance = Person(**person_meta)
#
#             address = data['address']
#             address_meta = address_builder.get_address_info(address)
#             address_meta['country'] = data['mcode'][:2]
#             address_instance = MemberAddressInfo(**address_meta)
#
#             try:
#                 member_instance.save()
#             except Exception as e:
#                 raise Exception('Can\'t create member instance' + e)
#
#             try:
#                 person_instance.member = member_instance
#                 person_instance.save()
#             except Exception as e:
#                 member_instance.delete()
#                 raise AttributeError('Can\'t create member person data' + e)
#
#             try:
#                 address_instance.member = member_instance
#                 address_instance.save()
#             except Exception as e:
#                 member_instance.delete()
#                 raise AttributeError('Con\'t create member address info' + e)
#
#                 # bank = data['bank']
#                 # bank_account_instance = bank_account.create_bank_account_instance(bank)
#
#         except Exception as e:
#             raise ValueError(e)
#
#     else:
#         raise ValueError('Not found')
#
#     return member_instance


# def search_member(code, **kwargs):
#     user = 'cci'
#     password = 'cci@2018'
#     member_endpoint = 'api/members/members'
#     host = kwargs.get('host', legacy.host)
#     port = kwargs.get('port', legacy.port)
#
#     uri = 'http://{}:{}/{}/{}'.format(host, port, member_endpoint, code)
#     response = requests.get(uri, auth=HTTPBasicAuth(user, password))
#
#     if response.status_code is 200:
#         data = response.json().get('data')
#     else:
#         data = None
#
#     return data


# def get_update_info(code, **kwargs):
#     user = 'cci'
#     password = 'cci@2018'
#     member_endpoint = 'api/members/members'
#     host = kwargs.get('host', legacy.host)
#     port = kwargs.get('port', legacy.port)
#
#     uri = 'http://{}:{}/{}/{}'.format(host, port, member_endpoint, code)
#     response = requests.get(uri, auth=HTTPBasicAuth(user, password))
#
#     if response.status_code is 200:
#         data = response.json().get('data')
#         member_meta = {
#             'country': data['mcode'][:2],
#             'member_code': data['mcode'],
#             'register_date': data['regDate']
#         }
#         member_meta = get_status(member_meta, data)
#
#         person = data['person']
#         person_meta = {
#             'name_title': person['name_title'],
#             'age': person['age'],
#             'sex': format_sex(person['sex']),
#             'nation': format_nation(person['national']),
#             'id_card': format_id_card(person['id_card']),
#             'mobile': format_mobile_number(person['mobile'])
#         }
#         person_meta = format_name(person_meta, person['name'])
#
#         address = data['address']
#         address_meta = address_builder.get_address_info(address)
#         address_meta['country'] = data['mcode'][:2]
#
#         return member_meta, person_meta, address_meta


# def get_all_member_code(**kwargs):
#     return legacy_request(endpoint='api/members/allmcode', **kwargs)


# def get_all_member(**kwargs):
#     cache = {
#         'level': {x.code: x for x in MemberLevel.objects.all()},
#         'honor': {x.code: x for x in HonorLevel.objects.all()},
#         'status': {x.code: x for x in MemberStatus.objects.all()},
#         'type': {x.code: x for x in MemberType.objects.all()}
#     }
#     all_data = legacy_request(endpoint='api/members/members?all=true', **kwargs)
#     data = []
#     for member in all_data:
#         member_meta = {
#             'country': member['mcode'][:2],
#             'member_code': member['mcode'],
#             'register_date': member['regDate']
#         }
#         member_meta = get_status(member_meta, member, cache)
#
#         person = member['person']
#         person_meta = {
#             'name_title': person['name_title'],
#             'age': person['age'],
#             'sex': format_sex(person['sex']),
#             'nation': format_nation(person['national']),
#             'id_card': format_id_card(person['id_card']),
#             'mobile': format_mobile_number(person['mobile'])
#         }
#         person_meta = format_name(person_meta, person['name'])
#
#         address = member['address']
#         address_meta = address_builder.get_address_info(address)
#         if len(address_meta['address']) >= 31:
#             address_meta['address'] = address_meta['address'][:30]
#         try:
#             post_code = int(address_meta['post_code'])
#         except Exception as e:
#             address_meta['post_code'] = 0
#             print('{} : {}'.format(member['mcode'], str(e)))
#
#         address_meta['country'] = member['mcode'][:2]
#
#         data.append({
#             'member': member_meta,
#             'person': person_meta,
#             'addr': address_meta
#         })
#     return data


# def get_tree(**kwargs):
#     return legacy_request(endpoint='api/members/upline?all=true', **kwargs)


# def get_non_active_member(**kwargs):
#     return legacy_request(endpoint='api/members/report/nonactive', **kwargs)


# def get_member_account(**kwargs):
#     return legacy_request(endpoint='api//members/account', **kwargs)


# def check_document(**kwargs):
#     return legacy_request(**kwargs)


# def fetch_member(mcode, **kwargs):
#     data = legacy_request(endpoint='api/members/members/{}'.format(mcode), **kwargs)
#
#     if data is not None:
#         try:
#             member_meta = {
#                 'country': data['mcode'][:2],
#                 'member_code': data['mcode'],
#                 'register_date': data['regDate']
#             }
#             member_meta = get_status(member_meta, data)
#             member_instance = Member(**member_meta)
#
#             person = data['person']
#             person_meta = {
#                 'name_title': person['name_title'],
#                 'age': person['age'],
#                 'sex': format_sex(person['sex']),
#                 'nation': format_nation(person['national']),
#                 'id_card': format_id_card(person['id_card']),
#                 'mobile': format_mobile_number(person['mobile'])
#             }
#             person_meta = format_name(person_meta, person['name'])
#             person_instance = Person(**person_meta)
#
#             address = data['address']
#             address_meta = address_builder.get_address_info(address)
#             address_meta['country'] = data['mcode'][:2]
#             address_instance = MemberAddressInfo(**address_meta)
#
#             try:
#                 member_instance.save()
#             except Exception as e:
#                 raise Exception('Can\'t create member instance' + e)
#
#             try:
#                 person_instance.member = member_instance
#                 person_instance.save()
#             except Exception as e:
#                 member_instance.delete()
#                 raise AttributeError('Can\'t create member person data' + e)
#
#             try:
#                 address_instance.member = member_instance
#                 address_instance.save()
#             except Exception as e:
#                 member_instance.delete()
#                 raise AttributeError('Con\'t create member address info' + e)
#
#                 # bank = data['bank']
#                 # bank_account_instance = bank_account.create_bank_account_instance(bank)
#
#         except Exception as e:
#             raise ValueError(e)
#
#     return
