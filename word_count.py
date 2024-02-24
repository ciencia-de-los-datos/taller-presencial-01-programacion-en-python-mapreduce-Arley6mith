#
# Escriba la función load_input que recive como parámetro un folder y retorna
# una lista de tuplas donde el primer elemento de cada tupla es el nombre del
# archivo y el segundo es una línea del archivo. La función convierte a tuplas
# todas las lineas de cada uno de los archivos. La función es genérica y debe
# leer todos los archivos de folder entregado como parámetro.
#
# Por ejemplo:
#   [
#     ('text0'.txt', 'Analytics is the discovery, inter ...'),
#     ('text0'.txt', 'in data. Especially valuable in ar...').
#     ...
#     ('text2.txt'. 'hypotheses.')
#   ]
#

import glob
import fileinput
import os

def load_input(input_directory):
    sequence = []
    file_names = glob.glob(input_directory+ '/*')
    with fileinput.input(file_names,encoding= 'utf-8') as f:
        for line in f:
            sequence.append(
                (fileinput.filename(),line))
    
    return sequence

#file_names = load_input('input')
#print(len(file_names))

#
# Escriba una función llamada maper que recibe una lista de tuplas de la
# función anterior y retorna una lista de tuplas (clave, valor). En este caso,
# la clave es cada palabra y el valor es 1, puesto que se está realizando un
# conteo.
#
#   [
#     ('Analytics', 1),
#     ('is', 1),
#     ...
#   ]
#
def mapper(sequence):
    mapper_out = []
    for _,tuple in sequence:
        out = tuple.split()
        for word in out:
            word = word.replace(
                ',','').replace(
                    '.','').replace("'","")
            word = word.lower()
            mapper_out.append((word,1))
    return mapper_out


#
# Escriba la función shuffle_and_sort que recibe la lista de tuplas entregada
# por el mapper, y retorna una lista con el mismo contenido ordenado por la
# clave.
#
#   [
#     ('Analytics', 1),
#     ('Analytics', 1),
#     ...
#   ]
#
def shuffle_and_sort(sequence):
    #sequence.sort(key = lambda x: x[0])
    sorted_out = sorted(sequence,key = lambda x: x[0])
    return sorted_out

#
# Escriba la función reducer, la cual recibe el resultado de shuffle_and_sort y
# reduce los valores asociados a cada clave sumandolos. Como resultado, por
# ejemplo, la reducción indica cuantas veces aparece la palabra analytics en el
# texto.
#
def reducer(sequence):
    reduce_out = []
    diccionario = {}

    # counter = 1
    # for position in range(len(sequence)-1):
    #     if sequence[position] ==  sequence[position+1]:
    #         counter+=1
    #     else:
    #         tuple_out = (sequence[position][0],counter)
    #         reduce_out.append(tuple_out)
    #         #print(counter)
    #         continue

    for key,value in sequence:
        if key not in diccionario.keys():
            diccionario[key]=0
        diccionario[key]+=value
    
    new_sequence = []
    for key,value in diccionario.items():
        tuple=(key,value)
        new_sequence.append(tuple)
    return new_sequence


#print(reduce_out)

#
# Escriba la función create_ouptput_directory que recibe un nombre de directorio
# y lo crea. Si el directorio existe, la función falla.
#
def create_ouptput_directory(output_directory):
    if os.path.exists(output_directory):
        raise FileExistsError(f"The directory '{output_directory}' already exist")
    else:
        os.mkdir(output_directory)
    pass

# create_ouptput_directory('output')
#
# Escriba la función save_output, la cual almacena en un archivo de texto llamado
# part-00000 el resultado del reducer. El archivo debe ser guardado en el
# directorio entregado como parámetro, y que se creo en el paso anterior.
# Adicionalmente, el archivo debe contener una tupla por línea, donde el primer
# elemento es la clave y el segundo el valor. Los elementos de la tupla están
# separados por un tabulador.
#
def save_output(output_directory , sequence):
    #file= os.path.join(output_directory,'part-00000')
    with open(output_directory + '/part-00000', 'w') as fp:
        for  key, value in sequence:
            fp.write(f"{key}\t {value}\n")
    #pass



#
# La siguiente función crea un archivo llamado _SUCCESS en el directorio
# entregado como parámetro.
#
def create_marker(output_directory):
    with open(output_directory + '/_SUCCESS', 'w') as fp:        
        fp.write("")



#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def job(input_directory, output_directory):

    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_ouptput_directory(output_directory)
    save_output(output_directory , sequence)
    create_marker(output_directory)

    pass


if __name__ == "__main__":
    job("input","output2")
