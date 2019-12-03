import xml.etree.ElementTree as ETree

def get_information_from_file(file_name = "demo.xml"):
    xml1 = ETree.parse(file_name)
    root = xml1.getroot()
    #print(root)
    return root

def get_all_nodes_from_file(root = get_information_from_file()):
    #Возвращает список всех узлов документа
    all_nodes = []
    for item in root.iter():
        all_nodes.append(item)
    return all_nodes

def q_ty_of_nodes(tag=None):
    #Возвращает все узлы с атрибутом tag
    information=get_information_from_file()
    nodes=[]
    nodes_with_tag=[]
    for i in range(0,len(information)):
        nodes.append(information[i])
    for j in range(0,len(nodes)):
        if len(nodes[j]) == 0:
            pass
        else:
            for l in range(0,len(nodes[j])):
                nodes.append(nodes[j][l])
    #print(len(nodes),nodes)
    for everyelement in range(0,len(nodes)):
        if tag == nodes[everyelement].tag:
            nodes_with_tag.append(nodes[everyelement])
    return nodes_with_tag

def node_parent(children_node_tag = None):
    #Возвращает родителя указанного узла
    information=get_information_from_file()
    nodes=[]
    #nodes_with_tag=[]
    for i in range(0,len(information)):
        nodes.append(information[i])
    for j in range(0,len(nodes)):
        if len(nodes[j]) == 0:
            pass
        else:
            for l in range(0,len(nodes[j])):
                nodes.append(nodes[j][l])
    res = None
    for everynode in range( len(nodes) ):
        chilrdens = nodes[everynode].findall(children_node_tag)
        for every_children in range( len(chilrdens) ):
            if chilrdens[every_children].tag == children_node_tag:
                res=nodes[everynode]
                break
        if res != None:
            break
    if res == None:
        for element in range( len(nodes) ):
            if nodes[element].tag == children_node_tag :
                res = information
    return res

def get_path(node = None):
    #Функция ищет все путь к удаляемому элементу через индексы
    data = get_information_from_file()
    root = get_all_nodes_from_file()
    parent = None
    path = []
    while parent != root : 
        parent = node_parent(node)
        if parent == None:
            break 
        #print(parent)
        path.append(parent)
        node = parent 
    return path
        
def delete_all_nodes(node_tag = None):
    #Функция удаляет все узлы по заданному тегу
    targets = q_ty_of_nodes(node_tag)
    data=get_information_from_file()
    #print(data)
    for every_target in range( len(targets) ):
        parent=node_parent(targets[every_target].tag)
        if parent != None:
            for parent_item in data.iter():
                if parent_item.tag == parent.tag:
                    childrens=parent_item.findall(node_tag)
                    for children_item in range( len(childrens) ):
                        parent_item.remove(childrens[children_item])
        else:
            children=data.findall(node_tag)
            for every_children in range( len(children) ):
                data.remove(children[every_children])
    return data
        
        


#print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
#Z=get_all_nodes_from_file()
#print(Z)
#print(Z[2])
#ZZ=node_parent('name')
#print(ZZ)
#print(get_path(Z[6]))
#ZZZ=delete_all_nodes("name")
#print(get_all_nodes_from_file(ZZZ))

