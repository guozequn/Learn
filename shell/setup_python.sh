#!/bin/bash
#
#添加自动补全，python命令历史
#
if [[ $SHELL =~ 'zsh' ]]
    then
    echo "export PYTHONSTARTUP='/root/.pythonstartup'" >> ~/.zshrc
    source ~/.zshrc
    else
    echo "export PYTHONSTARTUP='/root/.pythonstartup'" >> ~/.bashrc
    source ~/.bashrc
fi


exit

cat >> ~/.pythonstartup <<EOF

import os  
import readline  
import rlcompleter  
import atexit 

#tab completion  
readline.parse_and_bind("tab: complete")

#history file  
history_file = os.path.join(os.environ["HOME"],".pythonhistory")  
try:  
    readline.read_history_file(history_file)  
except IOError:  
    pass  
atexit.register(readline.write_history_file,history_file) 

del os,history_file,readline,rlcompleter

EOF
