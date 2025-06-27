import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print('(' + '___' + ')')
print('(' + 'o o' + ')' + '____/')
print(' @@      \\')
print('  \\ ____,/')
print('  //   //')
print(' ^^   ^^')