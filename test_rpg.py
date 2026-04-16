def test_paciente_es_mayor_de_edad(seld):
    p=Paciente(edad=20)
    self.assertTrue(p.es_mayor_de_edad())
    