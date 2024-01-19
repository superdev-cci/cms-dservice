staff_group = ('Admin', 'CEO', 'Supervisor',
               'Staff',  'StaffHq',
               'Stock', 'SupervisorStock', 'SupervisorHqStock',
               'SupervisorHq')
super_staff_group = ('Admin', 'CEO', 'SupervisorHq')
member_group = ('Customer', 'Member', 'Member_AG', 'Member_FR', 'Member_Mobile',)


class GroupAuthentication(object):
    staff_group = staff_group
    member_group = member_group
    super_staff_group = super_staff_group
    customer_group = ('Customer',)

    def get_groups(self):
        request = getattr(self, 'request', None)
        if request:
            group = getattr(request, 'user_group', None)
            if group:
                return group.name
            else:
                return None

    def is_staff(self):
        group = self.get_groups()
        if group is not None:
            if group in self.staff_group:
                return True

        return False

    def is_branch_staff(self):
        group = self.get_groups()

        if self.is_member():
            return False

        if group is not None:
            if group not in (*self.super_staff_group, 'StaffHq'):
                return True

        return False

    def is_member(self):
        group = self.get_groups()
        if group is not None:
            if group in self.member_group:
                return True

        return False

    def is_customer(self):
        group = self.get_groups()
        if group is not None:
            if group in self.customer_group:
                return True

        return False

    def is_admin(self):
        group = self.get_groups()
        if group is not None:
            if group == 'Admin':
                return True
        return False
