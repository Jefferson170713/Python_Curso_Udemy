# [J]efferson , Eng. De Produção
from log_mixins import *

#l = LOG('Teste')

#if __name__ == '__main__':
#    l = LogFileMixins()
#    l.Log('Teste1')
l2 = LogPrintMixins()
l2.log_error('Teste2')
l3 = LogFileMixins()
l3.log_success('teste3')
