" --------------------------------
" Add to the path
" --------------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))


" --------------------------------
"  Function(s)
" --------------------------------
function! DictInsert()
python3 << endOfPython
index = vim.current.window.cursor[0] - 2
vim.command('close')
vim.command('normal a' + query.get_entry(index))
endOfPython
endfunction

function! DictTranslate(engine, ...)
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
    vim.command('map <buffer> <Enter> :call DictInsert()<CR>')

engine = vim.eval("a:engine").lower()
word = ' '.join(vim.eval("a:000"))
if engine in ['cc', 'dictcc']:
    query = DictCCQuery(word)
elif engine in ['t', 'th', 'thesaurus']:
    query = ThesaurusQuery(word)
if query.num_results > 0:
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
