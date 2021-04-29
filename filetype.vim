" my filetype file
if exists("did_load_filetypes")
   finish
endif
augroup filetypedetect
  au! BufRead,BufNewFile *.oconf	setfiletype oconf
augroup END

