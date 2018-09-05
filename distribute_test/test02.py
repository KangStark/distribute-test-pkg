# coding=utf-8


class test(object):
    """this is a test02 class"""
    def __init__(self):
        self._payload = {'others0': 'other_params0','others1': 'other_params1'}

    def add_body_param(self, k, v):
        """
        添加请求体参数
        :param k:参数名：string
        :param v:参数值
        :return:
        """
        self._payload[k] = v

    def get_members(self):
        """
        获取业务主机
        :return:
        """
        return self.get_body_param().get('members')

    def get_body_param(self):
        return self._payload


    def set_members(self, members):
        """
        添加业务主机
        :param members: 业务主机列表，参数类型：list
        :return:
        """
        if members != []:
            self.add_body_param('members', members)
        if self.get_members() is None:
            self.add_body_param('members', members)
        if members == []:
            self._payload['members'].append({})

    def add_member_param(self, k, v):
        self._payload['members'][len(self.get_members())-1][k] = v

    def add_member_id(self, ID):
        self.add_member_param('id', ID)

    def add_member_port(self, port):
        self.add_member_param('port', port)

t = test()
# 依次添加
t.set_members([])
t.add_member_id('test_id')
t.add_member_port('test_port')
print (t._payload)
t.set_members([])
t.add_member_id('test_id2')
t.add_member_port('test_port2')
print (t._payload)

# 批量添加
t.set_members([{'id':'test_id1','port':'test_port1'},
               {'id':'test_id2','port':'test_port2'},
               {'id':'test_id3','port':'test_port3'}])
print (t._payload)

t.set_members([])
t.add_member_id('test_id2')
t.add_member_port('test_port2')
print (t._payload)
