import unittest, Xml_2

class Xml_example():

    def __init__(self):
        self.availible_tags = ["name" , "age" , "sex", "languages" , "pc" , "language" , "pc_item"]
        self.q_ty_of_tags = {"name":1, "age":1, "sex": 1, "languages": 1, "language": 3, "pc": 1, "pc_item": 4}
        self.parents={"name":"data","age":"data","sex":"data","languages":"data","language":"languages","pc":"data","pc_item":"pc"}

obj_for_tests=Xml_example()

class Xml_Tests(unittest.TestCase):

    def test_q_ty_of_nodes(self):
        #Тест метода для поиска всех узлов по заданному тегу
        #input_information=Xml_2.get_information_from_file()
        for everytag in range( len(obj_for_tests.availible_tags) ):
            result=Xml_2.q_ty_of_nodes(obj_for_tests.availible_tags[everytag])
            #print(result)
            if len(result) != 0 :
                if result[0].tag in obj_for_tests.availible_tags:
                    is_it_in_avaliable_tags=1
                else:
                    is_it_in_avaliable_tags=0
                self.assertEqual( 1 , is_it_in_avaliable_tags )
            else:
                for everychildren in range(len(obj_for_tests.availible_tags[everytag])):
                    children_result=Xml_2.q_ty_of_nodes(obj_for_tests.availible_tags[everytag][everychildren])
                    #print(everychildren)
                    if len(children_result) != 0 :
                        if children_result[0].tag in obj_for_tests.availible_tags:
                            is_it_in_avaliable_tags=1
                        else:
                            is_it_in_avaliable_tags=0
                        self.assertEqual( 1 , is_it_in_avaliable_tags )
                    else:
                        pass 
    
    def test_node_parent(self):
        #Тест для поиска родителя
        for everytag in range( len(obj_for_tests.availible_tags) ):
            parent_from_function = Xml_2.node_parent(obj_for_tests.availible_tags[everytag])
            parent_from_set = obj_for_tests.parents[obj_for_tests.availible_tags[everytag]]
            #print(parent_from_function.tag,parent_from_set)
            self.assertEqual( parent_from_function.tag , parent_from_set )

    def test_delete_all_nodes(self):
        #Тест удаления всех элементов с заданным тэгом
        for every_tag in range ( len(obj_for_tests.availible_tags) ):
            nodes = Xml_2.delete_all_nodes(obj_for_tests.availible_tags[every_tag])
            if len(nodes) == 1:
                availible_nodes=nodes.findall(obj_for_tests.availible_tags[every_tag])
                self.assertEqual( None , availible_nodes )
            else:
                for every_children in range ( len(nodes) ):
                    availible_nodes=nodes[every_children].findall(obj_for_tests.availible_tags[every_tag])
                    self.assertEqual( [] , availible_nodes )
 
            


    




if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()


#X=Xml_Tests()
#X.test_q_ty_of_nodes()
 