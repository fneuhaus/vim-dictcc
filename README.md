# vim-dicts
Vim plugin based on the work of Christoph Weinsheimer
[weinshec/vim-dictcc](https://github.com/weinshec/vim-dictcc) for dictionary lookups supporting:
* [**dict.cc**](https://dict.cc)
* [**thesaurus.com**](http://thesaurus.com)

## Requirements
vim-dicts requires vim to be compiled with python3 support. Check by running
```vim
:echo has('python3')
```
in vim, which should return `1`.

Further you need to have the python module
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) installed. which you can do via
your package manager or using
```sh
pip install beautifulsoup4
```
Remember to call this with `sudo` if being installed system-wide.

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/fneuhaus/vim-dicts ~/.vim/bundle/vim-dicts`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'fneuhaus/vim-dicts'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'fneuhaus/vim-dicts'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'fneuhaus/vim-dicts'` to .vimrc
  - Run `:PlugInstall`

## Usage
The plugin supports lookups **ENG <-> DEU** and for synonyms for now and provides a vim-command for
querying e.g.
```vim
:Dict [engine] lunch
```
will query the engine for *lunch* and shows the results in newly created buffer.
Engine could be for example cc for **dict.cc**:
```vim
:Dict cc lunch
```

To make it more convenient to use commands for the different engines can easily be greated in your
vimrc, e.g.
```vim
command! -nargs=1 DictCC :call DictTranslate("cc", <q-args>)
command! -nargs=1 Thesaurus :call DictTranslate("thesaurus", <q-args>)
```

The `DictCur [engine]` instead will query for the word currently under cursor, which is convenient to remap, e.g.
```vim
inoremap <c-s> <Esc>:DictCur cc<CR>
nnoremap <c-s> :DictCur cc<CR>
```
Now **Ctrl-s** in `normal` and `insert` mode will invoke the translation query.

The newly created `dicts` buffer can be closed by pressing the `q` key. The translation in the
line where the cursor is located can be inserted into the current buffer by pressing `Enter`.

## Development
vim-dicts is in an early stage of development and your help appreciated. Feel free to create issues and contribute PRs.
