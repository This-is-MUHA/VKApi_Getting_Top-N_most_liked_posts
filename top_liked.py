import vk_api
import webbrowser
from time import sleep

def by_likes(x):
	return (x['likes'])['count']

def get_vktools():
	# Your login and password:
	login, password
	vk_session = vk_api.VkApi(login, password)

	try:
		vk_session.auth(token_only=True)
	except vk_api.AuthError as error_msg:
		print(error_msg)
		quit()

	tools = vk_api.VkTools(vk_session)
	return tools

def find_top_liked_posts(profile_id):
	tools = get_vktools()
	wall = tools.get_all('wall.get', 100, {'owner_id': profile_id})
	wall = wall['items']
	url = 'https://vk.com/wall'
	wall.sort(key=by_likes, reverse=True)
	for i in range(5):
		webbrowser.open_new_tab(url+str(profile_id)+'_'+str((wall[i])['id']))
		sleep(0.1)

if __name__ == '__main__':
	# The ID of user of community
	# Community ID must be negative number
	find_top_liked_posts('searched_ID_number');