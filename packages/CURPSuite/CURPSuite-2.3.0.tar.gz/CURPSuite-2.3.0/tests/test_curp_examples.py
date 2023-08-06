#!/usr/bin/env python3

import unittest


class TestCURPExamples(unittest.TestCase):

    def test_inconvenient_words(self) -> None:
        pass


    # def test_name_splitting(self):
    #     curp_items = [
    #         {'curp': 'POPC990709MGTSRL02',
    #          'name': 'CLAUDIA LEONOR POSADA PEREZ',
    #          'result': {'nombre': 'CLAUDIA LEONOR', 'apellido': 'POSADA', 'apellido_m': 'PEREZ'}
    #         },
    #         {'curp': 'MAGE981117MMNCRS05',
    #          'name': 'ESTEFANIA DE LOS DOLORES MACIAS GARCIA',
    #          'result': {'nombre': 'ESTEFANIA DE LOS DOLORES', 'apellido': 'MACIAS', 'apellido_m': 'GARCIA'}
    #         },
    #         {'curp': 'MAPS991116MOCRZN07',
    #          'name': 'SANDRA DEL CARMEN MARTINEZ DE LA PAZ',
    #          'result': {'nombre': 'SANDRA DEL CARMEN', 'apellido': 'MARTINEZ', 'apellido_m': 'DE LA PAZ'}
    #         },
    #         {'curp': 'TAXA990915MNEMXM06',
    #          'name': 'AMBER NICOLE TAMAYO',
    #          'result': {'nombre': 'AMBER NICOLE', 'apellido': 'TAMAYO', 'apellido_m': ''}
    #         },
    #         {'curp': 'MXME991209MGRRSS07',
    #          'name': 'ESMERALDA MARTINEZ MASTACHE',
    #          'result': {'nombre': 'ESMERALDA', 'apellido': 'MARTINEZ', 'apellido_m': 'MASTACHE'}
    #         },
    #         {'curp': 'MACD990727MMMCRRN0',
    #          'name': 'DANIELA IVETTE MARTINEZ CRUZ',
    #          'result': False
    #         }
    #     ]
    #
    #     for i in curp_items:
    #         with self.subTest(i=i):
    #             r = CURPValidator.validate(i['curp'], i['name'])
    #             self.assertEqual(r, i['result'])
