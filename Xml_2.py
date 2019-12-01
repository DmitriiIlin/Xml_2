import xml.etree.ElementTree as ETree

def get_information_from_file(file_name = "demo.xml"):
    xml1 = ETree.parse(file_name)
    root = xml1.getroot()
    return root

def get_all_nodes_from_file(root = get_information_from_file()):
    #Возвращает список всех узлов документа
    all_nodes = []
    for item in root.iter():
        all_nodes.append(item)
    return all_nodes

def node_parent(children_node = None):
    #Возвращает родителя указанного узла
    children = children_node.tag
    res = None
    nodes = get_all_nodes_from_file()
    for everynode in range( len(nodes) ):
        chilrdens = nodes[everynode].findall(children)
        for every_children in range( len(chilrdens) ):
            if chilrdens[every_children] == children_node:
                res=nodes[everynode]
                break
        if res != None:
            break
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
    nodes = get_all_nodes_from_file()
    for everynode in range( len(nodes) ):
        childrens=nodes[everynode].findall(node_tag)
        #print(childrens)
        for every_children in range( len(childrens) ):
            #print(childrens[every_children])
            nodes[everynode].remove(childrens[every_children])
            #print(nodes[everynode])
        childrens=[]
    return nodes

def delete_all_nodes_2(node_tag = None):
    all_nodes=get_all_nodes_from_file()
    root=get_information_from_file()
    iroot=root
    targets=[]
    for j in range(len(root)):
        print(root[j])
    for everynode in range( len(all_nodes) ):
        if all_nodes[everynode].tag == node_tag:
            targets.append(all_nodes[everynode])
    for every_target in range( len(targets) ):
        parents=get_path(targets[every_target])
        parents.reverse()
        parents.pop(0)
        print(parents)
        # Получили список родителей, нулевой элемент этого списка это саиый дальний предок искомого элемента. Ищем в root этого предка
        # далее у этого предка ищем потомка который является предком для удаляемого элемента. При углублении до ближайшего предка (родителя) удаляется 
        # нулевой элемент из parents, так делается до того момента пока len(parents) !=0
        while len(targets) != 0: #Работаем до того момента пока в targets есть элементы
            while len(parents) != 0: # Цикл до того момента пока в parents никого не останеться
                for i in range(len(root) ): #Перебор элементов в root  
                    if parents[0].tag == root[i].tag : # Мы ищем элемент в root который равен parents[0], то есть самому дальнему предку удаляемого элемента.
                        ancestor = parents.pop(0) # Предок 
                        if len(parents) == 0: #Если в parents некого нет то мы на уровне родителя 
                            root[i].remove(targets[every_target])   # Удаляем искомый элемент у родителя
                            targets.pop(0) #Удаляем элемент из target
                            break                     
                        else:
                            root = ancestor # Переход на более близкого предка
                            i=0
                    else:
                        pass        
    return targets

                

print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
#Z=get_all_nodes_from_file()
#print(Z)
#print(Z[2])
#ZZ=node_parent(Z[6])
#print(ZZ)
#print(get_path(Z[6]))
ZZZ=delete_all_nodes_2('language')
print(ZZZ)

