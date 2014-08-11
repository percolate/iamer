develop:
	python setup.py develop

test:
	nosetests

clean:
	rm -rf iamer.egg-info
	rm -rf users.ini groups.ini policies
