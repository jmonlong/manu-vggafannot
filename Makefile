all: output/manuscript.pdf

docx: output/manuscript.docx

output/manuscript.pdf: content/*md figures/*png
	docker run -v `pwd`:/app -w /app -u `id -u ${USER}` -it jmonlong-manubot bash build/build.sh

output/manuscript.docx: content/*md figures/*png
	docker run -v `pwd`:/app -w /app -u `id -u ${USER}` -it jmonlong-manubot bash build/build_docx.sh

docker:
	docker build -t jmonlong-manubot .

.PHONY: all docx docker
