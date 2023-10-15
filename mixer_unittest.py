import unittest
#from mixer import Mixer


class TestMixer(unittest.TestCase):
    def test_combine2(self):
        # Проверка правильной работы объединения двух файлов
        self.assertEqual(Mixer.combine2("msfx1.ogg", "urdead.ogg", "wav"), True)
        self.assertEqual(Mixer.combine2("nil","nil"), False)
        
    def test_mix2(self):
        # Проверка работы функции создания микса из двух файлов
        self.assertEqual(Mixer.mix2("fsm.ogg", "fsm.ogg", 350, 250, 500), True)
        self.assertEqual(Mixer.mix2("fsm.ogg", "fsm.ogg", 0, -160), False)
        self.assertEqual(Mixer.mix2("urdead.ogg", "radio1.wav", 0, 0, e1=750, e2=1250), True)
        
    def test_overlay2(self):
        # Проверка работы накладывания одного аудио файла на другой
        self.assertEqual(Mixer.overlay2("urdead.ogg", "urdead.ogg", 500), True)

        
if __name__ == '__main__':
    unittest.main()
