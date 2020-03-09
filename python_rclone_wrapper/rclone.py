import logging
import os
import shlex
import subprocess

class RClone(object):
    def __init__(self, config_path, binary_path='rclone'):
        self.logger = logging.getLogger(self.__class__.__name__)
        if not os.path.exists(config_path) or not os.path.isfile(config_path):
            raise FileNotFoundError("Could Not Find Config File")
        self.config_path = config_path
        self.binary_path = binary_path

    @classmethod
    def commands(cls):
        return [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("_")]

    def _build_command(self, command, arguments=[], flags=[]):
        return shlex.split('{4} --config={0} {1} {2} {3}'.format(
            self.config_path,
            command,
            " ".join(arguments),
            " ".join(flags),
            self.binary_path
        ))

    def _execute(self, command, arguments=[], flags=[]):
        command_with_args = self._build_command(command, arguments, flags)    
        self.logger.debug("Invoking : %s", command_with_args)
        try:
            
            with subprocess.Popen(
                    command_with_args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE) as proc:
                (out, err) = proc.communicate()

                if err:
                    err = err.decode('utf-8').replace('\\n', '\n')
                    self.logger.debug("Error Output: %s", err)

                if out:
                    out = out.decode('utf-8').replace('\\n', '\n')
                    self.logger.debug("Output: %s", out)

                return {
                    "code": proc.returncode,
                    "out": out,
                    "error": err
                }
        except FileNotFoundError as exc:
            self.logger.error("Executable not found. %s", exc)
            return {
                "code": -20,
                "error": exc
            }
        except Exception as exc:
            self.logger.exception("Error running command. Reason: %s", exc)
            return {
                "code": -30,
                "error": exc
            }

    def about(self, arguments=[], flags=[]):
        return self._execute('about', arguments, flags)

    def authorize(self, arguments=[], flags=[]):
        return self._execute('authorize', arguments, flags)

    def cachestats(self, arguments=[], flags=[]):
        return self._execute('cachestats', arguments, flags)

    def cat(self, arguments=[], flags=[]):
        return self._execute('cat', arguments, flags)

    def check(self, arguments=[], flags=[]):
        return self._execute('check', arguments, flags)

    def cleanup(self, arguments=[], flags=[]):
        return self._execute('cleanup', arguments, flags)

    def config(self, arguments=[], flags=[]):
        return self._execute('config', arguments, flags)

    def config_create(self, arguments=[], flags=[]):
        return self._execute('config create', arguments, flags)

    def config_delete(self, arguments=[], flags=[]):
        return self._execute('config delete', arguments, flags)

    def config_disconnect(self, arguments=[], flags=[]):
        return self._execute('config disconnect', arguments, flags)

    def config_dump(self, arguments=[], flags=[]):
        return self._execute('dump', arguments, flags)

    def config_edit(self, arguments=[], flags=[]):
        return self._execute('edit', arguments, flags)

    def config_file(self, arguments=[], flags=[]):
        return self._execute('file', arguments, flags)

    def config_password(self, arguments=[], flags=[]):
        return self._execute('password', arguments, flags)

    def config_providers(self, arguments=[], flags=[]):
        return self._execute('providers', arguments, flags)

    def config_reconnect(self, arguments=[], flags=[]):
        return self._execute('reconnect', arguments, flags)

    def config_show(self, arguments=[], flags=[]):
        return self._execute('show', arguments, flags)

    def config_update(self, arguments=[], flags=[]):
        return self._execute('update', arguments, flags)

    def config_userinfo(self, arguments=[], flags=[]):
        return self._execute('userinfo', arguments, flags)

    def copy(self, arguments=[], flags=[]):
        return self._execute('copy', arguments, flags)

    def copyto(self, arguments=[], flags=[]):
        return self._execute('copyto', arguments, flags)

    def copyurl(self, arguments=[], flags=[]):
        return self._execute('copyurl', arguments, flags)

    def cryptcheck(self, arguments=[], flags=[]):
        return self._execute('cryptcheck', arguments, flags)

    def cryptdecode(self, arguments=[], flags=[]):
        return self._execute('cryptdecode', arguments, flags)

    def dbhashsum(self, arguments=[], flags=[]):
        return self._execute('dbhashsum', arguments, flags)

    def dedupe(self, arguments=[], flags=[]):
        return self._execute('dedup', arguments, flags)

    def delete(self, arguments=[], flags=[]):
        return self._execute('delete', arguments, flags)

    def deletefile(self, arguments=[], flags=[]):
        return self._execute('deletefile', arguments, flags)

    def genautocomplete(self, arguments=[], flags=[]):
        return self._execute('genautocomplete', arguments, flags)

    def genautocomplete_bash(self, arguments=[], flags=[]):
        return self._execute('genautocomplete bash', arguments, flags)

    def genautocomplete_zsh(self, arguments=[], flags=[]):
        return self._execute('genautocomplete zsh', arguments, flags)

    def gendocs(self, arguments=[], flags=[]):
        return self._execute('gendocs', arguments, flags)
 
    def hashsum(self, arguments=[], flags=[]):
        return self._execute('hashsum', arguments, flags)

    def help(self, arguments=[], flags=[]):
        return self._execute('', arguments, flags)

    def link(self, arguments=[], flags=[]):
        return self._execute('link', arguments, flags)

    def listremotes(self, arguments=[], flags=[]):
        return self._execute('listremotes', arguments, flags)

    def ls(self, arguments=[], flags=[]):
        return self._execute('ls', arguments, flags)

    def lsd(self, arguments=[], flags=[]):
        return self._execute('lsd', arguments, flags)

    def lsf(self, arguments=[], flags=[]):
        return self._execute('lsf', arguments, flags)

    def lsjson(self, arguments=[], flags=[]):
        return self._execute('lsjson', arguments, flags)

    def lsl(self, arguments=[], flags=[]):
        return self._execute('lsl', arguments, flags)

    def md5sum(self, arguments=[], flags=[]):
        return self._execute('md5sum', arguments, flags)

    def mkdir(self, arguments=[], flags=[]):
        return self._execute('mkdir', arguments, flags)

    def mount(self, arguments=[], flags=[]):
        return self._execute('mount', arguments, flags)

    def move(self, arguments=[], flags=[]):
        return self._execute('move', arguments, flags)

    def moveto(self, arguments=[], flags=[]):
        return self._execute('moveto', arguments, flags)

    def ncdu(self, arguments=[], flags=[]):
        return self._execute('ncdu', arguments, flags)

    def obscure(self, arguments=[], flags=[]):
        return self._execute('obscure', arguments, flags)

    def purge(self, arguments=[], flags=[]):
        return self._execute('purge', arguments, flags)

    def rc(self, arguments=[], flags=[]):
        return self._execute('rc', arguments, flags)

    def rcat(self, arguments=[], flags=[]):
        return self._execute('rcat', arguments, flags)

    def rcd(self, arguments=[], flags=[]):
        return self._execute('rcd', arguments, flags)

    def rmdir(self, arguments=[], flags=[]):
        return self._execute('rmdir', arguments, flags)

    def rmdirs(self, arguments=[], flags=[]):
        return self._execute('rmdirs', arguments, flags)

    def serve(self, arguments=[], flags=[]):
        return self._execute('serve', arguments, flags)

    def serve_dlna(self, arguments=[], flags=[]):
        return self._execute('serve dlna', arguments, flags)

    def serve_ftp(self, arguments=[], flags=[]):
        return self._execute('serve ftp', arguments, flags)

    def serve_http(self, arguments=[], flags=[]):
        return self._execute('serve http', arguments, flags)

    def serve_restic(self, arguments=[], flags=[]):
        return self._execute('serve restic', arguments, flags)

    def serve_sftp(self, arguments=[], flags=[]):
        return self._execute('serve sftp', arguments, flags)

    def serve_webdav(self, arguments=[], flags=[]):
        return self._execute('serve webdav', arguments, flags)

    def settier(self, arguments=[], flags=[]):
        return self._execute('settier', arguments, flags)

    def sha1sum(self, arguments=[], flags=[]):
        return self._execute('sha1sum', arguments, flags)

    def size(self, arguments=[], flags=[]):
        return self._execute('size', arguments, flags)

    def sync(self, arguments=[], flags=[]):
        return self._execute('sync', arguments, flags)

    def touch(self, arguments=[], flags=[]):
        return self._execute('touch', arguments, flags)

    def tree(self, arguments=[], flags=[]):
        return self._execute('tree', arguments, flags)

    def version(self, arguments=[], flags=[]):
        return self._execute('version', arguments, flags)

