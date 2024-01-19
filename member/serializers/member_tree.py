from .member import MemberSerializer


class MemberWithTreeSerializer(MemberSerializer):
    class Meta(MemberSerializer.Meta):
        fields = MemberSerializer.Meta.fields

    def to_representation(self, instance):
        request = self.context.get('request')
        stack = []
        if request is not None:
            depth = request.query_params.get('depth', None)
            spdepth = request.query_params.get('spdepth', None)
            data = super(MemberWithTreeSerializer, self).to_representation(instance)
            if depth is not None:
                stack.append(instance)
                data['tree'] = {}
                self.get_depth_data(stack, instance, data['tree'], 0, int(depth) + 1)

            if spdepth is not None:
                data['sponsor'] = []
                self.get_sponser_tree(instance, data['sponsor'], 0, int(spdepth) + 1)

            return data
        else:
            return super(MemberWithTreeSerializer, self).to_representation(instance)

    def get_depth_data(self, stack, instance, data, depth, max_depth):  # stack.append(instance)
        if depth < max_depth and instance is not None:
            down_line = instance.children
            left = None
            right = None
            for child in down_line:
                if child.line_pos == 'L':
                    left = child
                elif child.line_pos == 'R':
                    right = child
            data['member_code'] = instance.code
            data['full_name'] = instance.full_name
            data['status'] = instance.status
            data['level'] = instance.get_level
            data['honor'] = instance.get_honor
            if (depth + 1) < max_depth:
                data['right'] = {}
                data['left'] = {}
                if right is not None:
                    stack.append(instance)
                    self.get_depth_data(stack, right, data['right'], depth + 1, max_depth)
                    instance = stack.pop()
                else:
                    data['right'] = None

                if left is not None:
                    stack.append(instance)
                    self.get_depth_data(stack, left, data['left'], depth + 1, max_depth)
                    stack.pop()
                else:
                    data['left'] = None

        return

    def get_sponser_tree(self, instance, data, depth, max_depth):
        if depth == 0:
            for child in instance.sponsor_children:
                spc = {}
                self.get_sponser_tree(child, spc, depth + 1, max_depth)
                data.append(spc)
        elif depth < max_depth and instance is not None:
            data['member_code'] = instance.code
            data['full_name'] = instance.full_name
            data['status'] = instance.status
            data['level'] = instance.get_level
            data['honor'] = instance.get_honor
            child_data = []
            if (depth + 1) < max_depth:
                for child in instance.sponsor_children:
                    spc = {}
                    self.get_sponser_tree(child, spc, depth + 1, max_depth)
                    child_data.append(spc)
                data['sponsor'] = child_data
