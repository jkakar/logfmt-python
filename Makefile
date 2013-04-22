all:
	@test -n "$$VIRTUAL_ENV" || { echo "You're not in a virtualenv.  Create one by running: virtualenv .; . bin/activate"; exit 1; }
	pip install -r requirements.txt --upgrade

check:
	@trial logfmt

clean:
	find . -name \*pyc -exec rm {} \;
	rm -rf _trial_temp
