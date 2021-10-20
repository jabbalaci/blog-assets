all:
	Rscript -e "rmarkdown::render('test.Rmd')"

watch:
	ls *.Rmd | entr make all

clean:
	\rm ./test.pdf
