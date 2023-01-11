import time

from user_agents import parse

from .get_ip import get_client_ip


def get_user_info(request, view, town):
	ua_string = request.META['HTTP_USER_AGENT']
	user_agent = parse(ua_string)
	if user_agent.is_bot:
		msg = 'Посещение бота'
	if user_agent.is_pc:
		msg = 'Посещение с ПК'
	if user_agent.is_tablet:
		msg = 'Посещение с планшета'
	if user_agent.is_mobile:
		msg = 'Посещение с мобильного'
	time_log = time.ctime(time.time() + 10800)
	log_file = open('log_user.txt', 'a')
	ip_client = get_client_ip(request)
	msg_client = time_log + ': ' + msg + ', ' + view + ', ' + town + ', ' + ip_client + '\n'
	log_file.write(msg_client)
	log_file.close()
