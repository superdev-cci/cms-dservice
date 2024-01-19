import requests
from system.models import LineAgent


class LineNotifyAgentMixIn(object):
    line_url = 'https://notify-api.line.me/api/notify'
    agent_name = ''

    def get_line_notify_agent(self):
        return self.agent_name

    def line_notify(self, message, agent=''):
        if agent == '':
            agent = LineAgent.objects.get(agent=self.get_line_notify_agent())
            is_enable = agent.enable
        else:
            agent = LineAgent.objects.get(agent=agent)
            is_enable = agent.enable

        if is_enable:
            header = {
                'Authorization': 'Bearer {}'.format(agent.token)
            }
            requests.post(self.line_url,
                          headers=header,
                          data={'message': message})
        return
