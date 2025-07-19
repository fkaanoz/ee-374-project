## dev
run:
	python ./app/main.py

pip-freeze:
	pip freeze > requirements.txt

pip-install:
	pip install -r requirements.txt

run-db:
	python ./app/backend/database/db.py


## build 
create-installer-mac:
	pyinstaller build_mac.spec

clear-installer-mac:
	rm -rf build
	rm -rf dist

create-installer-win:
	pyinstaller build_win.spec

clear-installer-win:
	Remove-Item -Recurse -Force build
	Remove-Item -Recurse -Force dist
