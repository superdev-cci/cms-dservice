from rest_framework.filters import BaseFilterBackend
from django.db import models
from core.group_auth import staff_group


class BranchFilter(BaseFilterBackend):
    def get_branch_filed(self, view):
        search_fields = getattr(view, 'branch_field', None)
        return search_fields

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_branch_filed(view)
        if view.action in ('list',):
            branch = request.query_params.get('branch', None)
            q = {
                '{}__code'.format(search_fields): branch
            }
            queryset = queryset.filter(models.Q(**q))
        return queryset


class BranchStatementFilter(BaseFilterBackend):
    def get_branch_filed(self, view):
        search_fields = getattr(view, 'branch_field', None)
        return search_fields

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_branch_filed(view)
        branch = request.query_params.get('branch', None)
        if branch:
            branches = list(map(lambda x: int(x), branch.split(',')))
            q = {'{}__id__in'.format(search_fields): branches}

            queryset = queryset.filter(models.Q(**q))
        return queryset


class BranchStaffFilter(BranchFilter):
    staff_group = staff_group

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_branch_filed(view)
        user_group = getattr(request, 'user_group', None)
        branch = getattr(request, 'branch', None)

        if user_group is not None:
            if user_group.name in self.staff_group:
                if user_group.name == 'Staff':
                    queryset = queryset.filter(models.Q(**{search_fields: branch}))
            else:
                queryset = queryset.none()
        else:
            queryset = queryset.none()

        return queryset


class BranchNameStaffFilter(BranchStaffFilter):

    def filter_queryset(self, request, queryset, view):

        user_group = getattr(request, 'user_group', None)
        branch = getattr(request, 'branch', None)

        if user_group is not None:
            if user_group.name in self.staff_group:
                if user_group.name == 'Staff':
                    queryset = queryset.filter(models.Q(**{'id': branch.id}))
            else:
                queryset = queryset.none()
        else:
            queryset = queryset.none()

        return queryset
