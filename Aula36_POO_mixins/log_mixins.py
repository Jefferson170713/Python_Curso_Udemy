# [J]efferson , Eng. De Produção
class Log:

    def _Log(self, msg):
        raise NotImplementedError('implemente log.')

    def log_error(self, msg):
        return self._Log(f' Error : {msg}')

    def log_success(self, msg):
        return self._Log(f' Success : {msg}')

class LogFileMixins(Log):
    def _Log(self, msg):
        print(msg)
        print(f'{msg}, {self.__class__.__name__}')

class LogPrintMixins(Log):
    def _Log(self, msg):
        print(msg)
        print(f'{msg}, {self.__class__.__name__}')