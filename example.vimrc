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

" pip install python-language-server
au User lsp_setup call lsp#register_server({
        \ 'name': 'oconf',
        \ 'cmd': ['java',
        \     '-cp', 'javassist-3.12.1.GA.jar',
        \     '-jar','org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar'],
        \ 'allowlist': ['oconf'],
        \ })

let g:lsp_diagnostics_enabled = 1
let g:lsp_signs_enabled = 1         " enable signs
let g:lsp_diagnostics_echo_cursor = 1 " enable echo under cursor when in normal mode
let g:lsp_log_file = expand('~/vim-lsp.log') 
