# alterar o status inicial
# alterar o status inicial apenas de uma tarefa
# apagem ou modifiquem aquela

#variavel global
count = 0

class TODO:
  def __init__(self, tarefa, status):
    self.tarefa = tarefa
    self.status = status
    self.lista_TODO = []

  def User():
    global count #Acessando a variavel global
    count += 1 #Atualizando o valor global
    id_valor= f'{count}'
    tarefa = input('Tarefa: ')
    dic = {'id': id_valor,'status': 'incompleto' , 'tarefa': tarefa }
    return dic

#chamando a class
obj = TODO('', '')

#Laço de Repetição
while True:
  user = input('Deseja adicionar mais alguma tarefa? (S/N): ')
  if user.lower() == 's':
    tarefa = TODO.User() #chamando a função user dentro da classe TODO
    obj.lista_TODO.append(tarefa)
  else:
    print('Finalizando Tarefas...')
    break

#printando todos os elementos que irao estar dentro da lista
for tarefas in obj.lista_TODO:
  print(tarefas)
