import numpy as np 
import moderngl as mgl

class VBO:
	def __init__(self.ctx):
		self.vbos = {}
		self.vbo['cube'] = CubeVBO(ctx)

	def __destroy(self):
		[vbo.destroy() for vbo in self.vbos.values()]
		

class BaseVBO:
	def __init__(self, ctx):
		self.ctx = ctx
		self.vbo = self.get_vbo()
		self.format: str = None
		self.attribs: list = None

	def get_vertex_data(self): ...

	def get_vbo(self):
		vertex_data = self.get_vertex_data()
		vbo = self.ctx.buffer(vertext_data)
		return vbo

	def destroy(self):
		self.vbo.release()


class CuseVBO(BaseVBO):
	def __init__(self, ctx):
		super().__init__(ctx)
		self.format = '2f 3f 3f'
		self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']


	@staticmethod
    def get_data(vertice, indices):
        data = [vertice[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

        def get_vertex_data(self):
        # vertex_data = [(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0, 0.8, 0.0)]
        # vertex_data = np.array(vertex_data, dtype="f4")

        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]

        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)

        normals = [ (0, 0, 1) * 6,
                    (1, 0, 0) * 6,
                    (0, 0, -1) * 6,
                    (-1, 0, 0) * 6,
                    (0, 1, 0) * 6,
                    (0, -1, 0) * 6]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data