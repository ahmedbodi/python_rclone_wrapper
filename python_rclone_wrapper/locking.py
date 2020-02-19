from __future__ import print_function
import logging
import time
import os
import fcntl
import errno

class ProcessLock(object):
   """Provides the simplest possible interface to flock-based file locking. Intended for use with the `with` syntax. It will create/truncate/delete the lock file as necessary."""

   def __init__(self, path, timeout = None, refresh_interval = 0.1):
      self._path = path
      self._timeout = timeout
      self._refresh_interval = refresh_interval
      self._fd = None
      self.logger = logging.getLogger(self.__class__.__name__)

   def __enter__(self):
      self._fd = os.open(self._path, os.O_CREAT)
      start_lock_search = time.time()
      while True:
         try:
            fcntl.flock(self._fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            # Lock acquired!
            return
         except (OSError, IOError) as exc:
            if exc.errno == errno.EAGAIN: # [Error 35] Resource Temporarily unavailable (already locked)
                self.logger.exception("Another Process is already running")
                raise
            else:
                self.logger.exception("Error occoured while trying to create process lock %s: %s", self._path, exc)
                raise
         
         # TODO It would be nice to avoid an arbitrary sleep here, but spinning
         # without a delay is also undesirable.
         time.sleep(self._refresh_interval)

   def __exit__(self, *args):
      try:
         os.unlink(self._path)
      except:
         pass

      fcntl.flock(self._fd, fcntl.LOCK_UN)
      os.close(self._fd)
      self._fd = None
