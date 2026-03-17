import unittest
from unittest.mock import patch
import io
import main

class TestMiPrograma(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Gustavo", "24"])
    def test_programa_completo(self, mock_input, mock_stdout):
        # Ejecutar el programa
        main.main()
        
        # Obtener lo que se imprimió
        salida = mock_stdout.getvalue()
        
        # Verificar que el mensaje final está correcto
        self.assertIn("Su nombre es: Gustavo Su edad es: 24", salida)

if __name__ == '__main__':
    unittest.main()