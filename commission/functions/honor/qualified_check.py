class HonorQualify(object):
    qualify_list = [10000, 20000, 30000, 100000, 300000, 500000, 1500000]
    qualify_position = ['SI', 'GL', 'PE', 'SE', 'EE', 'DE', 'CE']

    @staticmethod
    def check_qualify(balance):
        matches = list(filter(lambda x: x < balance, HonorQualify.qualify_list))
        if len(matches):
            match_index = HonorQualify.qualify_list.index(matches[-1])
            return HonorQualify.qualify_position[match_index]
        return 'MB'

    @staticmethod
    def compare_qualify(first, second):
        if first not in HonorQualify.qualify_position:
            return second

        if second not in HonorQualify.qualify_position:
            return first

        first_index = HonorQualify.qualify_position.index(first)
        sec_index = HonorQualify.qualify_position.index(second)
        first_value = HonorQualify.qualify_list[first_index]
        sec_value = HonorQualify.qualify_list[sec_index]

        if first_value > sec_value:
            return first

        return second
