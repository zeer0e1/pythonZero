# Abstração
class Log:
  def log(self,msg):
    raise NotImplementedError('Implemente o método log')
  
  def log_error(self,msg):
    return self._log(f'Error: {msg}')
  
  def log_sucess(self,msg):
    return self._log(f'Error: {msg}')


class LogFileMixin(Log):
  def _log(self,msg):
     print(msg)

class LogPrintMixin(Log):
  def _log(self,msg):
     print(f'{msg}  ({self.__class__.__name__}) ')

if __name__ == '__main__':
  l = LogPrintMixin()
  l.log_error('Qualquer coisa') 
