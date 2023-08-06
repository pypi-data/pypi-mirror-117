VER=v0.1

MILL_BIN  = https://github.com/colin4124/knitkit-binary/releases/download/$(VER)/mill
CACHE_TAR = https://github.com/colin4124/knitkit-binary/releases/download/$(VER)/cache.tar.gz

prepare:
	mkdir -p knitkit_mill/assets
	wget -O knitkit_mill/assets/mill $(MILL_BIN)
	wget -O knitkit_mill/assets/cache.tar.gz $(CACHE_TAR)

install-local:
	if [ -d "dist" ]; then rm -r dist; fi
	python3 setup.py bdist_wheel
	pip3 uninstall knitkit-mill -y
	pip3 install --user `ls dist/*.whl`
