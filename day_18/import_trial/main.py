#Type1
# import class_test
#
# class_test.method_outside()
# obj = class_test.TestClass()
# obj.method_inside_class()

#Type2
# from class_test import method_outside,TestClass
# #We can import both method and class if we use from.
# method_outside()
# obj = TestClass()
# obj.method_inside_class()

#Type3
# from class_test import *
# method_outside()
# obj = TestClass()
# obj.method_inside_class()

#Type4
# import class_test as ct
# obj = ct.TestClass()
# obj.method_inside_class()
# ct.method_outside()