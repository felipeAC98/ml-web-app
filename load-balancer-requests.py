# Script to create and send/receive inference requests to load balancer

from urllib import parse, request
import random
import time

load_balancer_url = "http://177.220.85.231/predict_id"
max_requests=400

for i in range(1, max_requests):

	rooms=random.randint(1, 50)
	distance=random.randint(1, 100)
	print(f'Id: {i}, rooms: {rooms}, distance: {distance}')

	data_dic = {"id_request":i, "rooms":rooms, "distance":distance}
	data = parse.urlencode(data_dic).encode()

	# submitting the request
	req = request.Request(load_balancer_url, data, method="POST")

	# receiving the reponse for that request
	resp = request.urlopen(req)
	print(resp.read())
	time.sleep(1)

