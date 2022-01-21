set nocompatible hidden laststatus=2

if !filereadable('~/.vim/plug.vim')
  silent !curl --insecure -fLo ~/.vim/plug.vim
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

source ~/.vim/plug.vim

call plug#begin('~/.vim/plugged')
Plug 'prabirshrestha/asyncomplete.vim'
Plug 'prabirshrestha/vim-lsp'
Plug 'prabirshrestha/asyncomplete-lsp.vim'
call plug#end()

" install language-server
" Please make sure that the jar file is found by using absolute paths.
au User lsp_setup call lsp#register_server({
        \ 'name': 'oconf',
        \ 'cmd': ['java',
        \     '-jar','org.oceandsl.configuration.ide-1.3.0-SNAPSHOT-ls.jar'],
        \ 'allowlist': ['oconf'],
        \ })

let g:lsp_diagnostics_enabled = 1
let g:lsp_signs_enabled = 1         " enable signs
let g:lsp_diagnostics_echo_cursor = 1 " enable echo under cursor when in normal mode
let g:lsp_log_file = expand('~/vim-lsp.log') 
