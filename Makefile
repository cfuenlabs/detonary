asset-dist:
	# move Rob.woff to dist/app/_internal/assets
	cp Rob.woff dist/app/_internal/assets
	# move Rob.woff2 to dist/app/_internal/assets
	cp Rob.woff2 dist/app/_internal/assets
	# move words_alpha.sqlite to dist/app/_internal/assets
	cp words_alpha.sqlite dist/app/_internal/assets
	# move index.html to dist/app/_internal/assets
	cp index.html dist/app/_internal/assets

py-install:
	pyinstaller --noconsole app.py