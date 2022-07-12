import inst
# from inst1 import Inst
#
# list2 = dir(Inst)
#
# list1 = [e for e in dir(Inst) if e.startswith('get')]
# print(list1)

obj = __import__("inst")
getattr(obj)
