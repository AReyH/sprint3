

#id_comentario
#id_autor
#id_plato
#contenido
#fecha

class Comment:
	def __init__(self,id_comentario,id_autor,id_plato,contenido,fecha):
		self.id_comentario = id_comentario
		self.id_autor = id_autor
		self.id_plato = id_plato
		self.contenido = contenido
		self.fecha = fecha

	

	def show(self):
		return (self.id_comentario,
		self.id_autor,
		self.id_plato,
		self.contenido,
		self.fecha)
		
		

#comment_header = Comment('ID','Autor','Plato','Comentario','Fecha')
comment1 = Comment('1','Hugo','Torta','Deliciosa torta de fresas','01/10/2021')
comment2 = Comment('2','Paco','Galleta','Muy dulce, no me gustó','10/10/2021')
comment3 = Comment('3','Luis','Pan','Recien horneado','20/10/2021')



comentarios = [comment1, comment2, comment3]





