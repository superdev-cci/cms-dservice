import re
from member.models import Member
from django.db.models import Q

patterns = {
    'sub_district': u'(?<=ต\.)[\u0E01-\u0E4E\w]+',
    'sub_district_full': u'(?<=ตำบล).[\u0E01-\u0E4E\w]+',
    'sub_district_bkk': u'(?<=แขวง).[\u0E01-\u0E4E\w]+',

    'district': u'(?<=อ\.)[\u0E01-\u0E4E\w]+',
    'district_full': u'(?<=อำเภอ).[\u0E01-\u0E4E\w]+',
    'district_bkk': u'(?<=เขต).[\u0E01-\u0E4E\w]+',

    'province': u'(?<=จ\.).[\u0E01-\u0E4E\w]+',
    'province_full': u'(?<=จังหวัด).[\u0E01-\u0E4E\w]+',

    'bkk': u'กทม',
    'bkk_name': u'กรุงเทพมหานคร',
    'bkk_short': u'กรุงเทพฯ',
    'bkk_short2': u'กรุงเทพ',
    'bkk_short3': u'กทม.',

    'zip': u'[0-9]{5}',

}
patterns_list = []

address_extend_list = ['village', 'soi', 'street', ]
address_extend_dict = {
    'village': '',
    'soi': 'ซ.',
    'street': 'ถ.'}
override_fields_list = {
    'district': 'sub_district',
    'amphur': 'district',
    'province': 'province',
    'zip': 'post_code'
}

province_list = ['กรุงเทพมหานคร', 'สมุทรปราการ', 'นนทบุรี', 'ปทุมธานี', 'พระนครศรีอยุธยา', 'อ่างทอง', 'ลพบุรี',
                 'สิงห์บุรี', 'ชัยนาท', 'สระบุรี', 'นครนายก', 'ชลบุรี', 'ระยอง', 'จันทบุรี', 'ตราด', 'ฉะเชิงเทรา',
                 'ปราจีนบุรี', 'สระแก้ว', 'นครราชสีมา', 'บุรีรัมย์', 'สุรินทร์', 'ศรีสะเกษ', 'อุบลราชธานี', 'ยโสธร',
                 'ชัยภูมิ', 'อำนาจเจริญ', 'หนองบัวลำภู', 'ขอนแก่น', 'อุดรธานี', 'เลย', 'หนองคาย', 'มหาสารคาม',
                 'ร้อยเอ็ด', 'กาฬสินธุ์', 'สกลนคร', 'นครพนม', 'มุกดาหาร', 'เชียงใหม่', 'ลำพูน', 'ลำปาง', 'อุตรดิตถ์',
                 'แพร่', 'น่าน', 'พะเยา', 'เชียงราย', 'แม่ฮ่องสอน', 'นครสวรรค์', 'อุทัยธานี', 'กำแพงเพชร', 'สุโขทัย',
                 'พิษณุโลก', 'พิจิตร', 'เพชรบูรณ์', 'สุพรรณบุรี', 'นครปฐม', 'สมุทรสาคร', 'สมุทรสงคราม', 'ตาก',
                 'ราชบุรี', 'กาญจนบุรี', 'เพชรบุรี', 'ประจวบคีรีขันธ์', 'นครศรีธรรมราช', 'กระบี่', 'พังงา', 'ภูเก็ต',
                 'สุราษฎร์ธานี', 'ระนอง', 'ชุมพร', 'สงขลา', 'สตูล', 'ตรัง', 'พัทลุง', 'ปัตตานี', 'ยะลา', 'นราธิวาส',
                 'บึงกาฬ']


def create_match_pattern():
    patterns_list = []
    for k, v in patterns.items():
        patterns_list.append('(?P<%s>%s)' % (k, v))
    match_pattern = '|'.join(patterns_list)
    return match_pattern


def append_address(key, data, address_info):
    if data.get(key, None) != '':
        address_info.update({
            'address': '{} {}{}'.format(address_info['address'], address_extend_dict[key], data[key])
        })
    return address_info


def override_field(key, data, address_info):
    global override_fields_list
    if data.get(key, None) != '' and data.get(key, None) != '0':
        address_info.update({override_fields_list[key]: data[key]})
    return address_info


def get_address_info(data):
    global address_extend_list
    global override_fields_list
    match_pattern = create_match_pattern()
    address_info = {}
    matches = re.finditer(match_pattern, data['address'])
    start_remove = 0
    match_count = 0
    for match in matches:
        match_count += 1
        if match.lastgroup is None:
            continue

        if match.lastgroup.startswith('sub_district'):
            address_info['sub_district'] = match.group()
            if match.lastgroup.endswith('full') or match.lastgroup.endswith('bkk'):
                start_remove = match.span()[0] - 4
            else:
                start_remove = match.span()[0] - 2
        elif match.lastgroup.startswith('district'):
            address_info['district'] = match.group()
            if match.span()[0] < start_remove:
                if match.lastgroup.endswith('full'):
                    start_remove = match.span()[0] - 5
                elif match.lastgroup.endswith('bkk'):
                    start_remove = match.span()[0] - 3
                else:
                    start_remove = match.span()[0] - 2
        elif match.lastgroup.startswith('province'):
            address_info['province'] = match.group()
            if match.span()[0] < start_remove:
                if match.lastgroup.endswith('full'):
                    start_remove = match.span()[0] - 7
                else:
                    start_remove = match.span()[0] - 2
        elif match.lastgroup.startswith('bkk'):
            address_info['province'] = match.group()
        elif match.lastgroup.startswith('zip'):
            address_info['post_code'] = match.group()
    if match_count is not 0:
        address_info['address'] = ' '.join(re.findall('[ก-์\w*-~]+', data['address'][:start_remove]))
    else:
        address_info['address'] = ' '.join(re.findall('[ก-์\w*-~]+', data['address']))
    # list(map(lambda x: append_address(x, data, address_info), address_extend_list))
    # list(map(lambda x: override_field(x, data, address_info), override_fields_list.keys()))
    # address_info['country'] = data['mcode'][:2]
    try:
        address_info['post_code'] = int(address_info['post_code'])
    except Exception as e:
        address_info['post_code'] = 0

    return address_info


def cleaning_province():
    instance = Member.objects.filter(Q(provinceid=""), Q(mcode__startswith="TH"), ~Q(address=""), Q(status_terminate=0),
                                     Q(status_suspend=0))
    for m_obj in instance:
        tmp = get_address_info({'address': m_obj.address})
        if "province" in tmp:
            chk = tmp["province"].strip()
            if chk in province_list:
                m_obj.provinceid = chk
                m_obj.save()
            elif chk in ["กทม", "กทม.", "กรุงเทพ", "กรุงเทพฯ"]:
                m_obj.provinceid = "กรุงเทพมหานคร"
                m_obj.save()


def cleaning_send_province():
    instance = Member.objects.filter(Q(cprovinceid=""), Q(mcode__startswith="TH"), ~Q(caddress=""),
                                     Q(status_terminate=0), Q(status_suspend=0))
    for m_obj in instance:
        tmp = get_address_info({'address': m_obj.caddress})
        if "province" in tmp:
            chk = tmp["province"].strip()
            if chk in province_list:
                m_obj.cprovinceid = chk
                m_obj.save()
            elif chk in ["กทม", "กทม.", "กรุงเทพ", "กรุงเทพฯ"]:
                m_obj.cprovinceid = "กรุงเทพมหานคร"
                m_obj.save()

