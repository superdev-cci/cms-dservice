from django.db.models import Q, F
from trip.models import TravelPointStack


class TravelPointStackOperator(object):

    def __init__(self, *args, **kwargs):
        self.member = kwargs.get('member', None)
        return

    def pop_gold_stack(self, gold):
        assert self.member is not None, AttributeError('Member is not define')
        instance = TravelPointStack.objects.filter(
            remaining_gold_point__gt=0,
            member=self.member,
        ).first()
        assert instance is not None, AttributeError('Stack not found')
        remaining_gold = gold

        if gold > instance.remaining_gold_point:
            remaining_gold = remaining_gold - instance.remaining_gold_point
            instance.remaining_gold_point = 0
        else:
            instance.remaining_gold_point = instance.remaining_gold_point - gold
            remaining_gold = 0
        instance.save()

        if remaining_gold > 0:
            return self.pop_gold_stack(remaining_gold)

        return

    def pop_silver_stack(self, silver):
        assert self.member is not None, AttributeError('Member is not define')
        instance = TravelPointStack.objects.filter(
            remaining_silver_point__gt=0,
            member=self.member,
        ).first()
        assert instance is not None, AttributeError('Stack not found')
        remaining_silver = silver

        if silver > instance.remaining_silver_point:
            remaining_silver = remaining_silver - instance.remaining_silver_point
            instance.remaining_silver_point = 0
        else:
            instance.remaining_silver_point = instance.remaining_silver_point - silver
            remaining_silver = 0
        instance.save()

        if remaining_silver != 0:
            return self.pop_silver_stack(remaining_silver)

        return

    def push_gold_stack(self, gold):
        assert self.member is not None, AttributeError('Member is not define')
        instance = TravelPointStack.objects.filter(
            ~Q(remaining_gold_point=F('gold_point')),
            member=self.member,
        ).first()

        if instance is None:
            TravelPointStack.objects.create(
                member=self.member,
                gold_point=gold,
                remaining_gold_point=gold,
                silver_point=0,
                remaining_silver_point=0
            )
            return

        remaining_gold = gold
        if remaining_gold > 0:
            if instance.gold_point > instance.remaining_gold_point + gold:
                instance.remaining_gold_point += gold
                remaining_gold = 0
            else:
                remaining_gold = remaining_gold - instance.gold_point
                instance.remaining_gold_point = instance.gold_point
        instance.save()

        if remaining_gold > 0:
            return self.push_gold_stack(remaining_gold)
        return

    def push_silver_stack(self, silver):
        assert self.member is not None, AttributeError('Member is not define')
        instance = TravelPointStack.objects.filter(
            ~Q(remaining_silver_point=F('silver_point')),
            member=self.member,
        ).first()

        if instance is None:
            TravelPointStack.objects.create(
                member=self.member,
                gold_point=0,
                remaining_gold_point=0,
                silver_point=silver,
                remaining_silver_point=silver
            )
            return

        remaining_silver = silver
        if remaining_silver > 0:
            if instance.silver_point > instance.remaining_silver_point + silver:
                instance.remaining_silver_point += silver
                remaining_silver = 0
            else:
                remaining_silver = remaining_silver - instance.silver_point
                instance.remaining_silver_point = instance.silver_point
        instance.save()

        if remaining_silver > 0:
            return self.push_silver_stack(remaining_silver)
        return
