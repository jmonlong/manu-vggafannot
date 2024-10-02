all: output/manuscript.pdf

output/manuscript.pdf: content/*md figures/*png
	docker run -v `pwd`:/app -w /app -u `id -u ${USER}` -it jmonlong-manubot bash build/build.sh
