from django.db import transaction
from django.db.models import F, Min, Max
from .models import Member
import sys


def traverse_tree(member, depth, path, cache):
    sys.stdout.write('\r{} '.format(' ' * 50))
    sys.stdout.write("\rProcess: {0} depth :{1} , path={2}".format(member.mcode, depth, path))
    # print("Process: {0} depth :{1} , path={2}".format(member.code, depth, path))
    cache[member.id] = member
    member.line_lft = path
    member.line_depth = depth

    # go to left
    # print('Process L : ', member.code)
    try:
        left = Member.objects.get(upa_code=member.mcode, lr=1)
        if left is not None:
            path = traverse_tree(left, depth + 1, path + 1, cache)
    except:
        pass

    member.line_center = path + 1
    # go to right
    # print('Process R : ', member.code)
    try:
        right = Member.objects.get(upa_code=member.mcode, lr=2)
        if right is not None:
            path = traverse_tree(right, depth + 1, path + 1, cache)
    except:
        pass

    path += 1
    member.line_rgt = path
    return path


def traverse_sponsor_tree(member, depth, path, cache):
    sys.stdout.write('\r{} '.format(' ' * 50))
    sys.stdout.write("\rProcess: {0} depth :{1} , path={2}".format(member.mcode, depth, path))
    cache[member.id] = member
    member.sponsor_lft = path
    member.sponsor_depth = depth

    query = Member.objects.filter(sp_code=member.mcode)
    if query.count() != 0:
        new_path = path
        for x in query:
            new_path = traverse_sponsor_tree(x, depth + 1, new_path + 1, cache)
        member.sponsor_rgt = new_path + 1
        new_path += 1
        return new_path
    else:
        new_path = path + 1
        member.sponsor_rgt = new_path
    return new_path


def calculate_sponsor_tree():
    cache = {}
    entry = Member.objects.get(mcode='TH0000001')
    entry.sponsor_depth = 1
    entry.sponsor_lft = 1

    path = traverse_sponsor_tree(entry, 1, 1, cache)
    # entry.sponsor_rgt = path

    # Save member index
    with transaction.atomic():
        for k, v in cache.items():
            v.save()
    return


def calculate_tree():
    cache = {}

    entry = Member.objects.get(mcode='TH0000001')
    cache[entry.id] = entry
    entry.line_depth = 1
    entry.line_lft = 1

    left = Member.objects.get(upa_code='TH0000001', lr=1)

    path = traverse_tree(left, 2, 2, cache)
    entry.line_center = path + 1
    right = Member.objects.get(upa_code='TH0000001', lr=2)
    path = traverse_tree(right, 2, path + 1, cache)

    entry.line_rgt = path + 1

    with transaction.atomic():
        for k, v in cache.items():
            v.save()
    return


def cal_tree():
    queryset = Member.objects.values('mcode', 'upa_code', 'lr').all()
    all = {x['mcode']: x for x in queryset}
    pool = {}
    for k, v in all.items():
        upline = v['upa_code']
        if upline not in pool:
            pool[upline] = {
                'mcode': upline,
                'left': '',
                'right': '',
            }
        if v['lr'] == 1:
            pool[upline]['left'] = upline