" --------------------------------
" Add to the path
" --------------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))


" --------------------------------
"  Function(s)
" --------------------------------
function! DictTranslate(engine, word)
python3 << endOfPython

from dicts import DictCCQuery, ThesaurusQuery

def create_new_buffer(contents):
    vim.command('rightbelow split dicts')
    vim.command('normal! ggdG')
    vim.command('setlocal filetype=dicts')
    vim.command('call append(0, {0})'.format(contents))
    vim.command('setlocal readonly')
    vim.command('setlocal buftype=nowrite')
    vim.command('normal! gg')
    vim.command('map <buffer> q :close<CR>')

engine = vim.eval("a:engine").lower()
word = vim.eval("a:word").replace("\"", "")
if engine in ['cc', 'dictcc']:
    query = DictCCQuery(word)
elif engine in ['t', 'th', 'thesaurus']:
    query = ThesaurusQuery(word)
create_new_buffer(query.as_lines())

endOfPython
endfunction


function! DictTranslateWordUnderCursor(engine)
  let word = expand("<cword>")
  :call DictTranslate(a:engine, word)
endfunction


" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! -nargs=1 DictCur call DictTranslateWordUnderCursor(<f-args>)
command! -nargs=* Dict call DictTranslate(<f-args>)
